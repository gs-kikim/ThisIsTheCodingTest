def DP_Q31(n: int, m: int, l: list) -> int:
    move = [(-1, 1), (0, 1), (1, 1)]
    res = []

    def cal_index(x, y):
        return ((x - 1) * m) + (y - 1)

    def dp(x, y, v, i):
        if i == m:
            res.append(v)
            return

        for mx, my in move:
            _x = (x + mx)
            _y = (y + my)

            if _x >= 1 and _y >= 1 and cal_index(_x, _y) < len(l):
                dp(_x, _y, v + l[cal_index(_x, _y)], i + 1)

    for i in range(1, n+1):
        dp(i, 1, l[cal_index(i, 1)], 1)

    return max(res)

# def DP_Q31_2(n: int, m: int, l: list) -> int:
#     dp = []
#     pre = 0
#
#     for i in range(1, m+1):
#         dp.append(l[pre:m*i])
#         pre = m
#
#     for i in range(1, n):
#         for j in range(i + 1, m):
#             dp[i][j] = dp[i][j] + max(dp[i - 1][j], dp[i][j], dp[i+1][j])
#
#     return max(dp[n - 1])
