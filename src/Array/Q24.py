# https://www.acmicpc.net/problem/18310

def array_Q24(N: int, antenna: list) -> int:
    antenna.sort()
    if N == 1:
        return antenna[0]
    half = int((N - 1) / 2)
    if (N % 2) == 1:
        return antenna[half]
    else:
        al = antenna[:half]
        a = abs(sum(al) - antenna[half] * len(al)) + (sum(antenna[half+1:]) - (antenna[half] * (len(antenna[half+1:]))))
        h2 = half+1
        al = antenna[:h2]
        ap1 = abs(sum(al) - antenna[h2] * len(al)) + (sum(antenna[h2+1:]) - (antenna[h2] * (len(antenna[h2+1:]))))

        return antenna[half] if a <= ap1 else antenna[half + 1]

n=int(input())
data = list(map(int, input().split()))

print(array_Q24(n, data))
