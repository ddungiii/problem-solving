"""
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE
5656. [모의 SW 역량테스트] 벽돌 깨기


2
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
2 9 10
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
1 1 0 0 1 0 0 0 0
1 1 0 1 1 1 0 1 0
1 1 0 1 1 1 0 1 0
1 1 1 1 1 1 1 1 0
1 1 3 1 6 1 1 1 1
1 1 1 1 1 1 1 1 1
"""


import collections
from re import X

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


def explod():


def bfs(point):
    deque = collections.deque([point])

    while deque:
        r, c, power = deque.popleft()

        targets = []
        for i in range(4):
            nr = r + dr[i] * (power-1)
            nc = c + dc[i] * (power-1)
            if 0 <= nr < H and 0 <= nc < W and matrix[nr][nc] > 0:
                deque.append((nr, nc, matrix[nr][nc]))

        explode()
        fall_down()

    pass


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    # ///////////////////////////////////////////////////////////////////////////////////
    balls = [i for i in range(W)]

    answer = float("inf")
    for ball in balls:
        for r in range(H):
            if matrix[r][ball] > 0:
                answer = min(answer, bfs((r, ball, matrix[r][ball])))

    # ///////////////////////////////////////////////////////////////////////////////////
    print(f"#{test_case} {answer}")
