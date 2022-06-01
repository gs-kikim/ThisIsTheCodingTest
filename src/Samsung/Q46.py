"""
https://www.acmicpc.net/problem/16236
if 1마리 : 먹으러감
else:
  if 가까운 물고기 :위
  if 여러마리 : 왼쪽

"""
from collections import deque

INF = 1e9

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

baby_shark_size = 2
now_x, now_y = 0, 0


def find(n, array, dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] < baby_shark_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


def dfs(n, array):
    dist = [[-1] * n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= baby_shark_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def solution(n, array):
    global now_x, now_y
    global baby_shark_size

    for i in range(n):
        for j in range(n):
            if array[i][j] == 9:
                now_x, now_y = i, j
                array[now_x][now_y] = 0  # ?? 아기 상어 위치를 왜 아무것도 없다고 처리하는가?

    result = 0
    ate = 0
    while True:
        value = find(n, array, dfs(n, array))
        if value == None:
            return result
            break
        else:
            now_x, now_y = value[0], value[1]
            result += value[2]
            array[now_x][now_y] = 0
            ate += 1

            if ate >= baby_shark_size:
                baby_shark_size += 1
                ate = 0
