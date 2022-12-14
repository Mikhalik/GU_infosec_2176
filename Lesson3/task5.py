'''
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
plus = 0
def sum_func(plus):
    str = " "
    while str != "!":
        my_str = input('Ввести числа: ').split(' ')
        for el in my_str:
            try:
                if el != '!' and el != '':
                    plus = int(el) + plus
                else:
                    str = el
            except:
                print(f'Такое число не существует {el}')
        print(f'Cумма всех введенных чисел {plus}')
    return plus


print('Вводите числа через пробел, затем нажмите Enter для подсчета суммы.'
      ' Чтобы прервать суммирование введите !')
print(f'Общая сумма чисел {sum_func(plus)}')
