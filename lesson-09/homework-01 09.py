import time


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            if self.__color == 'red':
                print(self.__color)
                time.sleep(7)
                self.__color = 'yellow'
                print(self.__color)
                time.sleep(2)
                self.__color = 'green'
            elif self.__color == 'green':
                print(self.__color)
                time.sleep(5)
                self.__color = 'yellow'
                print(self.__color)
                time.sleep(2)
                self.__color = 'red'


a = TrafficLight('red')  # передача имени в объект в класс, с чего начинать
a.running()  # вызов функции



