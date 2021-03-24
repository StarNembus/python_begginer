class Road:
    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_formula(self):
        return f'{self._length}m * {self._width}m * {Road.weight}kg * {Road.thickness}sm =' \
               f' {(self._length * self._width * Road.weight * Road.thickness) / 1000} t'


road_1 = Road(5000, 20)
print(road_1.calculate_formula())

