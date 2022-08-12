#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_division(number1, number2):
    return number1 / number2


number1 = int(input('Введите число 1 - '))
number2 = int(input('Введите число 2 - '))
if number2 == 0:
    print('Делить на ноль нельзя!')
else:
    print(my_division(number1,number2))
