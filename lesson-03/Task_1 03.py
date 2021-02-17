
def num_translate(eng_val):  # функция, eng_val аргумент в функции
    my_dict = {"zero": "ноль",  # словарь от 0 до 9
               "one": "один",
               "two": "два",
               "three": "три",
               "four": "четыре",
               "five": "пять",
               "six": "шесть",
               "seven": "семь",
               "eight": "восемь",
               "nine": "девять"}

    if eng_val.lower() in my_dict:  # lower приводит вводимые данные к нижнему регистру,если аргумент в словаре найден
        print(my_dict[eng_val.lower()])  # если True, то выводим из словаря значение
    else:
        print(None)    # иначе выводит None


# Test
num_translate("Zero")
num_translate("ZEro")
num_translate("zerO")














