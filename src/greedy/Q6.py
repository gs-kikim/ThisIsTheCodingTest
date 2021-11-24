# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def greedy_Q6(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for x, y in enumerate(food_times):
        heapq.heappush(q, (y, x + 1))

    food_count = len(food_times)
    prev = 0
    while True:
        num, idx = heapq.heappop(q)
        if (num - prev) * food_count <= k:
            k -= ((num - prev) * food_count)
            food_count -= 1
            prev = num
        else:
            heapq.heappush(q, (num, idx))
            break
    q = sorted(q, key=lambda x: x[1])
    return q[k % food_count][1]
