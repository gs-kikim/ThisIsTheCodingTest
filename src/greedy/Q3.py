import itertools

# 메모리 29200, 시간 68
def backjun_1(nums:str):
    l = list(map(int, list(nums)))
    newl = [l[0]]
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            newl.append(l[i])
    return min(newl.count(0), newl.count(1))

# 메모리 : 29200kb , 시간 72ms
# https://www.acmicpc.net/problem/1439
def greedy_Q3(nums: str) -> int:
    zero_cnt = 0
    one_cnt = 0

    if nums.count('0') == 0 or nums.count('1') == 0:
        return 0

    for k, v in itertools.groupby(nums):
        if k == '0':
            zero_cnt += 1
        else:
            one_cnt += 1
    return zero_cnt if zero_cnt < one_cnt else one_cnt

# data =input()
# print(greedy_Q3(data))
