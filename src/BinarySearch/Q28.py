def solution(N: int, l: list) -> int:
    def binary_search(l, s, e):
        if s > e:
            return None
        m = int((s + e) / 2)
        if l[m] == m:
            return m
        elif l[m] > m:
            return binary_search(l, s, m - 1)
        else:
            return binary_search(l, m + 1, e)

    res = binary_search(l, 0, N - 1)
    return -1 if res is None else res
