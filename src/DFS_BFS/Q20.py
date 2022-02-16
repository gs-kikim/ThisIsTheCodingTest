"""
상하좌우
가능한
"""
from itertools import combinations


def watch(x, y, i, L):
    if i == 0:
        while y >= 0:
            if L[x][y] == 'S': return True
            if L[x][y] == 'O': return False
            y -= 1
    if i == 1:
        while y < len(L):
            if L[x][y] == 'S': return True
            if L[x][y] == 'O': return False
            y += 1
    if i == 2:
        while x >= 0:
            if L[x][y] == 'S': return True
            if L[x][y] == 'O': return False
            x -= 1
    if i == 3:
        while x < len(L):
            if L[x][y] == 'S': return True
            if L[x][y] == 'O': return False
            x += 1

    return False


def check(T: list, S: list, L: list):
    for x, y in T:
        for i in range(4):
            if watch(x, y, i, L):
                return True
    return False


def getDefence(x, y, x1, y1, q):
    if x == x1:
        q.append((x, y - 1), (x, y + 1))
    if y == y1:
        q.append((x + 1, y), (x - 1, y))
    if (x1, y1) in q:
        return False
    return True


def solution_(T: list, X: list, L: list):
    q = []

    for x, y in T:
        for x1, y1 in X:
            if not getDefence(x, y, x1, y1, q): return False

    for data in combinations(q, 3):
        for x, y in data:
            L[x][y] = 'O'

        if check(T, X, L):
            return True

        for x, y in data:
            L[x][y] = 'X'

    return False


def solution(N: int, L: list):
    dl = []
    T = []
    X = []
    for i in range(0, N):
        l = L[N * i:N * (i + 1)]
        if 'S' in l or 'T' in l:
            for j, x in enumerate(l):
                if x == 'T':
                    T.append(i, j)
                elif x == 'X':
                    X.append(i, j)
        dl.append(L[N * i:N * (i + 1)])
    return solution_(T, X, dl)
