"""
1~N까지의 도시
M개의 단방향 도로
--> 모든 도로의 거리 1
특정 도시 X로 출발
최단 거리가 정확히 K인 모든 도시번호를 출력

x->x : 0(최단거리)
"""

from collections import deque

def solution(node: dict, N: int, K: int, X: int) -> list:
    q = deque([X])
    distance = [-1]*(N+1)
    distance[X] = 0

    while q:
        now = q.popleft()
        for i in node[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                q.append(i)

    if K not in distance:
        print(-1)

    for i, e in enumerate(distance):
        if e == K:
            print(i)


# def solution_(args: list, M, N, K, X) -> list:
#     node = {k: [] for k in range(1, M + 1)}
#     for i, k in args:
#         node[i].append(k)
#     return solution(node, N, K, X)


n, m, k, x = map(int, input().split())
graph = {k: [] for k in range(1, n + 1)}

for _ in range(m):
    a, b = [[] for _ in range(n + 1)]
    graph[a].append(b)

solution(graph, n, k, x)
