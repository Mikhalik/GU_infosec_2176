'''
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json

total = 0
n = 0
profit_dict = {}
average_dict = {}
with open('task7.txt', 'r') as my_file:
    for line in my_file:
        print(line.rstrip())
        line = line.split(' ')
        profit = int(line[2]) - int(line[3])
        if profit > 0:
            print(f'Выручка: {profit}\n')
            summa = summa + profit
            n = n + 1
            profit_dict[line[0]] = profit
        else:
            print(f'Убыток: {profit}\n')
            profit_dict[line[0]] = profit
    print(f'Средняя выручка фирм: {summa / n}\n')
    average_dict['average_profit'] = summa / n
    my_list = [profit_dict, average_dict]
    print(my_list)
with open('profit.json','w') as j_file:
    json.dump(my_list, j_file, ensure_ascii=False, indent=4)
print(f'\n Файл profit.json сохранен')
