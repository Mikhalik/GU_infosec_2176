#3)Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
#  Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

digit = int(input("Введите число от 1 до 9 включительно: "))
amount = digit * (1 + 11 + 111)
print(f'Сумма разрядов = {amount}')