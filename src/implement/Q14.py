"""
- n은 1 이상 200 이하인 자연수입니다.
- weak의 길이는 1 이상 15 이하입니다.
    서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
    취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
    weak의 원소는 0 이상 n - 1 이하인 정수입니다.
- dist의 길이는 1 이상 8 이하입니다.
    dist의 원소는 1 이상 100 이하인 자연수입니다.
- 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.

https://programmers.co.kr/learn/courses/30/lessons/60062
"""

from itertools import permutations


def solution(n: int, weak: list, dist: list):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist)
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start+length):
                if position < weak[index]:
                    count +=1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
        answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

    return answer
