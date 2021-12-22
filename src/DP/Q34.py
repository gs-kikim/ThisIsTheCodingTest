def DP_Q34(x: int, arr: list) -> int:
    dp = [1]*x
    arr.reverse()

    for i in range(1, x):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return (x - max(dp))

# n = int(input())
# t = []
# p = []
#
# for _ in range(n):
#     x, y = map(int, input().split())
#     t.append(x)
#     p.append(y)
#
# DP_Q34(n, t, p)
