# lambda + key + lst + str

s = [
    [47, 470],
    [50, 600],
    [60, 480],
    [45, 540],
    [30, 300]
]

# s = [[*row, row[1]/row[0]] for row in s]

print(*s, sep='\n', end='\n\n')

# s.sort(key=lambda x: (x[2], x[0]))

s.sort(key=lambda x: (x[1]/x[0], x[0]))

print(*s, sep='\n')