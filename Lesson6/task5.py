'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
class Stationery:
    title = ()

    @staticmethod
    def draw():
        print('Запуск отрисовки:')

class Pen(Stationery):
    def __init__(self):
        pass

    def draw(self, title):
        print(f'Пишем {title}')

class Pencil(Stationery):
    def __init__(self):
        pass

    def draw(self, title):
        print(f'Рисуем {title}')

class Handle(Stationery):
    def __init__(self):
        pass

    def draw(self, title):
        print(f'Используем {title}')

line = Stationery()
line.draw()

line_pen = Pen()
line_pen.draw("ручкой")

line_pencil = Pencil()
line_pencil.draw("карандашом")

line_mark = Handle()
line_mark.draw("маркер")
