import itertools  # для значений None
import sys  # для кода 1

with open('users', 'r', encoding='utf-8') as f:  # открываем файл для чтения
    my_list_1 = [el.strip('\n').replace(',', ' ') for el in f]  # strip убираем из элемента\n и replace(заменяем)запятую

with open('hobby', 'r', encoding='utf-8') as h:  # второй файл то же самое
    my_list_2 = [el.strip('\n') for el in h]

if len(my_list_1) < len(my_list_2): # если длина первого списка меньше длины второго выходим с кодом 1
    sys.exit(1)

my_dict = dict(itertools.zip_longest(my_list_1, my_list_2))  # соединяем списки в словарь с помощью zip,
print(my_dict)  # для значения None itertools.zip_longest

test = open('test.txt', 'w', encoding='utf-8')  # записываем словарь с помощью преобразования в строку в новый файл test
test.write(str(my_dict))
test.close()
