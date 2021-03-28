class CompNums:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'z = {self.b} * i + {self.a}'

    def __add__(self, other):
        return f'z = {self.b + other.b} * i + {self.a * other.a}'

    def __mul__(self, other):
        return f'z = {self.a * other.b + self.b * other.a} * i + {self.a * other.a - self.b * self.b}'


z_1 = CompNums(1, -3)
z_2 = CompNums(2, 3)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
