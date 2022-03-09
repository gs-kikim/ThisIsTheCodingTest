INF = int(1e9)


def solution(N, M, I):
    D = [[INF] * N for _ in range(N)]

    for a in range(N):
        for b in range(N):
            if a == b:
                D[a][b] = 0

    for i in range(M):
        a, b, c = I[i]
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
                print("0")
            else:
                print(" "+D[a][b])

    return D
