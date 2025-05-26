import csv

f = open("attr.csv", encoding='utf-8')
reader = csv.reader(f)
attr = dict(reader)


class Dictionary:
    ...

for key, value in attr.items():
    setattr(Dictionary,key,value)


print(Dictionary.__dict__)

print(getattr(Dictionary,'rus'))
print(getattr(Dictionary,'eng'))