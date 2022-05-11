from itertools import combinations


def solution(n, m, datas):
    chicken, house = [], []
    for r in range(n):
        data = datas[r]
        for c in range(n):
            if data[c] == 1:
                house.append((r, c))
            elif data[c] == 2:
                chicken.append((r, c))

    candidates = list(combinations(chicken, m))
    result = 1e9
    for candidate in candidates:
        result = min(result, get_sum(candidate, house))

    return result


def get_sum(candidate, house):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result
