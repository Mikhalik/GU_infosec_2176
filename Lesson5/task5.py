'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''
plus = 0
numbers = input('Введите числа через пробел:')

myfile = open('task5.txt', 'w')
myfile.writelines(numbers)
myfile.close()
print(numbers)

with open('task5.txt', 'r') as my_file:
     num_list = my_file.read()
     num_list = num_list.split(' ')
     for el in num_list:
         try:
              if el != '':
                  plus = int(el) + plus
              else:
                  str = el
         except:
              print(f'Такое число - {el} не существует ')
     print(f'Cумма всех введенных чисел {plus}')
