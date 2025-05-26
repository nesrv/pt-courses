#

def do(a,b, op):
    return op(a,b)


def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b


func_fabric = {
    'plus' : lambda a,b : a + b ,
    'minus' : lambda a,b : a - b,
    'mul' : multiply,
    'power' : pow
}

print(func_fabric['plus'](5,5))
print(func_fabric['mul'](5,5))
print(func_fabric['power'](2,10))