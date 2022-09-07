'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_number(cls, date):
        date = date.replace('-','')
        return int(date)

    @staticmethod
    def date_valid(date):
        date_list = date.split('-')
        if int(date_list[0]) > 31 or int(date_list[0]) < 1:
            date_list[0] = "Неверное число месяца"
        if int(date_list[1]) > 12 or int(date_list[1]) < 1:
            date_list[1] = "Неверный месяц"
        if int(date_list[2]) > 2022 or int(date_list[2]) < 0:
            date_list[2]= "Неверный год"
        return ', '.join(date_list)

date = input('Введите дату в формате «день-месяц-год»: ')
print(f'Число из даты: {Date.date_number(date)}')
print(f'Валидность даты: {Date.date_valid(date)}')
