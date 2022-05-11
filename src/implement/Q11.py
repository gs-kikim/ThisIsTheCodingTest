X = [0, 1, 0, -1]
Y = [1, 0, -1, 0]


def turn(direction, c):
    return (direction - 1) % 4 if c == "L" else (direction + 1) % 4


def simulate(data, n, info, l):
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + X[direction]
        ny = y + Y[direction]

        if (1 <= nx <= n) and (1 <= ny <= n) and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0) # 사과를 안먹었기에 원복
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time


def solution(n, k, MAP, l, curve):
    data = [[0] * (n + 1) for _ in range(n + 1)]  # 보드
    info = []

    for i in range(k):  # 사과의 개수, 사과 1
        data[MAP[i][0]][MAP[i][1]] = 1

    for i in range(l):  # 뱀의 방향 변환
        x, c = curve[i]
        info.append((int(x), c))

    return simulate(data, n, info, l)
