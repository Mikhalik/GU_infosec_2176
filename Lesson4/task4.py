'''
4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию.
Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
my_list = [3, 5, 9, 22, 43, 43, 0, 124, 123, 4, 123, 3, 7, 58, 0, 19, 18, 0]
print(f'Исходный список - {my_list}')
empty_list = []
new_list = [empty_list.append(el) for el in my_list if el not in empty_list]
print(f'Cписок уникальных значений - {empty_list}')

new_list1 = list(set(my_list))
print(f'Cписок уникальных значений, через множество {new_list1}')
