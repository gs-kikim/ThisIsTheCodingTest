"""
위상 정렬 - 정렬 알고리즘 일종
방향 그래프의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열하는 것"
indegree(진입차수): 특정한 노드로 들어오는 간선의 개수

1. 진입차수가 0인 노드를 큐에 넣는다.
2.1 큐에서 원소를 커내 행당 노드에서 출발하는 간선을 그래프에서 제거
2.2 새롭게 진입차수가 0인 된 노드를 큐에 넣는다.
2.3 큐가 빌 때까지 2의 과정을 반복

https://www.acmicpc.net/problem/3665
"""

from collections import deque


def solution(v, node, m, map) -> int:  # node,edge
    indegree = [0] * (v + 1)
    graph = [[False] * (v + 1) for i in range(v + 1)]

    # 방향 그래프의 모든 간선 정보 입력
    for i in range(v):
        for j in range(i + 1, v):
            graph[node[i]][node[j]] = True
            indegree[node[j]] += 1

    for i in range(m):
        a, b = map[i]
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬 함수
    def topoly_sort():
        result = []
        q = deque()

        for i in range(1, v + 1):
            if indegree[i] == 0:
                q.append(i)

        certain = True
        cycle = False

        for i in range(v):
            if len(q) == 0:
                cycle = True
                break
            if len(q) >= 2:
                certain = False
                break
            now = q.popleft()
            result.append(now)
            for i in range(1, v + 1):
                if graph[now][i]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)

        if cycle:
            return "IMPOSSIBLE"
        elif not certain:
            return "?"
        else:
            return result

    return topoly_sort()
