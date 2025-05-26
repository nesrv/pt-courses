# Циклы. Практика

s= 'XXXYYXXYZXXYXZYXXXYYXXXXXXXXYZXYXXXYXYZYYZXYXXXXXXXXXYXZXYYXYYYXXXYXYZYYXYXYZXYXXYYXZXXXXYXZXYXYXXXYXXZXXYYZYXXXYYYYZXYYXXZXXXXYXXXYXXXZZXXXZYYZXXZXXXYXXYXXYYXYYXZYXYXZXZYXXYXXXYXXXZYYYYXXXXXZXZXXYXZXZXXZZZYYZXXXXYYZXZYXYYXXZYYXXYXZXXZXXYYXXZXXYYXZXXYXZYXXXXYZXZYXXXYXYYXYXYZYXXXXYXYXXXYXXXXXYYXYXYYXXYZXZYXYXYYZXXXZYXYYYYZYYYZYXXXYYYYYYXZXYYZXZYYXYZZXZXXZYYYYXXXYYXXXXYXZXXYXYXXYYZZZXXYXXXYXYXYXXYZXXYZXXXYXYYXZXYYXXXYXXYXZXZYYXXZXXXXYXYYXXXXZXXYYZZXXXZXXZYXXYXXZYZYXXYYZXYXYYXYYXYYYYZYXXZYYZXXZXYXYZX'
# Определите длину самой длинной последовательности, состоящей из символов X.

# x = 'X'
#
# while x in s:
#     x += 'X'
#
# print(x)
# print(len(x) - 1)

text = "В теории, теория и практика неразделимы. На практике это не так."
vowels = "ауоыэяюёие"
# найти количество гласных(русских) букв

cnt = 0

while vowels:
    letter = vowels[0]
    cnt += text.count(letter)
    vowels = vowels[1:]

print(cnt)

vowels = "ауоыэяюёие"
cnt = 0

for letter in vowels:
    cnt += text.count(letter)

print(cnt)











