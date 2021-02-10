duration = int(input("Введите секунды: "))

minutes = duration // 60

sec = duration % 60

hours = minutes // 60
minutes = minutes % 60

days = hours // 24
hours = hours % 24

weeks = days // 7
days = days % 7

# when year = 365 days
year = days // 365
days = days % 365

print(str(year) + " year " + str(days)
      + "d " + "{:02d}:".format(hours) + "{:02d}:".format(minutes) + "{:02d}".format(sec))
