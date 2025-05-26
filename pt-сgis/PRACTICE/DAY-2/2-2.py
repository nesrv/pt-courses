# SPLIT + MAP

text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# text = text.split(' ', 5)
text = text.partition('дуб')
# print(text)

lst = '1 2 3 4 5 3.14'

lst = lst.split()

lst = map(float, lst)

print(sum(lst))
# print(*lst)