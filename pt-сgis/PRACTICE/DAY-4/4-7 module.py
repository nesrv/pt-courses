import my_module

print(my_module.name)
res = my_module.avg(1,2,2)
print(res)


from my_module import name, avg

res1 = avg(4,5,7)
print(res1)

if __name__ == "__main__":
    print("самост запуск")
else:
    print('запуск при импорте')
