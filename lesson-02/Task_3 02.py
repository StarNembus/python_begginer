my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in my_list:  # элемент из списка
    new_list = el.split()  # создаем новый список с помощью сплит

    name = new_list[len(new_list)-1]  # переменная, последнее значение из каждого элемента списка

    print(f'Привет, {name.title()}!')  # вывод с помощью функции преобразования имени

