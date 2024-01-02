"""
[[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

[[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]

[[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]

[[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70], [40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
"""

import time

import collections
import itertools


def solution(dice):
    dp = collections.defaultdict(int)

    combinations = list(itertools.combinations(range(len(dice)), int(len(dice) / 2)))
    other_combinations = []
    for comb in combinations:
        other_comb = []
        for i in range(len(dice)):
            if i not in comb:
                other_comb.append(i)
        other_combinations.append(tuple(other_comb))

    scores = []
    for A, B in zip(combinations, other_combinations):
        if dp[(A, B)]:
            scores.append(dp[(A, B)])
            continue

        win = 0
        lose = 0

        start_product = time.time()
        product_A = collections.Counter(
            [sum(p) for p in itertools.product(*[dice[_a] for _a in A])]
        ).items()

        product_B = collections.Counter(
            [sum(p) for p in itertools.product(*[dice[_b] for _b in B])]
        ).items()

        print("product", time.time() - start_product)

        start_loop = time.time()
        for sum_a, count_a in product_A:
            for sum_b, count_b in product_B:
                count = count_a * count_b
                if sum_a > sum_b:
                    win += count
                elif sum_a < sum_b:
                    lose += count
        print("loop", time.time() - start_loop)

        scores.append(win)

        dp[(A, B)] = win
        dp[(B, A)] = lose

    index = scores.index(max(scores))
    return [c + 1 for c in combinations[index]]


dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
dice = [
    [40, 41, 42, 43, 44, 45],
    [43, 43, 42, 42, 41, 41],
    [1, 1, 80, 80, 80, 80],
    [70, 70, 1, 1, 70, 70],
]
dice = [
    [40, 41, 42, 43, 44, 45],
    [43, 43, 42, 42, 41, 41],
    [1, 63, 80, 80, 80, 80],
    [68, 33, 1, 1, 70, 70],
    [40, 41, 42, 43, 44, 46],
    [1, 12, 3, 4, 5, 6],
    [1, 1, 80, 80, 80, 80],
    [46, 3, 3, 3, 4, 4],
]
dice = [
    [43, 41, 42, 43, 44, 45],
    [40, 41, 42, 43, 44, 45],
    [43, 43, 42, 42, 41, 41],
    [1, 63, 80, 80, 80, 80],
    [68, 33, 1, 1, 70, 70],
    [40, 41, 42, 43, 44, 46],
    [1, 12, 3, 4, 5, 6],
    [1, 1, 80, 80, 80, 80],
    [46, 3, 3, 3, 4, 4],
    [70, 70, 1, 1, 70, 73],
]


start = time.time()
print(solution(dice))
print(time.time() - start)
