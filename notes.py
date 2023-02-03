'''
    Приложение заметки Notes.py

'''
import sys
import datetime
from notes_package.notes_class import Notes

def help_notes():
    print('допустимые команды:')
    print('--help|HELP|h                            - информация по командам')
    print('--clear|CLEAR|c                          - удаляет все заметки')
    print('--list|LIST|l all|ALL                    - выводит список всех заметок')
    print('--list|LIST "data"                       - выводит список всех заметок за указанную дату')
    print('--add|ADD|a "title" "text"               - добавляет новую заметку с указанным заголовком и текстом')
    print('--del|DEL|d "title"                      - удаляет заметку с указанным заголовком')
    print('--edit|EDIT|e "title"                    - редактирует заметку с указанным заголовком')
    print('--vcleariew|VIEW"|v "title"              - просматривает заметку с указанным заголовком')
    print('--rename|RENAME|r "old_title" "new_title"- переименовывает заметку')

def parser_command(command, params):

    # создание объекта класса работы с заметками
    note = Notes()

    if command in ("--clear","--CLEAR","--c"):
        note.clear()

    elif command in ("--help","--HELP","--h"):
        help_notes()

    elif command in ("--list","--LIST","--l"):
        if params[0] == "all" or params[0] == "ALL":
            note.get_notes_all()
        else:
            try:
                dt = datetime.datetime.strptime(params[0], '%Y-%m-%d')
                note.get_notes_date(params[0])
            except ValueError:
                print(f'Некорректный формат даты: "{params[0]}" !')
                print("Требуется дата в формате %Y-%m-%d. Пример: 2002-02-02")

    if command in ("--add", "--ADD", "--a"):
        print(command, params)
        note.add_notes(params[0], params[1])

    elif command in ("--del", "--DEL","--d"):
        note.del_note(params[0])

    elif command in ("--edit","--EDIT","--e"):
        note.edit_notes(params[0])

    elif command in ("--view","--VIEW", "--v"):
        note.print_note(params[0])

    elif command in ("--rename", "--RENAME", "--r"):
        note.change_title_note(params[0], params[1])

    elif command == "--print":        
        note._Notes__print_all()

def create_dict_commands():
    '''
    Создание словаря по допустимым командам и числу их параметров
    '''
    params_info = {
        '--list': 1,   '--LIST': 1,  '--l': 1,      # просмотр заголовков заметок
        '--add': 2,    '--ADD': 2,   '--a': 2,      # добавление заметки
        '--del': 1,    '--DEL': 1,   '--d': 1,      # удаление заметки
        '--edit': 1,   '--EDIT': 1,  '--e': 1,      # редактирование заметки
        '--view': 1,   '--VIEW': 1,  '--v': 1,      # просмотр заметки
        '--rename': 2, '--RENAME': 2,'--r': 2,      # переименование заголовка заметки
        '--clear': 0,  '--CLEAR': 0, '--c': 0,      # очистка всего
        '--help': 0,   '--HELP': 0,  '--h': 0,      # помощь по командам
        '--print': 0                                # печать всего (отладочная) - в справке не выводится

        }

    return params_info

if __name__ == '__main__':

    params_info = create_dict_commands()

    param_name = sys.argv[1]

    if param_name not in params_info.keys():
        print(f'Неизвестная команда "{param_name}".')
        help_notes()
        exit(1)

    if (params_info[param_name] != len(sys.argv)-2):
        print(f"Ошибка в числе параметров. Ожидалось - {params_info[param_name]}. Получено - {len(sys.argv)}")
        help_notes()
        exit(1)

    param_value = []
    for i in range(params_info[param_name]):
        param_value.append(sys.argv[i+2])

    parser_command(param_name, param_value)
