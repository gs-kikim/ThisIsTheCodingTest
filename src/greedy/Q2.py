def greedy_Q2(nums: str) -> int:
    res = int(nums[0])

    for i in range(1, len(nums)):
        num = int(nums[i])
        if res <= 1 or num <= 1:
            res += num
        else:
            res *= num
    return res

