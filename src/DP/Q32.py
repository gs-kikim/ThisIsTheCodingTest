def DP_Q32(n, l) -> int:
    dp = []
    pre = 0

    for i in range(1, n + 1):
        dp.append(l[pre:pre + i])
        pre = i

    for i in range(1, n):
        for j in range(i + 1):
            up_left = 0 if j == 0 else dp[i - 1][j - 1]
            up = 0 if j == i else dp[i - 1][j]
            dp[i][j] = dp[i][j] + max(up_left, up)

    return max(dp[n - 1])
