YOU = 1
ME = 2


def print_list(board):
    for row in board:
        print(row)
    print()


def count_alive(board):
    cnt = 0
    for row in board:
        cnt += sum(1 for r in row if r > 0)
    return cnt


def solution(board, skill):
    print_list(board)
    for type, r1, c1, r2, c2, degree in skill:
        degree = degree if type == ME else -degree
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += degree
    print_list(board)

    return count_alive(board)


print(
    solution(
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [
            [1, 0, 0, 3, 4, 4],
            [1, 2, 0, 2, 3, 2],
            [2, 1, 0, 3, 1, 2],
            [1, 0, 1, 3, 3, 1],
        ],
    )
)

print(
    solution(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
    )
)
