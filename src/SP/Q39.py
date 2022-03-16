"""
하나의 정점에서 다른 하나의 정점까지 최단 경로를 구하는 문제 --> Dijkstra, 벨만-포드(음수 가중치 간선이 존재 시)
하나의 정점에서 다른 모든 정점까지의 최단 경로를 구하는 문제 -->BFS
각 모든 정점에서 다른 모든 정점까지의 최단 경로를 구하는 문제 -> 플로이드(Floyd)
"""
import heapq

INF = int(1e9)
distance: list
graph: list


def solution(N, MAP):
    global distance, graph
    distance = [INF] * (N*N)
    graph = [[] for i in range(N*N)]

    for i in range(N):
        for j in range(N):
            a = (i * N) + j
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < N and 0 <= y < N:
                    b = (x * N) + y
                    graph[a].append((b, MAP[x][y]))

    dijkstra(0, MAP[0][0])
    return distance[N*N-1]


def dijkstra(start, value):
    q = []
    heapq.heappush(q, (value, start))
    distance[start] = value
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
