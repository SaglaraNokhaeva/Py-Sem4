# Задача 1. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. 
# Окончанием ввода пусть служит пустая строка.


data = open('file.txt', 'a', encoding='UTF-8')

while True:
    string = input('Введите строку: ')
    if string == '':
        break
    data.write(string + '\n')

data.close()


# Задача 2. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество 
# в ней символов и слов.


data = open('file.txt', 'r', encoding='UTF-8')

for s in data.readlines():
print(s, end='')
print(f'Количество символов = {len(s)}')
print(f"Количество слов = {len(s.split())}")
print()
data.close()