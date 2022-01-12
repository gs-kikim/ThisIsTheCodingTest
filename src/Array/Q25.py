"""
1<=N<=500
1<=states<=200,000
---> 자연수
내림차순sort 필수
no user --> 0

스테이지 도달 노클 플레이어 수/도달 플레이어 수
"""
# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter


def solution(N, stages):
    all = len(stages)
    dic = {}

    count = Counter(stages)

    for i in range(1, N + 1, 1):
        no_clear = count.get(i)
        if no_clear:
            value = no_clear / all
            dic.update({i: value})
            all -= no_clear
        else:  # None
            dic.update({i: 0})
    return sorted(dic, key=dic.get, reverse=True)
