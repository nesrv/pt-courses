def check_cardnumber(number):
    cn = number[::-1]
    tmp1 = 0
    for i in range(1, len(cn), 2):
        num = int(cn[i]) * 2
        if num > 9:
            num = int(str(num)[0]) + int(str(num)[1])
        tmp1 += int(num)
    tmp2 = 0
    for i in range(0, len(cn), 2):
        tmp2 += int(cn[i])
    return True if ((tmp1 + tmp2) % 10 == 0) else False


somecard = '2200300514986874'
print(check_cardnumber(somecard))