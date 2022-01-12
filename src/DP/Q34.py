# LIS 가장 긴 증가하는 부분 수열
def DP_Q34(x: int, arr: list) -> int:
    dp = [1]*x
    arr.reverse()

    for i in range(1, x):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return (x - max(dp))

# n = int(input())
# l = map(int, input().split())
#
# print(DP_Q34(n, l))
