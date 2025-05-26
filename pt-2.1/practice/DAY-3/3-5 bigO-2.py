# bigO
import timeit

# bigO(n)
def capitalization_1(deposit, persent, year):
    for y in range(year):
        deposit += (deposit * persent) / 100
    return deposit

# bigO(1)
def capitalization_2(deposit, persent, year):
    return deposit * (1 + persent / 100) ** year




print (capitalization_1(1000,20,10))
print (capitalization_2(1000,20,10))

t1 = timeit.Timer("capitalization_1(1000, 20, 1000)", "from __main__ import capitalization_1")
t2 = timeit.Timer("capitalization_2(1000, 20, 1000)", "from __main__ import capitalization_2")

print(t1.timeit(10**3))
print(t2.timeit(10**3))


# 100 + n ** 2 + 250 # O(3) -> O(1) - константная сложность

for n in range(100): #O(n)
    100 + n ** 2 + 250  # O(3) -> O(1)


# n * 3 = 3n -> O(n)