# Функции высшего порядка

# map lambda  filter reduce


lst = ("Москва", "Рязань1", "Смоленск", "Тверь2", "Томск-20", "орел", "анапа")

res1 = filter(str.isalpha, lst)

# все города на букву T ?

res2 = filter(lambda w: w[0] == "Т", lst)

res3 = filter(str.istitle, lst)

print(*res1)

print(*res2)

print(*res3)
