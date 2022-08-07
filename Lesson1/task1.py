# 1)Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
''' 
Переменная в Python не имеет типа.
В памяти создаётся объект определенного типа, а переменная получает на него ссылку.
То есть именно объект в памяти имеет тип, а переменная — просто указатель.
Пример типов объектов: int (целое), float (с плавающей запятой), str (строка), bool (логика) и др.
'''
zero = 0
number = 23
word = 'word'
peace = True
count = number + zero

# Запросим у пользователя день недели - переменная dayofweek и год - переменная year,
# затем выведим ответы на экран.
day_of_week = input("Какой сегодня день недели? ")
year = input("Какой сейчас год? ")
print("Сегодня", day_of_week,"; ", year, "год")
