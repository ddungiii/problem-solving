"""
https://www.acmicpc.net/problem/23288

4 5 500
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
"""


import collections


class Dice:
    maps = [[6, 3, 1, 4], [6, 2, 1, 5], [3, 2, 4, 5]]

    def __init__(self):
        self.r, self.c = (0, 0)

        # 가로, 세로 방향의 list 종류
        self.hori = 0
        self.vert = 1

        # 주사위의 다음 방향 0, 1, 2, 3 (동, 남, 서, 북)
        self.dirc = 1

        # 가로, 세로 방향의 index in the list
        self.hori_index = 0
        self.vert_index = 0

        # 가로, 세로 방향의 방향
        self.hori_dirc = 1
        self.vert_dirc = 1

    def __str__(self) -> str:
        return f"r, c: ({self.r}, {self.c}), direction: {self.dirc}, value: {self.maps[self.hori][self.hori_index]}, {self.maps[self.vert][self.vert_index]}"

    def can_move(self) -> bool:
        direction = dr[self.dirc], dc[self.dirc]
        r, c = self.r + direction[0], self.c + direction[1]

        return 0 <= r < N and 0 <= c < M

    def get_value(self):
        return self.maps[self.vert][self.vert_index]

    def move(self):
        """
        dirc: 0, 1, 2, 3 (동, 남, 서, 북)
        """
        direction = dr[self.dirc], dc[self.dirc]
        self.r, self.c = self.r + direction[0], self.c + direction[1]

        if direction[1] != 0:
            """
            Move horizontal
            """
            dirc = direction[1]  # 오른쪽 / 왼쪽

            self.hori_index = (self.hori_index + dirc * self.hori_dirc) % 4
            value = self.maps[self.hori][self.hori_index]

            flip_dirc = False
            self.vert = (self.vert + dirc) % 3
            if self.vert == self.hori:
                self.vert = (self.vert + dirc) % 3
                flip_dirc = True

            self.vert_index = self.maps[self.vert].index(value)
            if flip_dirc:
                self.vert_dirc *= -1

        elif direction[0] != 0:
            """
            Move vertical
            """
            dirc = direction[0]  # 오른쪽 / 왼쪽

            self.vert_index = (self.vert_index + dirc * self.vert_dirc) % 4
            value = self.maps[self.vert][self.vert_index]

            flip_dirc = False
            self.hori = (self.hori + dirc) % 3
            if self.hori == self.vert:
                self.hori = (self.hori + dirc) % 3
                flip_dirc = True

            self.hori_index = self.maps[self.hori].index(value)
            if flip_dirc:
                self.hori_dirc *= -1

    def turn_right(self):
        self.dirc = (self.dirc + 1) % 4

    def turn_left(self):
        self.dirc = (self.dirc - 1) % 4


def move(dice: Dice):
    """
    1.
    주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    """
    if not dice.can_move():
        for _ in range(2):
            dice.turn_right()

    dice.move()


def get_point(r, c):
    """
    2.
    주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    """
    q = collections.deque([(r, c)])
    visited = set([(r, c)])

    while q:
        _r, _c = q.popleft()

        for i in range(4):
            nr = _r + dr[i]
            nc = _c + dc[i]

            if (
                0 <= nr < N
                and 0 <= nc < M
                and (nr, nc) not in visited
                and matrix[r][c] == matrix[nr][nc]
            ):
                q.append((nr, nc))
                visited.add((nr, nc))

    return len(visited) * matrix[r][c]


def set_direction(dice: Dice):
    """
    3.
    주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
        - A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
        - A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
        - A = B인 경우 이동 방향에 변화는 없다.
    """
    A = dice.get_value()
    B = matrix[dice.r][dice.c]

    if A > B:
        dice.turn_right()
    elif A < B:
        dice.turn_left()


dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# dice = Dice()
# answer = 0
# for _ in range(K):
#     move(dice)
#     point = get_point(dice.r, dice.c)
#     set_direction(dice)
#     print(_, dice, "m_value:", matrix[dice.r][dice.c], ", point: ", point)

#     answer += point

# print(answer)

dice = Dice()
print(dice)
for _ in range(3):
    dice.move()
    print(dice)
dice.turn_left()
print("turnleft")
# for _ in range(3):
#     dice.move()
#     print(dice)
# print("turnright")
# dice.turn_right()
for _ in range(4):
    dice.move()
    print(dice)
print("turnleft")
dice.turn_left()
for _ in range(4):
    dice.move()
    print(dice)
