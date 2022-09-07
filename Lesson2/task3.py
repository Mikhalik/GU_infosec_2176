# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
my_list = ['0','Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
month = int(input('Введите номер месяца от 1 до 12:'))
if month in range(9, 12):
    print(f'{my_list[month]} Осень')
elif month in range(3, 6):
    print(f'{my_list[month]} Весна')
elif month in range(6, 9):
    print(f'{my_list[month]} Лето')
elif  month in range(1, 3) or month == 12:
    print(f'{my_list[month]} Зима')
else:
    print('Нет такого месяца')

seasons = {0: '0', 1: 'Январь',2: 'Февраль',3: 'Март',4: 'Апрель',5: 'Май',6: 'Июнь',7: 'Июль',8: 'Август',9: 'Сентябрь',10: 'Октябрь',11: 'Ноябрь',12: 'Декабрь'}
month = int(input('Введите номер месяца от 1 до 12:'))
if month in range(9, 12):
    print(f'{seasons.get(month)} Осень')
elif month in range(3, 6):
    print(f'{seasons.get(month)} Весна')
elif month in range(6, 9):
    print(f'{seasons.get(month)} Лето')
elif  month in range(1, 3) or month == 12:
    print(f'{seasons.get(month)} Зима')
else:
    print('Нет такого месяца')
