'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''
my_db_goods = list() # список данных о товаров с номером
my_goods_list = list() # перечень товаров
my_price_list = list() # список цен
my_count_list = list() # список количества
my_unit_list = list() # список единиц измерения
my_goods_kort = tuple(list()) # кортеж - данные о товаре
my_goods_dict = dict() # словарь с данными о товарах
my_analitics = dict() # словарь аналитика по ключам свойств товара
n = 1 # номер товара в списке
i = 1 # проверка на ввод нового товара
while i == 1:
    goods = input("Введите название товара:")
    price = input("Введите цену товара:")
    count = input("Введите количество товара:")
    unit = input("Введите единицу измерения товара:")
    my_goods_dict = {'Название': goods, 'Цена': price, 'Количество': count, 'Ед': unit}
    my_goods_kort = (n,my_goods_dict)
    my_db_goods.append(my_goods_kort)
    my_goods_list.append(goods)
    my_price_list.append(price)
    my_count_list.append(count)
    my_unit_list.append(unit)
    quest = input("Добавить еще один товар Да (1), Нет любая клавиша:")
    try:
       i = int(quest)
       n = n + 1
       print('Хорошо')
    except ValueError:
       i = 0
for elements in my_db_goods:
    print(elements)
my_analitics = {'Название': my_goods_list, 'Цена': my_price_list, 'Количество': my_count_list, 'Ед': my_unit_list}
print("Аналитика по товарам")
for elements in my_analitics.items():
    print(elements)
