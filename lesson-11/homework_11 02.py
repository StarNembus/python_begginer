class MyError(Exception):
    def __init__(self):
        print('Ошибка деления на ноль')


try:
    try:
        print(5 // 0)

    except ZeroDivisionError:
        raise MyError

except MyError:
    print('Обработано исключение MyError')
