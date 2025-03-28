class Matrix:
    def __init__(self, data):  # конструктор класса Matrix
        self.data = data  # матрица(объект)

    def __str__(self):  # переопределение метода str
        temp_str = ''   # создание пустой строки для реализации вывода элементов матрицы в удобном виде
        for i in self.data:  # прохождение по элементам(спискам матрицы) data
            for j in i:    # прохождение по элементам элементов матрицы(элементам внутри списка списков)
                temp_str += str(j)  # преобразование к строке элемента списка списков
                temp_str += '\t'    # для красивого вывода
            temp_str += '\n'        # перенос списков на другую строку
        return temp_str             # возврат строки

    def __add__(self, other):      # сложение матриц
        temp_list = []             # создание пустого списка для внесения значений сложения матриц
        for i in range(len(self.data)):   # прохождение по элементам матрицы (ее длине)
            inner_list = []               # создание пустого списка для внесения значений из матрицы
            for j in range(len(self.data[i])):  # прохождение по элементам списка списков по длине матрицы
                inner_list.append(self.data[i][j] + other.data[i][j])  # добавление значений путем сложения элементов из внутренних  списков списка
            temp_list.append(inner_list)  # добавление значений
        return Matrix(temp_list)  # создание новой матрицы (возврат списка списков)


my_list = [[1, 2, 3], [4, 5, 6]]
my_list_2 = [[5, 6, 7], [8, 9, 10]]
a = Matrix(my_list)
b = Matrix(my_list_2)
print(a)
print(b)
print(a + b)
