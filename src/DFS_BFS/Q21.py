"""
L<=두 인구 수 차이 <=R
int(연합인구수 / 칸 개수)
https://www.acmicpc.net/problem/16234

"""

import math

X = [-1, 0, 1, 0]
Y = [0, -1, 0, 1]
L: int
R: int
N: int
A: list


def open(a, b):
    ch = abs(a - b)
    return (L <= ch and R >= ch)


def unbound(x, y) -> bool:
    return x < 0 or y < 0 or x > N - 1 or y > N - 1


def move(find):
    find = set(find)
    psum = 0
    for x, y in find:
        psum += A[x][y]

    average = math.trunc(psum / len(find))
    for x, y in find:
        A[x][y] = average


def check_open(x, y, MAP) -> list:
    union = []
    for i in range(0, 4):
        x1 = x + X[i]
        y1 = y + Y[i]
        if unbound(x1, y1): continue
        if MAP[x1][y1] != -1 and open(A[x][y], A[x1][y1]):
            union.append((x1, y1))

    return union


def find_and_sum(sx, sy, MAP):
    find = [(sx, sy)]
    for x, y in find:
        find.extend(check_open(x, y, MAP))
        MAP[x][y] = -1

    return find


def solution(n, l, r, graph):
    global L, R, N, A
    N = n
    L = l
    R = r
    A = graph
    res = 0
    m_list = []

    while True:
        MAP = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if MAP[i][j] == 0:
                    find = find_and_sum(i, j, MAP)
                    if len(find) > 1:
                        m_list.append(find)
        if len(m_list) > 0:
            for find in m_list:
                move(find)

            m_list = []
            res += 1
        else:
            break

    return res

# n, l, r = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append((list(map(int, input().split()))))
#
# print(solution(n, l, r, graph))
