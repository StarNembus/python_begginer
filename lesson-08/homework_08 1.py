import re


def email_parse(text):
    domain = re.search('@.+', text)
    name = re.search('.+@', text)
    if domain is None or name is None:
        raise ValueError(f'wrong email:{text}')
    domain = domain.group()[1:]
    name = name.group()[:-1]

    my_dict = {name: domain}
    return my_dict


email = 'someone@geekbrains.ru'
try:
    print(email_parse(email))
except ValueError as v:
    print(v)

