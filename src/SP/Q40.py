import heapq

INF = int(1e9)
distance: list
graph: list


def solution(N, M, MAP):
    global distance, graph
    distance = [INF] * (N + 1)
    graph = [[] for i in range(N + 1)]

    for i in range(M):
        a, b = MAP[i]
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dijkstra(1, 0)
    cnt = max(distance[1:])
    index = distance.index(cnt)
    return (index, cnt, distance.count(cnt))


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
