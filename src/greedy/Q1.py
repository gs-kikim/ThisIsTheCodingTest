def greedy_Q1(n: int, adventurers: list) -> int:
    if n is 0:
        return 0
    res = 0
    adventurers.sort()
    max = adventurers[0]
    cnt = 0

    for i in range(0, n):
        adventurer = adventurers[i]
        cnt += 1
        if cnt >= (adventurer if adventurer > max else max):
            cnt = 0
            res += 1

    return res
