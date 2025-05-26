
f = open('TXT.TXT', 'w', encoding='utf-8')

print('hello', file=f, end="_")
print('привет', file=f, end="_")

f.write("\nпривет привет")

while