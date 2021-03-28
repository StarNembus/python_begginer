class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def auto_go(self):
        print(f"{self.name} {self.color}: Поехали")

    def auto_turn(self, turn):
        print(f"{self.name}: Повернула налево" if turn == 0 else "Повернула направо")

    def auto_stop(self):
        print(f"{self.name}: Стоп")

    def show_speed(self):
        return f"{self.name}: Скорость: {self.speed}"


class TownCar(Car):

    def show_speed(self):
        return f"{self.name}: Скорость {self.speed}. Превышение скорости!!!" \
            if self.speed > 60 else f"{self.name}: Скорость {self.speed}"


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}: Скорость {self.speed}. Превышение скорости!!!" \
            if self.speed < 40 else f"{self.name}: Скорость: {self.speed}"


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


class SportCar(Car):
    def show_speed(self):
        pass


town_car = TownCar('Хэчбэк', 'белый', 35)
town_car.auto_go()
town_car.auto_turn(3)
town_car.auto_stop()
print(town_car.show_speed())


police_car = PoliceCar('авто', 'серый', 150)
police_car.auto_go()
police_car.auto_turn(60)
police_car.auto_stop()
print(police_car.show_speed())
