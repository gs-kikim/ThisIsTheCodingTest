"""
- 서로소 : 공통 원소가 없는 두 집함. 자신이 속한 집합을 찾을 때, 루트 노드를 재귀적으로 찾습니다.
- 신장트리 : 하나의 그래프가 있을때 모든 노드를 포함하는 부분 그래프
- 크루스칼 알고리즘 : 가능한 초소 비용의 신장 트리를 찾아주는 알고리즘
- 위상 정렬 알고리즘 : 방향 그래프의 모든 노드들을 방향성에 거스르지 않도록 순서대로 나열하는 정렬 기법.
"""


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


def solution(N, M, MAP):
    parent = [0] * (N + 1)
    edges = []
    result = 0
    total_cost = 0

    for i in range(1, N + 1):
        parent[i] = i

    for i in range(M):
        a, b, cost = MAP[i]
        total_cost += cost
        edges.append((cost, a, b))

    edges.sort()  # 비용순 정렬

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return total_cost-result
