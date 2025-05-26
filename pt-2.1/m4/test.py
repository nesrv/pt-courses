import csv

class Dictionary:
    ... 


f = open('m4/attr.csv', encoding='utf-8')
reader = csv.reader(f)

for row in reader:
    name,value = row
    setattr(Dictionary, name, value)
    

# print(Dictionary.__dict__)
# print(getattr(Dictionary, 'rus'))
    
class Programmer:
    ...   
    
import json
f = open('m4/attr.json', encoding='utf-8')
data = json.load(f)

for key, value in data.items():
    setattr(Programmer, key, value)
    
print(Programmer.__dict__)

