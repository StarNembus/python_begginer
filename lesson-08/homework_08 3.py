def type_logger(func):
    def inner(x):
        return type(x)
    return inner


def calc_cube(x):
    return x ** 3


calc_cube = type_logger(calc_cube)
print(calc_cube(3))


def type_logger(func):
    def wrapper(*x):
        return tuple(type(i) for i in range(len(x)))
    return wrapper


def calc_cube(*x):
    return tuple(i**3 for i in range(1, len(x) + 1))


calc_cube_decorated = type_logger(calc_cube())
print(calc_cube_decorated(1, 2, 3))
