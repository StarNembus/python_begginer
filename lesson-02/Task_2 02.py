gk = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
if len(gk[1]) == 1:  # если длина строки индекса 1  равна 1
    gk[1] = "0" + gk[1]  # к длине индекса прибавляется 0

if len(gk[8][1:]) == 1:  # в индексе 8 3  значения, поэтому берем срез с элемента 1 и проверяем длину
    gk[8] = gk[8][0] + '0' + gk[8][1:]  # вставляем ноль после + если длина числовой части меньше 2

# добавление кавычек
gk[1] = ('"' + gk[1] + '"')
gk[3] = ('"' + gk[3] + '"')
gk[8] = ('"' + gk[8] + '"')

gk = ' '.join(gk)  # скрепляем строку из списка с помощью метода join
print(gk)
