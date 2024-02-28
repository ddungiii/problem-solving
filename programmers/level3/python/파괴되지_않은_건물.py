YOU = 1
ME = 2


def print_list(board):
    for row in board:
        print(row)
    print()


def get_prefix_sum(skill, w, h):
    prefix_sum = [[0 for _ in range(h + 1)] for _ in range(w + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        degree = degree if type == ME else -degree
        prefix_sum[r1][c1] += degree
        prefix_sum[r2 + 1][c1] += -degree
        prefix_sum[r1][c2 + 1] += -degree
        prefix_sum[r2 + 1][c2 + 1] += degree

    # Sum prefix
    for r in range(w + 1):
        prefix = 0
        for c in range(h + 1):
            prefix_sum[r][c] += prefix
            prefix = prefix_sum[r][c]

    for c in range(h + 1):
        prefix = 0
        for r in range(w + 1):
            prefix_sum[r][c] += prefix
            prefix = prefix_sum[r][c]

    return prefix_sum


def count_alive(board):
    cnt = 0
    for row in board:
        cnt += sum(1 for r in row if r > 0)
    return cnt


def solution(board, skill):
    prefix_sum = get_prefix_sum(skill, len(board), len(board[0]))
    # Combine prefix_sum
    for r in range(len(board)):
        board[r] = [x + y for x, y in zip(board[r], prefix_sum[r][:-1])]

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
