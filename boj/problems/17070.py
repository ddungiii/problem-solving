"""
https://www.acmicpc.net/problem/17070
"""


from enum import Enum

Status = Enum("Status", ["RIGHT", "DOWN", "DIAGONAL"])


class Pipe:
    """
    (0,0) (0,1) (0,2)
    (1,0) (1,1) (1,2)
    (2,0) (2,1) (2,2)
    """

    def __init__(self, x=0, y=1, status=Status.RIGHT):
        self.x = x
        self.y = y
        self.status = status

    def get(self):
        return self.x, self.y

    def moves(self):
        moves = []
        if self.status == Status.RIGHT:
            if self.y + 1 < n and not walls[self.x][self.y + 1]:
                moves.append(Pipe(self.x, self.y + 1, Status.RIGHT))
                if (
                    self.x + 1 < n
                    and not walls[self.x + 1][self.y]
                    and not walls[self.x + 1][self.y + 1]
                ):
                    moves.append(Pipe(self.x + 1, self.y + 1, Status.DIAGONAL))

        elif self.status == Status.DOWN:
            if self.x + 1 < n and not walls[self.x + 1][self.y]:
                moves.append(Pipe(self.x + 1, self.y, Status.DOWN))
                if (
                    self.y + 1 < n
                    and not walls[self.x][self.y + 1]
                    and not walls[self.x + 1][self.y + 1]
                ):
                    moves.append(Pipe(self.x + 1, self.y + 1, Status.DIAGONAL))

        elif self.status == Status.DIAGONAL:
            if self.y + 1 < n and not walls[self.x][self.y + 1]:
                moves.append(Pipe(self.x, self.y + 1, Status.RIGHT))
            if self.x + 1 < n and not walls[self.x + 1][self.y]:
                moves.append(Pipe(self.x + 1, self.y, Status.DOWN))
                if (
                    self.y + 1 < n
                    and not walls[self.x][self.y + 1]
                    and not walls[self.x + 1][self.y + 1]
                ):
                    moves.append(Pipe(self.x + 1, self.y + 1, Status.DIAGONAL))

        return moves


n = int(input())
walls = []
for _ in range(n):
    walls.append(list(map(int, input().split())))


def dfs(pipe=Pipe()):
    x, y = pipe.get()
    if (x, y) == (n - 1, n - 1):
        return 1

    count = 0
    moves = pipe.moves()
    for move in moves:
        count += dfs(move)

    return count


print(dfs())
