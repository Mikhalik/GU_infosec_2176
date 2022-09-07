'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
'''
class Store:
    def __init__(self, name, country, year):
        self.name = name
        self.country = country
        self.year = year

class Printer(Store):
    def __init__(self, name, model, type):
        super().__init__(name, model, type)

class Scaner(Store):
    def __init__(self, name, model, type):
        super().__init__(name, model, type)

class Copier(Store):
    def __init__(self, name, model, type):
        super().__init__(name, model, type)
