'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
 Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
 Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

scrname, productivity, hours, rate = argv
productivity = int(productivity)
hours = int(hours)
rate = int(rate)


def my_salary(productivity, hours, rate):
    return (productivity * hours) + rate


print(f'Выработка в часах: {productivity} час.')
print(f'Ставка в час: {hours} руб.')
print(f'Премия: {rate} руб.')
print()
print(f'Зарплата: {my_salary(productivity, hours, rate)} руб.')
