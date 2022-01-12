# https://www.acmicpc.net/problem/10825
"""
1<=N<=100,000
1. 국어점수 내림차순 1
2. 영어 오름차순 2
3. 수학 내림 3
4. 이름 사전순 내림차순이라면?
"""
def array_Q23(N: int, students: list):
    l = []
    for s in students:
        sl = s.split(" ")
        l.append([sl[0], int(sl[1]), int(sl[2]), int(sl[3])])

    l.sort(key=lambda x: (x[1], -x[2], x[3], x[0]), reverse=True)

    return [r[0] for r in l]

# n = int(input())
# students = []
#
# for _ in range(n):
#     students.append(input())
#
# for student in array_Q23(n, students):
#     print(student)