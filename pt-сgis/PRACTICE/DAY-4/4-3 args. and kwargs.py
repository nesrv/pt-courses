def avg(*args, **kwargs):

    accuracy = kwargs.get('accuracy',2)
    fill = kwargs.get('fill',10)

    temp = sum(args)/ len(args)
    temp = round(temp, accuracy)
    temp = str(temp).zfill(fill)

    return temp


res1 = avg(1, 2, 4)
res2 = avg(1, 2, 4, accuracy=3, fill=7)
res3 = avg(1, 2, 4,  fill=10)

print(res1)
print(res2)
print(res3)

