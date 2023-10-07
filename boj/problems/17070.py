"""
https://www.acmicpc.net/problem/17070
"""


from enum import Enum

Status = Enum("Status", ["RIGHT", "DOWN", "DIAGONAL"])

n = int(input())
walls = []
for _ in range(n):
    walls.append(list(map(int, input().split())))


def get_moves(x, y, status):
    moves = []
    if status == Status.RIGHT:
        if y + 1 < n and not walls[x][y + 1]:
            moves.append((x, y + 1, Status.RIGHT))
            if x + 1 < n and not walls[x + 1][y] and not walls[x + 1][y + 1]:
                moves.append((x + 1, y + 1, Status.DIAGONAL))

    elif status == Status.DOWN:
        if x + 1 < n and not walls[x + 1][y]:
            moves.append((x + 1, y, Status.DOWN))
            if y + 1 < n and not walls[x][y + 1] and not walls[x + 1][y + 1]:
                moves.append((x + 1, y + 1, Status.DIAGONAL))

    else:
        if y + 1 < n and not walls[x][y + 1]:
            moves.append((x, y + 1, Status.RIGHT))
        if x + 1 < n and not walls[x + 1][y]:
            moves.append((x + 1, y, Status.DOWN))
            if y + 1 < n and not walls[x][y + 1] and not walls[x + 1][y + 1]:
                moves.append((x + 1, y + 1, Status.DIAGONAL))

    return moves


def dfs(x, y, status):
    if (x, y) == (n - 1, n - 1):
        return 1

    count = 0
    moves = get_moves(x, y, status)
    if not len(moves):
        return count

    for new_x, new_y, new_status in moves:
        count += dfs(new_x, new_y, new_status)

    return count


print(dfs(0, 1, Status.RIGHT))
