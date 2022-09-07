'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
class Matrix:
    def __init__(self, *args):
        self.new_list = list(args)

    def __str__(self):
        normal = '\n'.join(map(str, self.new_list))
        normal = normal.replace(',', '').replace('[', '').replace(']', '')
        return normal

    def __add__(self, other):
        total = []
        str_total = []
        for i in range(len(self.new_list)):
            for j in range(len(self.new_list[i])):
                str_total.append(self.new_list[i][j] + other.new_list[i][j])
            total.append(str_total)
            str_total = []
        return Matrix('\n'.join(map(str, total)))

Matr1 = Matrix([3, 5, 2], [4, 5, 3], [3, 4, 8])
print('Первая матрица:')
print(Matr1)
Matr2 = Matrix([7, 2, 9], [8, 5, 6], [0, 0, 1])
print('Вторая матрица:')
print(Matr2)
sum_matrix = Matr1 + Matr2
print('Сумма матриц:')
print(sum_matrix)
