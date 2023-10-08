"""
https://www.acmicpc.net/problem/17406

5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
"""
from itertools import permutations

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


def get_value(mat):
    value = float("inf")

    for r in mat:
        value = min(value, sum(r))

    return value


def rotate(new_matrix, rotation):
    r, c, s = rotation
    r -= 1
    c -= 1
    if s == 0:
        return

    temp = new_matrix[r - s][c - s]
    for d in range(4):
        nc = dc[d]
        nr = dr[d]

        if d == 0:
            start = (r - s, c - s)
        elif d == 1:
            start = (r - s, c + s)
        elif d == 2:
            start = (r + s, c + s)
        else:
            start = (r + s, c - s)

        for _ in range(s * 2):
            next = start[0] + nr, start[1] + nc
            new_matrix[next[0]][next[1]], temp = (
                temp,
                new_matrix[next[0]][next[1]],
            )
            start = next

    rotate(new_matrix, (r + 1, c + 1, s - 1))


def solution():
    answer = float("inf")
    for rotations_perm in permutations(rotations):
        new_matrix = [mat[:] for mat in matrix]
        for rotation in rotations_perm:
            rotate(new_matrix, rotation)
        answer = min(answer, get_value(new_matrix))

    return answer


N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

rotations = []
for _ in range(K):
    rotations.append(list(map(int, input().split())))

print(solution())
