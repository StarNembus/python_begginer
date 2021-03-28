from sys import argv
import csv


def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


data = argv
# csv.register_dialect("bakery.csv", delimiter=",")
with open("bakery.csv", "a", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    if is_number(data[1]):
        print(writer.writerow([data[1]]))
    else:
        print("Введите число")
