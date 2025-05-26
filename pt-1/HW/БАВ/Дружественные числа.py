for n in range(400):
    s=0
    t = 0
    for i in range(1, n):
        if n % i == 0:
            s=s+i
            for j in range(1, s):
                if s % j == 0:
                    t = t+ j
                    if  s==j and t==i:
                        break
print(s,t)
