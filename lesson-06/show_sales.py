import csv  # для работы с файлом csv для чтения
from sys import argv  # для ввода из консоли

data = argv  # переменная

with open("bakery.csv", encoding="utf-8") as file:  # открытие файла для чтения
    reader = csv.reader(file)
    if len(data) == 1:  # вывод всего списка
        for row in reader:
            print(*row)
    elif len(data) == 2:  # вывод всех записей с номера, равного этому числу
        start = int(data[1]) - 1
        reader = list(reader)
        for i in range(start, len(reader)):
            print(reader[i][0])
    elif len(data) == 3:  # вывод записи, начиная с номера, равного первому числу, по номер, равный второму числу
        start = int(data[1]) - 1
        end = int(data[2])
        reader = list(reader)
        for i in range(start, end):
            print(reader[i][0])
