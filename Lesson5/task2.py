'''
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
   выполнить подсчёт строк и слов в каждой строке.
'''
# В задаче использовал различные методы подсчета строк и слов.
file = open('task2.txt', 'r')
text = file.read()
strings = len(text.split('\n'))
words = len(text.split())
symbols = len(text)
print(text, '\n')
print('Файл содержит:')
print(f'строк - {strings}, слов - {words}, символов - {symbols}')
file.close()
file = open('task2.txt', 'r')
wordsn = 0
lines = 0
for line in file:
    lines += 1
    wordsn = len(line.split())
    print(f'Слов в {lines} строке: {wordsn}')
file.close()
