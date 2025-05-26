# считывание строки и разбиение ее по пробелам
lst_in = input().split()

s = 0
for i in lst_in:
    try:
        if type(int(i)) == int:
            s += int(i)
    except:
        pass
print (s)



# ---------------------------


lst_in = input().split()

def check_number(value):
    try:
        return int(value)
    except:
        return False


print(sum(map(check_number, lst_in)))


# --------------------------------------


lst_in = input().split()


def my_func(string):
    try:
        return int(string)
    except:
        try:
            return float(string)
        except:
            return string
        return string


lst_out = list(map(my_func, lst_in))


# считывание строки и разбиение ее по пробелам
lst_in = input().split()

def convert_to_some_value(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return x

lst_out = list(map(convert_to_some_value, lst_in))