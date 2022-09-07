'''
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
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
        price = int(input('Цена:'))
        quantity = int(input('Количество:'))
        unit = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
        self.my_unit.update(unit)
        self.my_store.append(self.my_unit)
        return print(f'Текущая позиция на складе -\n {self.my_store}')

    def remove(self):
        name = input('Наименование:')
        quantity = int(input('Количество:'))
        filial = input('Перемещение в филиал:')
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
