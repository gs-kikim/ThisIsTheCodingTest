from bisect import bisect_left, bisect_right


def solution(N: list, x: int) -> int:
    res = N.count(x)
    return res if res > 0 else -1


def bisect_solution(l: list, x: int) -> int:
    left = bisect_left(l, x)
    right = bisect_right(l, x)

    return (right - left) if (right - left) > 0 else -1
