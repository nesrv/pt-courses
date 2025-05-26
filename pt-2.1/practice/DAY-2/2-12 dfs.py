# DFS - поиск в глубину

graph = {
    1: {2, 3, 4},
    2: {1, 6, 7},
    3: {1, 8},
    4: {1},
    5: {9},
    6: {2},
    7: {2},
    8: {3},
    9: {10},
    10: {9}
}

visited = [False] * (len(graph) + 1)

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)
dfs(1)

print(visited[1:])


