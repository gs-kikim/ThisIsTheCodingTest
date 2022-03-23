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


def solution(N, M, map):
    parent = [0] * (N+1)

    for i in range(1, N+1):
        parent[i] = i

    result = 0
    for i in range(M):
        data = find_parent(parent, map[i])
        if data == 0:
            break
        union_parent(parent, data, data-1)
        result += 1

    return result
