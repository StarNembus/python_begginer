m = []  # пустой список кубических чисел от 1 до 1000

coub_list_multiplie_by_seven = []  # значение списка чисел целочисленного остатка от 7

for i in range(1, 1000, 2):  # выборка чисел от 1 до 1000 с шагом 2
    m.append(i ** 3)  # возведение числа в куб и добавление в список m

for i in m:  # проходимся по списку m
    sum_inner = 0  # переменная, которая будет принимать сумму чисел
    el = i
    while i != 0:  # цикл для добавления значений в новый пустой список i значение
        b = i % 10   # объявление переменной, разбивка по числам
        sum_inner += b  # сумма чисел одного значения в новом списке, вкладываемого  список со значениями кратными 7
        i = i // 10  # целочисленное значение
    if sum_inner % 7 == 0:  # число от сложения чисел одного значения из списка, которое делится без остатка на 7
        coub_list_multiplie_by_seven.append(el) # запихиваем числа в список

delta = 17
print(coub_list_multiplie_by_seven)
print(sum(coub_list_multiplie_by_seven))   # считаем и выводим сумму всего списка

print(delta * len(coub_list_multiplie_by_seven) + sum(coub_list_multiplie_by_seven))

for idx in range(len(coub_list_multiplie_by_seven)):
    coub_list_multiplie_by_seven[idx] = coub_list_multiplie_by_seven[idx] + delta

print(sum(coub_list_multiplie_by_seven))
