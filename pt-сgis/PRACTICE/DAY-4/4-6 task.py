def get_html(s, tag='h1'):

    return f'<{tag}> {s} </{tag}>'


# print(get_html('Hello Python'))
# print(get_html('Hello Python', 'div'))
# print(get_html('Hello Python', tag='p'))


def check_pallindrom(s):
    s = s.upper()
    return s == s[::-1]


# print(check_pallindrom('шалаш'))
# print(check_pallindrom('АННА'))
# print(check_pallindrom('Анна'))

def is_odd(x):
    return x % 2


from string import *
chars = ascii_lowercase + ascii_uppercase + digits + '_'


def check_email(email):
    if '@' in email and '.' in email:
        email = email.replace('@','').replace('.','')
        for char in email:
            if not char in chars:
                return "НЕТ"
        return "ДА"
    return "НЕТ"

print(check_email('sc@liblistcom'))