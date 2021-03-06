from random import choice  # выбор случайного значения из списков


def get_jokes(n_jokes):  # функция, устанавливаем аргумент
    my_list_1 = ["автомобиль", "лес", "огонь", "город", "дом"]
    my_list_2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    my_list_3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = list()  # пустой список

    for i in range(n_jokes):   # цикл осуществляется до конечного значения в списке
        joke = choice(my_list_1) + " " + choice(my_list_2) + " " + choice(my_list_3)  # устанавливаем переменную
        jokes_list.append(joke)  # добавляем пустой список переменную

    return jokes_list  #


print(get_jokes(2))









