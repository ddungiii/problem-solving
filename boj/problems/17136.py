"""
https://www.acmicpc.net/problem/17136
"""

papers = [0, 5, 5, 5, 5, 5]


def get_largest_paper_size(r, c):
    size = 0

    size_up = True
    while size_up and size < 5:
        new_size = size + 1
        for i in range(new_size):
            for j in range(new_size):
                if r + i >= N or c + j >= N or matrix[r + i][c + j] == "0":
                    size_up = False

        if size_up:
            size = new_size

    return size


def fill(r, c, size, char):
    for i in range(size):
        for j in range(size):
            matrix[r + i][c + j] = char


def dfs(index, cnt):
    global answer

    if index == len(filled):
        answer = min(answer, cnt)
        return

    if cnt >= answer:
        return

    r, c = filled[index]
    if matrix[r][c] == "0":
        dfs(index + 1, cnt)
        return

    largest_size = get_largest_paper_size(r, c)

    for s in range(largest_size, 0, -1):
        if papers[s] > 0:
            papers[s] -= 1
            fill(r, c, s, "0")
            dfs(index + 1, cnt + 1)
            fill(r, c, s, "1")
            papers[s] += 1


def solution():
    global answer
    dfs(0, 0)

    if answer == 26:
        answer = -1

    return answer


N = 10
matrix = [input().split() for _ in range(N)]
filled = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == "1":
            filled.append((i, j))

answer = 26
print(solution())
