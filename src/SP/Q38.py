"""
음수 가중치를 가진 간선이 없어야 함.
greedy algorithm을 사용
미방문 정점들을 저장하기 위해 우선순위 큐를 사용
"""
import heapq

INF = int(1e9)
graph: list
N: int


def solution(n, M, I):
    global graph, N
    N = n
    graph = [[] for _ in range(N)]
    dis = []
    res = 0

    for i in range(M):
        a, b = I[i]
        graph[a - 1].append((b - 1, 1))

    for i in range(N):
        dis.append(dk(i))

    for i in range(N):
        cnt = 0
        for j in range(N):
            if dis[i][j] != INF or dis[j][i] != INF:
                cnt += 1
        if cnt == N:
            res += 1
    return res


def dk(start: int):
    q = []
    distance = [INF] * N

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance
