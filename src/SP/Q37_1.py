"""
https://www.acmicpc.net/problem/11404
"""

INF = int(1e9)
N: int
M: int

def solution():
    D = [[INF] * N for _ in range(N)]

    for a in range(N):
        for b in range(N):
            if a == b:
                D[a][b] = 0

    for i in range(M):
        a, b, c = map(int, input().split())
        if D[a - 1][b - 1] > c:
            D[a - 1][b - 1] = c

    # 플로이드 알고리즘
    for m in range(N):
        for s in range(N):
            for e in range(N):
                D[s][e] = min(D[s][e], D[s][m] + D[m][e])

    for a in range(N):
        for b in range(N):
            if D[a][b] == INF:
                print(0, end=" ")
            else:
                print(D[a][b], end=" ")

        print()


N = int(input())
M = int(input())
solution()
