"""
https://www.acmicpc.net/problem/20058

3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1

3 1
1 1 2 2 1 1 2 2  
1 1 2 2 1 1 2 2
3 3 4 4 3 3 4 4
3 3 4 4 3 3 4 4
1 1 2 2 1 1 2 2  
1 1 2 2 1 1 2 2
3 3 4 4 3 3 4 4
3 3 4 4 3 3 4 4
2
"""


import collections


def print_matrix(matrix):
    for row in matrix:
        print(row)


def rotate(r, c, L):
    """
    그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
    9  1 -> 10 9
    10 2    2  1
    """
    S = 2 ** (L - 1)

    # 제 4 사분면
    temp = []
    for i in range(S):
        temp.append(matrix[r + i][c : c + S])

    # 제 1, 2, 3 사분면 -> 제 2, 3 ,4 사분면
    for i in range(S):
        matrix[r + i][c : c + S] = matrix[r + S + i][c : c + S]
        matrix[r + S + i][c : c + S] = matrix[r + S + i][c + S : c + S + S]
        matrix[r + S + i][c + S : c + S + S] = matrix[r + i][c + S : c + S + S]

    # 제 4 사분면 -> 제 2 사분면
    for i in range(S):
        matrix[r + i][c + S : c + S + S] = temp[i]


def melt():
    """
    이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다
    """
    targets = []

    for r in range(2**N):
        for c in range(2**N):
            if matrix[r][c] == 0:
                continue

            count = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                # 가장자리는 항상 녹음
                if 0 <= nr < 2**N and 0 <= nc < 2 ** N and matrix[nr][nc] > 0:
                    count += 1

            if count < 3:
                targets.append((r, c))

    for r, c in targets:
        matrix[r][c] -= 1

    return len(targets)


def divide(L):
    """
    파이어스톰은 먼저 격자를 2^L x 2^L 크기의 부분 격자로 나눈다
    """
    if L == 0:
        return

    for r in range(0, 2**N, 2**L):
        for c in range(0, 2**N, 2**L):
            rotate(r, c, L)


def find_ices():
    """
    1. 남아있는 얼음 A[r][c]의 합
    """

    return sum([sum(row) for row in matrix])


def bfs(r, c):
    q = collections.deque([(r, c)])
    visited = set([(r, c)])
    size = 0

    while q:
        _r, _c = q.popleft()
        size += 1

        for i in range(4):
            nr, nc = _r + dr[i], _c + dc[i]
            if (
                0 <= nr < 2**N
                and 0 <= nc < 2**N
                and (nr, nc) not in visited
                and matrix[nr][nc] > 0
            ):
                matrix[nr][nc] = -1
                q.append((nr, nc))
                visited.add((nr, nc))

    return size


def find_largest():
    """
    2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.
    """
    largest = 0
    for r in range(2**N):
        for c in range(2**N):
            if matrix[r][c]:
                largest = max(largest, bfs(r, c))

    return largest


dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

N, Q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2**N)]
L_list = list(map(int, input().split()))


for i in range(Q):
    print(f"i: {i}, L: {L_list[i]}")
    if L_list[i] == 0:
        continue
    divide(L_list[i])
    print_matrix(matrix)
    print(melt())

    print_matrix(matrix)
    print()

ices = find_ices()
largest = find_largest()

print(ices)
print(largest)
