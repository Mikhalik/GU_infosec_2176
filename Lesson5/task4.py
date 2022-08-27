'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
'''
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = open('new_task4.txt', 'w', encoding = 'utf-8')
my_file = open('task4.txt', 'r', encoding = 'utf-8')
text = my_file.read()
print(f'Исходный текст:\n{text}')
my_file.seek(0)
print('\n' f'Измененный текст:')
for line in my_file:
    line = line.split(' ')
    for el in line:
        if el in my_dict.keys():
            newel = my_dict[el]
        line = ' '.join(line)
        line = line.replace(el, newel)
        print(line.rstrip())
        new_file.writelines(line)
        break
new_file.close()
my_file.close()
