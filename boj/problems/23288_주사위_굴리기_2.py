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
    maps = [[-1, 2, -1], [4, 1, 3], [-1, 5, -1], [-1, 6, -1]]

    def __init__(self):
        self.r, self.c = (0, 0)
        self.direction = 0

    def __str__(self):
        return f"({self.r}, {self.c}): {self.maps[3][1]}, direction: {self.direction}"

    def can_move(self) -> bool:
        r, c = self.r + dr[self.direction], self.c + dc[self.direction]

        return 0 <= r < N and 0 <= c < M

    def get_value(self):
        return self.maps[3][1]

    def move(self):
        self.r, self.c = self.r + dr[self.direction], self.c + dc[self.direction]

        if self.direction == 0:
            temp = self.maps[1][2]
            self.maps[1] = [self.maps[3][1]] + self.maps[1][:2]
            self.maps[3][1] = temp
        elif self.direction == 1:
            self.maps[0][1], self.maps[1][1], self.maps[2][1], self.maps[3][1] = (
                self.maps[3][1],
                self.maps[0][1],
                self.maps[1][1],
                self.maps[2][1],
            )
        elif self.direction == 2:
            temp = self.maps[1][0]
            self.maps[1] = self.maps[1][1:] + [self.maps[3][1]]
            self.maps[3][1] = temp
        elif self.direction == 3:
            self.maps[0][1], self.maps[1][1], self.maps[2][1], self.maps[3][1] = (
                self.maps[1][1],
                self.maps[2][1],
                self.maps[3][1],
                self.maps[0][1],
            )

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4


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

dice = Dice()
answer = 0
for _ in range(K):
    move(dice)
    point = get_point(dice.r, dice.c)
    set_direction(dice)
    # print(_, dice, "m_value:", matrix[dice.r][dice.c], ", point: ", point)

    answer += point

print(answer)
