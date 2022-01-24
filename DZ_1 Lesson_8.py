import re

def email_parse(email_adress):

    pattern = re.compile(r'^[A-Za-z0-9_]+@[A-Za-z0-9_]+\.[A-Za-z0-9_]')
    result = pattern.match(email_adress)

    if not result:
        raise ValueError (f'Электронный адресс невалиден: {email_adress}')
    return result()

#print(email_parse('username'))
#print(email_parse('someone'))
#print(email_parse('domain'))
#p#rint(email_parse('geekbrains.ru'))
#print(email_parse('geekbrains@mail.ru'))

