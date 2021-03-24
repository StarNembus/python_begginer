class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'{self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if self.quantity - other.quantity > 0 \
            else 'Воспроизвести разность нельзя'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __floordiv__(self, other):
        return Cell(self.quantity // other.quantity)


a_1 = Cell(70)
a_2 = Cell(25)
print(a_1 + a_2)
print(a_1 - a_2)
print(a_1 * a_2)
print(a_1 // a_2)
