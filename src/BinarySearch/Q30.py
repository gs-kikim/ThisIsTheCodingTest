def solution(words, queries):
    answer = []

    def binary_search(w, q, s, e) -> bool:
        if s >= e:
            return True
        if (w[s] == q[s] or q[s] == '?') and (w[e] == q[e] or q[e] == '?'):
            m = int((s + e) / 2)
            if w[m] == q[m] or q[m] == '?':
                return (binary_search(w, q, s, m - 1) & binary_search(w, q, m + 1, e))

        return False

    for q in queries:
        res = 0
        for w in words:
            if len(w) == len(q):
                res += 1 if binary_search(w, q, 0, len(w)-1) else 0
        answer.append(res)

    return answer
