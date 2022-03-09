"""
음수 가중치를 가진 간선이 없어야 함.
greedy algorithm을 사용
미방문 정점들을 저장하기 위해 우선순위 큐를 사용
"""

INF = int(1e9)
graph: list
N: int


def solution(n, M, I):
    global graph, N
    N = n
    graph = [[INF] * N for _ in range(N)]
    res = 0

    for a in range(N):
        for b in range(N):
            if a==b:
                graph[a][b] =0

    for i in range(M):
        a, b = I[i]
        graph[a - 1][b - 1] = 1

    for k in range(N):
        for a in range(N):
            for b in range(N):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # print(graph, end="\n")
    for i in range(N):
        cnt = 0
        for j in range(N):
            if graph[i][j] != INF or graph[j][i] != INF:
                cnt += 1
        if cnt == N:
            res += 1
    return res
