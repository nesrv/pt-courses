def five(n):
    for i in range(n):
        while i % 2 != 0:
            print(i)
            i -= 1
        print("Done")


# five(100)

def six(n):
    for i in range(n):
        cnt = n * n
        for j in range(cnt):
            if j == 4:
                return -1
            print("Done")


six(200)