def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(N, M, map, trevel):
    parent = [0] * N

    for i in range(N):
        parent[i] = i

    for i in range(N):
        for j in range(N):
            if map[i][j] == 1:
                union_parent(parent, i, j)

    p = parent[trevel[0]]
    for i in trevel[1:]:
        if p != parent[i]:
            return "NO"

    return "YES"
