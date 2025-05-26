#Task1
import json


with open("practice/DAY-3/attr.json",  "r", encoding="utf-8") as file:
    data=json.load(file)
    print(data)

class Programmer:
    ...
# for key, value in data.items():
#     setattr(Programmer, key, value)
    
p1=Programmer()



print(type(data))
p1.__dict__ |=  data

print(hasattr(p1,'job'))


d3 = {**Programmer.__dict__, **data}

print(d3)