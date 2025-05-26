import re
from tempfile import template

text = "стеклянный, стекляный, стеклянная"

search = re.findall(r'стеклянн?[ыйая]*', text)
# print(search)

phone = "89123456789, 89883137443, +79123456789, +59123456789"

# template = r'8\d{10}'
match = r'8[0-9]{10}'

search = re.findall(match, phone)
# print(search)

text = "Google, Gooogle, Goooooogle"

match = r'Go{2,}gle'
search = re.findall(match, text)

print(search)