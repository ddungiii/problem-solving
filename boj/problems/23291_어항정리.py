"""
https://www.acmicpc.net/problem/23291

input:
8 7
5 2 3 14 9 2 11 8

output:
1
"""

import collections


N, K = map(int, input().split())
bowls = list(map(int, input().split()))


def print_bowls(bowls):
    """
    for debugging
    """
    print("bowls")
    for i in range(len(bowls) - 1, -1, -1):
        print(bowls[i])


def calc_fish_diff():
    """
    Calculate difference the number of max, min of fishes.
    """
    return max(bowls) - min(bowls)


def add_fish_to_min_bowls():
    """
    Add a fish to bowls has minimum numbers of fishes
    """
    min_fishes = min(bowls)
    for i, bowl in enumerate(bowls):
        if bowl == min_fishes:
            bowls[i] += 1


def pop_bowls(bowl_matrix, width, height):
    """
    Pop the bowls that will be rotated
    """
    bowls = [collections.deque() for _ in range(height)]

    for _ in range(width):
        for h in range(height):
            bowls[h].append(bowl_matrix[h].popleft())

    return bowls


def rotate_bowls(bowl_matrix):
    """
    Rotate matrix in clock direction
    """
    width, height = len(bowl_matrix[0]), len(bowl_matrix)

    bowls = [collections.deque() for _ in range(width)]

    for w in range(width):
        for h in range(height):
            bowls[w].append(bowl_matrix[h].pop())

    return bowls


def stack_bowls(bowl_matrix, width=1, height=1, rotation=1):
    """
    Stack up Bowls for mixing by making matrix
    """
    if width + height > len(bowl_matrix[0]):
        return

    poped_bowls = pop_bowls(bowl_matrix, width, height)
    rotated_bowls = rotate_bowls(poped_bowls)
    for _ in range(rotation - 1):
        rotated_bowls = rotate_bowls(rotated_bowls)

    if len(rotated_bowls) + 1 > len(bowl_matrix):
        bowl_matrix.append(collections.deque())

    for i, row in enumerate(rotated_bowls):
        bowl_matrix[i + 1] = row

    # print_bowls(bowl_matrix)

    stack_bowls(bowl_matrix, len(rotated_bowls[0]), len(rotated_bowls) + 1, rotation)


def mix_bowls(bowl_matrix):
    """
    Find Adjacent bowls that difference is larger than K.
    And flow fishes to smaller bowl.
    """
    W, H = len(bowl_matrix[0]), len(bowl_matrix)

    dr = (1, 0, -1, 0)
    dc = (0, 1, 0, -1)

    mix_dict = collections.defaultdict(int)
    for r, _ in enumerate(bowl_matrix):
        for c, _ in enumerate(bowl_matrix[r]):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if (
                    0 <= nr < H
                    and 0 <= nc < len(bowl_matrix[nr])
                    and ((bowl_matrix[nr][nc] - bowl_matrix[r][c]) // 5) >= 0
                ):
                    diff = bowl_matrix[nr][nc] - bowl_matrix[r][c]
                    mix_dict[(nr, nc)] -= diff // 5
                    mix_dict[(r, c)] += diff // 5

    for point, diff in mix_dict.items():
        r, c = point
        bowl_matrix[r][c] += diff


def flatten_bowls(bowl_matrix: list) -> list:
    new_bowls = []
    if len(bowl_matrix) == 1:
        return list(bowl_matrix[0])

    for _ in range(len(bowl_matrix[1])):
        for j in range(len(bowl_matrix)):
            new_bowls.append(bowl_matrix[j].popleft())

    while new_bowls:
        bowl_matrix[0].appendleft(new_bowls.pop())

    return list(bowl_matrix[0])


def flip_bowls(bowl_matrix, width, height):
    """
    Flip Bowls for mixing by making matrix
    """
    poped_bowls = pop_bowls(bowl_matrix, width, height)
    rotated_bowls = rotate_bowls(poped_bowls)
    rotated_bowls = rotate_bowls(rotated_bowls)

    for _ in range(height):
        bowl_matrix.append(collections.deque())

    for i, row in enumerate(rotated_bowls):
        bowl_matrix[i + height] = row

    # print_bowls(bowl_matrix)


def organize_bowls():
    global bowls
    """
    1. Add a fish for min bowl
    2. stack_bowls
        2-1. pop_bowls
        2-2. rotate_bowls
    3. mix_fishes
    4. flatten_bowls

    5. stack_bowls x 2
    6. flatten_bowls
    """

    # Step 1
    add_fish_to_min_bowls()
    bowl_matrix = [collections.deque(bowls)]
    stack_bowls(bowl_matrix)
    mix_bowls(bowl_matrix)
    bowls = flatten_bowls(bowl_matrix)

    # Step 2
    bowl_matrix = [collections.deque(bowls)]
    flip_bowls(bowl_matrix, int(N / 2), 1)
    flip_bowls(bowl_matrix, int(N / 4), 2)
    mix_bowls(bowl_matrix)
    bowls = flatten_bowls(bowl_matrix)


count = 0
while calc_fish_diff() > K:
    count += 1

    organize_bowls()


print(count)
