#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.
def my_func(arg1, arg2, arg3):
    if arg1 > arg2 and arg3 > arg2:
        return arg1 + arg3
    elif arg2 > arg1 and arg3 > arg1 :
        return arg2 + arg3
    elif arg1 > arg3 and arg2 > arg3:
        return arg1 + arg2


arg1 = int(input("Первое число:" ))
arg2 = int(input("Второе число:" ))
arg3 = int(input("Третье число:" ))
print(f'Сумма наибольших двух - {my_func(arg1, arg2, arg3)}')
