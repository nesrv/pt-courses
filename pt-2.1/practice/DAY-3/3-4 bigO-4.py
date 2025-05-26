def pow_one(base, exp): #O(n)
    result = 1
    cnt = 0
    while exp > 0:
        result *= base
        exp -= 1
        cnt +=1
    print(cnt)
    return result

def pow_two(base, exp): # bigO(log(N))
    result = 1
    cnt = 0
    while exp > 0:
        if exp % 2 == 0:
            base *= base
            exp //= 2
            cnt+=1
        else:
            result *= base
            exp -= 1
            cnt+=1
    print(cnt)
    return result


# 1 + 2*n
# big(O) = O(n)

print(pow_one(2,100))
print(pow_two(2,100))