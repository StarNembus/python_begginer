from requests import get


def currency_rates(code):  # функция, аргумент code
    my_dict = {"USD": "Доллар США", "EUR": "Евро"}  # словарь
    if code in my_dict:
        response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # значения с сайта
        line = response.text
        index = line.find(my_dict[code]) + len(my_dict[code]) + 14  # находим курс доллара из строки
        str_num = ""        # пустая строка
        while not line[index] == "<":  # пока индекс не станет равен <
            str_num += line[index]   # перебираем значения курса по индексу
            index += 1
        course = float(str_num.replace(",", "."))  # замена запятой в строке на точку
        return course  # возвращаем курс
    else:
        return None   # иначе None


