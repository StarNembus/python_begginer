class Stationery:
    def __init__(self, title='Parker'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Пишем красоту {self.title} ручкой!')


class Pencil(Stationery):
    def draw(self):
        print(f'Лучше всех {self.title} карандаши!')


class Handle(Stationery):
    def draw(self):
        print(f'Сделай жизнь яркой с {self.title} marker!')


stat = Stationery()
stat.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()

