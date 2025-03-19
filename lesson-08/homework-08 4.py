def val_checker(f):
    def chek(func):
        def wrapper(num):
            if f(num):
                print(func(num))
            else:
                raise ValueError(f'wrong val {num}')

        return wrapper

    return chek


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(-5)
except ValueError as error:
    print(error)
