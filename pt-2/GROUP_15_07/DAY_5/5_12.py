# Жадный алгоритм (англ. Greedy algorithm)


# storage = '''
# 43
# 40
# 32
# 40
# 30
# '''.strip().splitlines()

storage = open("boxes.txt").readlines()

storage = [int(x) for x in storage]
storage.sort(reverse=True)

containers = []

while storage:

    box = [storage.pop(0)]
    i = 0

    while i < len(storage):

        if box[-1] - storage[i] >= 5:
            box.append(storage.pop(i))
            continue
        i += 1

    containers.append(box)

print(len(containers), len(containers[0]))
