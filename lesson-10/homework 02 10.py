from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    def __init__(self, size, name):
        super().__init__(name)
        self.size = size

    def calculate(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, growth, name):
        super().__init__(name)
        self.growth = growth

    def calculate(self):
        return 2 * self.growth + 0.3


a_1 = Coat(34, 'coach')
print(f'Расход ткани на пальто {"%.2f" % a_1.calculate()}')


a_2 = Costume(175, 'coach')
print(f'Расход ткани на костюм {"%.2f" % a_2.calculate()}')

print(f'Общий расход ткани {"%.2f" % (a_1.calculate() + a_2.calculate())}')


