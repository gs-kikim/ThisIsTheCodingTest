"""
https://programmers.co.kr/learn/courses/30/lessons/60058
균형 --> 올바른으로 변경하는 과정
"""


def returnUV(p) -> list:
    stack = [p[0]]
    i = 1
    while len(stack) != 0:
        if stack.pop() == p[i]:
            stack.append(p[i])
            stack.append(p[i])
        i += 1

    return p[:i], p[i:]


def checkParenthesis(p) -> bool:
    stack = []
    for x in p:
        if len(stack) == 0:
            if x == '(':
                stack.append(x)
            else:
                return False
        elif stack.pop() == x:
            stack.append(x)
            stack.append(x)
    return len(stack) == 0


def changeParenthesis(p) -> str:
    tmp = ''
    for x in p:
        if x == ')':
            tmp += '('
        else:
            tmp += ')'
    return tmp


def solution(p):
    res = ""
    if len(p) == 0 or checkParenthesis(p):
        return p
    u, v = returnUV(p)

    if checkParenthesis(u):
        res = u + solution(v)
    else:
        u = changeParenthesis(u[1:len(u) - 1])
        res = '(' + solution(v) + ')' + u

    return res
