"""
https://www.acmicpc.net/problem/18406
"""


def solution(N: int) -> str:
    S = [int(x) for x in str(N)]
    l = len(S) // 2
    return "LUCKY" if sum(S[:l]) == sum(S[l:]) else "READY"

# n = input()
# print(solution(n))
