# https://www.acmicpc.net/problem/1715

def solution(N: int, params: list) -> int:
    params.sort()

    sum = params[0] + params[1]

    for i in params[2:]:
        sum += (sum + i)

    return sum


import heapq


def s2(n, data):
    heap = []

    for i in range(n):
        heapq.heappush(heap, data[i])

    result = 0
    while len(heap) != 1:
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        sum_value = one + two
        result += sum_value
        heapq.heappush(heap, sum_value)
    return result

#
# n = int(input())
# heap = []
#
# for i in range(n):
#     data = int(input())
#     heapq.heappush(heap, data)
#
# print(s2(heap))
