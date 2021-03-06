def thesaurus(*name):
    my_dict = {}

    for el in name:
        first_char = el[0]
        if first_char in my_dict:
            my_dict[first_char].append(el)
        else:
            my_dict[first_char] = list()
            my_dict[first_char].append(el)

    return my_dict


print(thesaurus("Иван", "Марина", "Петр", "Илья", "Паула"))






