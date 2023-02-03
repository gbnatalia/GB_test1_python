import datetime

class find_note:
    '''
     Класс поиска узлов в списке заметок согласно
     заданной дате редактирования
    '''

    def __init__(self, notes, date):
        '''
        конструктор класса
        '''
        self.__notes = notes
        self.__et_dt = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        self.___find_first()

    def __get_data(self, index):
        return datetime.datetime.strptime(self.__notes[index]['date_up'], '%Y-%m-%d %H:%M:%S.%f').date()

    def ___find_first(self):
        '''
        функция получения 1-го индекса, удовлетворяющего дате поиска
        '''
        self.index = -1
        if len(self.__notes) == 0:
            return -1
        first = 0
        last = len(self.__notes) - 1
        while first <= last:
            mid = (first + last) // 2
            dt = self.__get_data(mid)
            if self.__et_dt == dt:
                self.index = mid
                for i in range(mid-1, -1, -1):
                    if self.__et_dt == self.__get_data(i):
                        self.index = i
                    else:
                        break
                return self.index
            elif self.__et_dt < dt:
                last = mid - 1
            else:
                first = mid + 1
        return -1

    def find_next_index(self):
        '''
        получение индекса след.узла в списке заметок, удовлетворяющего условию поиска
        :return: индекс узла, удовлетворяющего условию поиска - если он существует,
                 -1  - в противном случае
        '''
        # текущий индекс
        cur_index = self.index

        # получение следущего индекса
        if self.index > -1:
            self.index += 1
            if self.index >= len(self.__notes) or self.__get_data(self.index) != self.__et_dt:
                self.index = -1

        return cur_index

