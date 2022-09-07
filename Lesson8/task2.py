'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
class DivZeroError(Exception):
    def __init__(self, zero):
        self.zero = zero

number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')
try:
    if int(number_2) == 0:
        raise DivZeroError("На ноль делить нельзя")
except TypeError:
    print("Вы ввели не число")
except ValueError:
    print("Вы ввели не число")
except DivZeroError as err:
    print(err)
else:
    print(int(number_1) / int(number_2))
