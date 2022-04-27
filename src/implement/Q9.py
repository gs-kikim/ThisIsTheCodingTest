"""
https://programmers.co.kr/learn/courses/30/lessons/60057
"""
def solution(s):
    chunks = len(s)
    min_num = chunks

    for chunk_size in range(1, chunks//2+1):
        l = [s[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
        l.append("#")
        w = l[0]
        res = ""
        cnt = 1
        for word in l[1:]:
            if w != word:
                if cnt >= 2:
                    res += w + str(cnt)
                else:
                    res += w
                w = word
                cnt = 1
            else:
                cnt += 1
        min_num = min(min_num, len(res))
    return min_num
