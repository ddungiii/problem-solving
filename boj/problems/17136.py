"""
https://www.acmicpc.net/problem/17136
"""
from collections import deque

paper_counts = [5, 5, 5, 5, 5]
dr = (1, 0, 1)
dc = (0, 1, 1)

flag = True


def bfs(r, c):
    global flag
    matrix[r][c] = 0

    depth = 1
    grow = True
    while grow:
        points = []
        for i in range(1, depth + 1):
            for j in range(3):
                nr = r + dr[j] * i
                nc = c + dc[j] * i
                if (
                    not matrix[nr][c + i]
                    or not matrix[r + i][nc]
                    or nr > N - 1
                    or nc > N - 1
                ):
                    grow = False
                    break
                else:
                    points.append((nr, c + i))
                    points.append((r + i, nc))

        if grow:
            for _r, _c in points:
                matrix[_r][_c] = 0

            if paper_counts[depth]:
                depth += 1
            else:
                grow = False
        # else:
        #     depth -= 1

    paper_counts[depth - 1] -= 1
    if paper_counts[depth - 1] < 0:
        flag = False


def solution():
    for r in range(N):
        for c in range(N):
            if not flag:
                return -1

            if matrix[r][c]:
                bfs(r, c)

    return 25 - sum(paper_counts) if flag else -1


matrix = []
line = list(map(int, input().split()))
matrix.append(line)
N = len(line)

for _ in range(N - 1):
    matrix.append(list(map(int, input().split())))

print(solution())
