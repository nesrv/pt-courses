def pow_one(base, exp):
    result = 1
    cnt = 0
    while exp > 0:
        result *= base
        exp -= 1
        cnt+=1
    return result,cnt

def pow_two(base, exp):
    result = 1
    cnt = 0
    while exp > 0:
        cnt+=1
        if exp % 2 == 0:
            base *= base
            exp //= 2
        else:
            result *= base
            exp -= 1
    return result,cnt


print (pow_one(2,20)) # bigO(n)
print (pow_two(2,100)) # big(log)
