'''
Notes.json:
    [
        {
        "title": "Заметка 1",
        "data_up": 10.01.2023,
        "text": "Текст заметки 1"
        },
        {
        "title": "Заметка 2",
        "data_up": 01.02.2023,
        "text": "Текст заметки 2"
        }
    ]
'''
import json
import os
import datetime
from notes_package.edit_class import Editor
from notes_package.find_date import find_note

class Notes:
    '''
    Класс работы с заметками.
    Класс реализует следующий функционал:
    - чтение списка заметок (все, соответствующие какой то дате)
    - добавление заметки
    - редактирование заметки (текста)
    - смена заголовка заметки
    - вывод содержимого заметки
    - удаление заметки
    - удаление всех заметок
    - удаление всех заметок старше определенной даты
    '''
    __notes = []

    def __load_data(self):
        '''
        загрузка информации по заметкам
        '''
        if os.path.exists('notes.json'):
            with open('notes.json') as json_file:
                self.__notes = json.load(json_file)
                self.__notes = sorted(self.__notes, key=lambda el: el['date_up']) # на всякий случай
        else:
            print("file not exists")

    def __update_data(self):
        '''
        сохранение текущих изменений
        '''
        self.__notes = sorted(self.__notes, key=lambda el: el['date_up'])
        if os.path.exists('notes.json'):
            os.remove('notes.json')
        with open('notes.json', 'w') as outfile:
            json.dump(self.__notes, outfile, indent=4)

    def __print_all(self):
        print("Текущее состояние хранилища заметок:")
        for note in self.__notes:
            print(f"{note['title']} ({note['date_up']}): {note['text']}")

    def __init__(self):
        '''
        конструктор класса
        '''
        self.__load_data()

    def add_notes(self, title, text):
        '''
        Добавление заметки
        :param title: заголовок заметки
        :param text: текст заметки
        '''
        # проверка существования заметки с указанным заголовком
        for note in self.__notes:
            if note['title'] == text:
                print('Заметка с указанным заголовком уже существует:')
                self.print_note(title)
                print('Задайте другой заголовок или редактируйте текущую!')
                return

        # добавление новой заметки
        new_note = {}
        new_note["title"] = title
        new_note["text"] = text
        new_note['date_up'] =  str(datetime.datetime.now())
        self.__notes.append(new_note)
        self.__update_data()

    def get_notes_all(self):
        '''
        получение списка заголовков заметок
        '''
        print("Список заметок:")
        for note in self.__notes:
            print(f"{note['title']}")

    def get_notes_date(self, date):
        '''
        получение списка заголовков заметок за указанную дату
        :param date: дата на которую требуется получить заметки
        '''
        indexs = []
        fn = find_note(self.__notes, date)
        while (True):
            cur_index = fn.find_next_index()
            if cur_index == -1:
                break
            indexs.append(cur_index)

        print(f"Список заметок от {date}:")
        for i in indexs:
            print(f"{self.__notes[i]['title']}")

    def change_title_note(self, old_title, new_title):
        '''
        переименование заметки
        :param old_title:  старый заголовок
        :param new_title:  новый заголовок
        '''
        for note in self.__notes:
            if note['title'] == old_title:
                note['title'] = new_title
                note['date_up'] = str(datetime.datetime.now())
                self.__update_data()
        else:
            print(f'Заметки "{old_title}" не существует')

    def edit_notes(self, title):
        '''
        редактирование заметки
        :param title: заголовок заметки
        '''
        for note in self.__notes:
            if note['title'] == title:
                app = Editor(title, note['text'])
                app.mainloop()
                note['text'] = app.res
                note['date_up'] =  str(datetime.datetime.now())
                self.__update_data()
                return
        else:
            print(f'Заметки "{title}" не существует')

    def print_note(self, title):
        '''
        отображение содержимого заметки
        :param title: заголовок заметки
        '''
        for note in self.__notes:
            if note['title'] == title:
                print(note['text'])
                return
        else:
            print(f'Заметки "{title}" не существует')

    def del_note(self, title):
        '''
        удаление заметки
        :param title: заголовок заметки
        '''
        for ind in range(len(self.__notes)):
            if self.__notes[ind]['title'] == title:
                self.__notes.pop(ind)
                self.__update_data()
                return
        else:
            print(f'Заметки "{title}" не существует')

    def __del_old_notes(self, date):
        '''
        удаление старых заметок (заметок старше даты - date)
        :param date: дата последнего редактирования заметки в формате
         !!! НЕ КОРРЕКТНО !!! ДАТЫ МОЖЕТ НЕ СУЩЕСТВОВАТЬ !!! МЕТОД ДЛЯ СЛЕДУЮЩЕЙ ВЕРСИИ
        '''
        fn = find_note(self.__notes, date)
        find_index = fn.find_next_index()
        if find_index != -1:
            self.__notes = self.__notes[find_index:]

    def clear(self):
        '''
        удаление всех заметок
        '''
        self.__notes = []
        self.__update_data()


if __name__ == '__main__':
    #sm = {}
    #sm["date_up"] = datetime.date.today()
    #print(sm["date_up"])

    #note = {}
    #note["title"] = "111"
    #note["text"] = "222"
    #note['date_up'] = str(datetime.datetime.now())

    my_notes = Notes()
    my_notes.get_notes_date("2023-02-02")

    #my_notes.clear()
    #my_notes.add_notes("Заметка 1", "Текст заметки 1")
    #my_notes.add_notes("Заметка 2", "Текст заметки 2")
    #my_notes.add_notes("Заметка 3", "Текст заметки 3")
    #my_notes._Notes__print_all()

    #my_notes.get_notes_all()
    #my_notes.del_note("Заметка 2")
    #my_notes.get_notes_all()
    #my_notes.print_note("Заметка 1")
    #my_notes.edit_notes("Заметка 1")
    #my_notes.print_note("Заметка 1")
    #my_notes._print_all()

    #text = datetime.date.today()
    #print(text)

    #dt = datetime.datetime.strptime(self.__notes[index]['date_up'], '%Y-%m-%d %H:%M:%S.%f')
    #et_dt = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    #if dt.date() == date:
    #    return index + 1
    #return -1