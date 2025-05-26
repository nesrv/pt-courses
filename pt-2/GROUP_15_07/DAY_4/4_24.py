def f1(tag="h1"):
    def f2(string):
        return f'<{tag}> {string} </{tag}>'

    return f2


# f = f1(tag="span")
# # res = f("Пушкин")
# res = f("Онегин")
# print(res)


def parse(tp=tuple):
    def convert(str):
        str = map(int, str.split())
        return dict.fromkeys(str, None) if tp == dict else tp(str)
        # return dict(zip(str,[0] * len(list(str)))) if tp == dict else tp(str)

    return convert

s = '-5 6 8 11 0 111 -456 3'

# p1 = parse()
# res = p1(s)
# print(res)
#
# p2 = parse(dict)  # хочу словарь с ключами из цифр, значение None
# res2 = p2(s)
#
# print(res2)

s = '1 + 2**10 - 3.14 * 100'

r = eval(s)

print(r)