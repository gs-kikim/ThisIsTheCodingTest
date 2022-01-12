# https://www.acmicpc.net/problem/18310

def array_Q24(N: int, antenna: list) -> int:
    antenna.sort()
    return antenna[int((N-1)/2)]


# n=int(input())
# data = list(map(int, input().split()))
#
# print(array_Q24(n, data))
