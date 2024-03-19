import collections

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dp = collections.defaultdict(int)


def merge_board(board):
    """
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    =>
    000000000
    """
    return "".join(["".join([str(i) for i in row]) for row in board])


def create_new_board(board, loc):
    new_board = [row for row in board]
    new_board[loc[0]][loc[1]] = 0

    return new_board


def is_safe(board, loc):
    return board[loc[0]][loc[1]] == 1


def is_in(board, loc):
    return (
        loc[0] >= 0 and loc[0] < len(board) and loc[1] >= 0 and loc[1] < len(board[0])
    )


def dfs(board, aloc, bloc, turn, count):
    if not is_safe(board, aloc) or not is_safe(board, bloc):
        return count

    if dp[(merge_board(board), aloc, bloc)]:
        return dp[(merge_board(board), aloc, bloc)]

    loc = aloc if turn == 0 else bloc
    new_board = create_new_board(board, loc)

    max_count = 0
    for r, c in dirs:
        if turn == 0:
            new_aloc = aloc[0] + r, aloc[1] + c
            if not is_in(new_board, new_aloc):
                continue
            max_count = max(max_count, dfs(new_board, new_aloc, bloc, 1, count + 1))
        else:
            new_bloc = bloc[0] + r, bloc[1] + c
            if not is_in(new_board, new_bloc):
                continue
            max_count = max(max_count, dfs(new_board, aloc, new_bloc, 0, count + 1))

    dp[(merge_board(board), aloc, bloc)] = max_count
    return dp[(merge_board(board), aloc, bloc)]


def solution(board, aloc, bloc):
    return dfs(board, tuple(aloc), tuple(bloc), 0, 0)

    print(dp)
    answer = -1
    return answer
