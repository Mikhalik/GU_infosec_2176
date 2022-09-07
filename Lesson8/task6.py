'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''
class Store:
    def __init__(self, name, price, quantity, country, year):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.country = country
        self.year = year
        self.my_store = []
        self.my_unit = {}

    def __str__(self):
        return f'{self.name} цена {self.price} страна {self.country} год {self.year}'

    def add(self):
        name = input('Наименование:')
        while True:
            try:
                price = int(input('Цена:'))
                break
            except:
                print("Введите число")
        while True:
            try:
                quantity = int(input('Количество для перемещения:'))
                break
            except:
                print("Введите число")
        unit = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
        self.my_unit.update(unit)
        self.my_store.append(self.my_unit)
        return print(f'Текущая позиция -\n {self.my_store}')

    def remove(self):
        name = input('Наименование:')
        quantity = int(input('Количество:'))
        filial = input('Наименование филиала:')
        return print(f'В {filial} перемещено {name} {quantity} шт.')

class Printer(Store):
    def __init__(self, name, price, quantity, model, type):
        super().__init__(name, price, quantity, model, type)

class Scaner(Store):
    def __init__(self, name, price, quantity, model, type):
        super().__init__(name, price, quantity, model, type)

class Copier(Store):
    def __init__(self, name, price, quantity, model, type):
        super().__init__(name, price, quantity, model, type)

unit_1 = Printer('hp', 2000, 5, 'A', 10)
unit_2 = Scaner('Canon', 1200, 5, 'B', 10)
unit_3 = Copier('Xerox', 1500, 1, 'C', 15)
print(unit_1.add())
print(unit_2.__str__())
print(unit_3.remove())
