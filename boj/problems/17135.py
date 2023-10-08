"""
https://www.acmicpc.net/problem/17135
"""
"""
5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
"""
import collections
from itertools import combinations

dr = (0, -1, 0)
dc = (-1, 0, 1)


def attack(board, archers):
    def bfs(r: int, c: int):
        if board[r][c]:
            enemy_set.add((r, c))
            return

        deque = collections.deque([(r, c, 1)])

        while deque:
            x, y, distance = deque.popleft()

            if distance > D:
                continue

            if board[x][y]:
                enemy_set.add((x, y))
                return

            for i in range(3):
                nx = x + dr[i]
                ny = y + dc[i]
                if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                    continue

                deque.append((nx, ny, distance + 1))

    kill = 0
    for r in range(N - 1, -1, -1):
        enemy_set = set()
        for ancher in archers:
            bfs(r, ancher)

        for x, y in enemy_set:
            board[x][y] = 0
            kill += 1

    return kill


def solution():
    archers_comb = combinations(range(M), 3)

    answer = 0
    for archers in archers_comb:
        new_board = [b[:] for b in board]
        answer = max(answer, attack(new_board, archers))

    return answer


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

print(solution())
