# https://www.acmicpc.net/problem/14501
def DP_Q33(n: int, t: list, p: list) -> int:
    dp = [0] * (n + 1)
    max_value = 0

    for i in range(n - 1, -1, -1):
        time = t[i] + i
        pay = p[i]
        if time <= n:
            dp[i] = max(pay + dp[time], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value

    return max_value


# n = int(input())
# t = []
# p = []
#
# for _ in range(n):
#     x, y = map(int, input().split())
#     t.append(x)
#     p.append(y)
#
# print(DP_Q33(n, t, p))
