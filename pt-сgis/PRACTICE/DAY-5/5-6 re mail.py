
import re


emails = '''
p+rettyandsimple@example.com 
very.common@example.com 
other.email-with-dash@example.com
x@example.comcom 
example-indeed@strange-example.com
mail@mail.ru

'''


match = r'\S+@\S+\.\S+'

match = r'[A-Za-z_]+@[A-Za-z_]+\.[a-z]{2,3}\b'


search = re.findall(match, emails)

print(*search, sep='\n')