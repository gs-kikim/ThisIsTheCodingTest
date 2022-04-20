def solution(S: str) -> str:
    sl = []
    num = 0
    for i in S:
        if 'A' <= i <= 'Z':
            sl.append(i)
        else:
            num += int(i)
    sl.sort()
    return "".join(sl) + str(num)
