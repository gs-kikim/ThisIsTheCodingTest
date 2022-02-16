"""
https://www.acmicpc.net/problem/14888
N개의 수열 A
+,-,*,/
음수면 양수로 바꾼뒤 몫을 음수로 바꿈
"""


def sum(a, b): return a + b


def mul(a, b): return a * b


def minus(a, b): return a - b


def div(a, b): return int(a / b)


def cul(i: int, a, b):
    if i == 0:
        return sum(a, b)
    elif i == 1:
        return minus(a, b)
    elif i == 2:
        return mul(a, b)
    else:
        return div(a, b)


def solution(A: int, l: list):
    q = []
    for i, x in enumerate(l):
        if x > 0:
            q.extend([i * x])
    res = []
    max_val = 0
    A.reverse

    def dfs(i, A, max_val):
        if len(q) == i:
            return A[i]
        for j in q[i:]:
            b = dfs(i + 1, A, max_val)
            max_val = max(max_val, cul(j, A[i], b))

        return max_val

    def dfs_(i, A, max_val):
        if len(q) == i:
            return A[i]
        for j in q[i:]:
            b = dfs(i + 1, A, max_val)
            max_val = min(max_val, cul(j, A[i], b))

        return max_val

    max_val = dfs(0, A[::-1], max_val)
    max_val = dfs_(0, A[::-1], max_val)

    return max_val, max_val
