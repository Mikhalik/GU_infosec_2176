'''
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных:
создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''
class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict()

class Position(Worker):

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(f'Полное имя: {full_name}')

    def get_total_income(self):
        total = int(self._income['wage'] + self._income['bonus'])
        print(f'Доход: {total}')

person = Position('name', 'surname', 'position')
person.name = input('Введите имя:')
person.surname = input('Введите фамилию:')
person.position = input('Введите должность:')
person._income['wage'] = int(input('Оклад:'))
person._income['bonus'] = int(input('Премия:'))
person.get_full_name()
person.get_total_income()
