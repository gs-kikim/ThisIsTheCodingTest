def DP_Q31(n: int, m: int, l: list) -> int:
    move = [(-1, 1), (0, 1), (1, 1)]
    res = []

    def cal_index(x, y):
        return ((x - 1) * m) + (y - 1)

    def dp(x, y, v, i):
        if i == m:
            res.append(v)
            print('save = [' + str(x) + ',' + str(y) + ']')
            return

        for mx, my in move:
            _x = (x + mx)
            _y = (y + my)

            if _x >= 1 and _y >= 1 and cal_index(_x, _y) < len(l):
                print('sum = [' + str(_x) + ',' + str(_y) + ']')
                dp(_x, _y, v + l[cal_index(_x, _y)], i+1)

    i = 1
    for value in l[:m]:
        print('sum = [' + str(i) + ',' + str(1) + ']')
        dp(i, 1, value, 1)
        i += 1

    return max(res)
