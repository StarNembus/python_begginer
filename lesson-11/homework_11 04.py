class Stock:
    def __init__(self, name, price, quantity, numb, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = numb
        self.my_list = []
        self.my_list_one = []
        self.unity = {'model': self.name, 'price': self.price, 'quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'

    def reception(self):

        try:
            a_1 = input(f'Name: ')
            b_1 = int(input(f'Price for each: '))
            c_1 = int(input(f'Quantity: '))
            unique = {'model': a_1, 'price': b_1, 'quantity': c_1}
            self.unity.update(unique)
            self.my_list_one.append(self.unity)
            print(f'Текущий список - {self.my_list_one}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - s, продолжение - Enter')
        s = input(f'--> ')
        if s == 'S' or s == 's':
            self.my_list.append(self.my_list_one)
            print(f'Весь склад -\n {self.my_list}')
            return f'Выход'
        else:
            return Stock.reception(self)


class OfficeEquipment(Stock):
    def my_method(self, name, price, quantity, numb):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = numb


class Printer(OfficeEquipment):
    def to_print(self):
        return f'to print something {self.numb} times'


class Scanner(OfficeEquipment):

    def to_scan(self):
        return f'to scan something {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier something  {self.numb} times'


a = Printer('hp', 2000, 5, 10)
b = Scanner('Canon', 1200, 5, 10)
c = Copier('hp_1', 1500, 1, 15)
print(a.reception())
print(b.reception())
print(c.reception())
print(a.to_print())
print(c.to_copier())
