# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = list()
count = int(input('Введите количество элементов списка:'))
while count > 0:
    elements = input('Введите элемент списка:')
    my_list.append(elements)
    print(my_list.index(elements))
    count = count - 1
print(my_list)
new_list = list()
for elements in my_list:
    if my_list.index(elements) % 2 == 0:
        new_list.append(elements)
    else:
        new_list.insert(my_list.index(elements) - 1, elements)
print(new_list)
