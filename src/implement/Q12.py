"""
https://programmers.co.kr/learn/courses/30/lessons/60061

기둥은
 1. 바닥 위에 있거나 ,y==0
 2. 보의 한쪽 끝 부분 위에 있거나,
 3. 또는 다른 기둥 위에 있어야 합니다.
보는
 1. 한쪽 끝 부분이 기둥 위에 있거나,
 2. 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다

 삭제는 기둥과 보를 삭제한 후에 남은 기둥과 보들 또한 위 규칙을 만족해야 함.

 [x,y,a,b] xy 좌표, a(0:기둥, 1:보), b(0:삭제, 1:설치)
 return [[x,y,a]]

"""


def possible(answer: list):
    for frame in answer:
        x, y, stuff = frame[0], frame[1], frame[2]
        if stuff == 0:  # 기둥
            if y == 0 or [x + 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        else:
            if [x - 1, y - 1, 0] in answer or [x, y - 1, 0] in answer or ([x - 1, y, 1] and [x + 1, y, 1]):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = [[]]
    MAP = [[0] * n for _ in range(n)]

    for frame in build_frame:
        x, y, stuff, operate = frame[0], frame[1], frame[2], frame[3]
        # if stuff == 0:  # 기둥
        #     if operate == 1:
        #         if y==0 or on_beam(x,y) or on_column(x,y):
        #             answer.append([x,y,stuff])
        #             MAP[x][y] = stuff
        # else:
        #     if operate == 1:
        #         if on_column(x,y) or on_column(x+1,y) or (on_beam(x,y) and on_beam(x+1,y)):
        #             answer.append([x, y, stuff])
        #             MAP[x][y] = stuff
        elem = [x, y, stuff]
        if operate == 0:  # del
            answer.remove(elem)
            if not possible(answer):
                answer.append(elem)
        else:
            answer.append(elem)
            if not possible(answer):
                answer.remove(elem)

    return sorted(answer)
