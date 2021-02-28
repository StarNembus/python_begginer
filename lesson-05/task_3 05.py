import itertools

# имя и имя2 создано для проверки работы генератора
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'имя', 'имя2']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = [el for el in itertools.zip_longest(tutors, klasses) if el[0] is not None]

for i in gen:
    print(i)
