def DP_Q31(n: int, m: int, l: list) -> int:
    move = [(-1, 1), (0, 1), (1, 1)]
    res = []
    stack = []

    def cal_index(x, y):
        return ((x - 1) * m) + (y - 1)

    def dp(x, y, v, i):
        print(v)
        if i == m:
            res.append(v)
            print(stack.__str__())
            return

        for mx, my in move:
            _x = (x + mx)
            _y = (y + my)

            if _x >= 1 and _y >= 1 and cal_index(_x, _y) < len(l):
                stack.append((_x, _y));
                dp(_x, _y, v + l[cal_index(_x, _y)], i + 1)
                stack.pop()

    for i in range(1, n+1):
        stack.append((i, 1));
        dp(i, 1, l[cal_index(i, 1)], 1)
        stack.pop()

    print(res.__str__())
    return max(res)
