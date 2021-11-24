# https://programmers.co.kr/learn/courses/30/lessons/42891
def greedy_Q6(food_times, k) -> int:
    index = -1
    n = len(food_times)
    for i in range(0, k):
        index = i % n
        if food_times[index] is 0:
            continue
        food_times[index] = food_times[index]-1

    return -1 if sum(food_times) is 0 else index
