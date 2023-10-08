"""
https://www.acmicpc.net/problem/17281

9
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
"""
from itertools import permutations
from collections import deque
import time


def play_baseball(line_up, index, inning):
    out = 0
    score = 0

    b1, b2, b3 = 0, 0, 0
    while out < 3:
        player = hits[inning][line_up[index - 1]]

        if player == 0:
            out += 1
        elif player == 1:
            score += b3
            b1, b2, b3 = 1, b1, b2
        elif player == 2:
            score += b2 + b3
            b1, b2, b3 = 0, 1, b1
        elif player == 3:
            score += b1 + b2 + b3
            b1, b2, b3 = 0, 0, 1
        elif player == 4:
            score += 1 + b1 + b2 + b3
            b1, b2, b3 = 0, 0, 0

        index += 1
        index %= 9

    return (score, index)


def get_score(line_up):
    score = 0

    index = 1
    for inning in range(N):
        _score, index = play_baseball(line_up, index, inning)
        score += _score

    return score


def solution():
    start = time.time()

    answer = 0

    for comb in permutations(range(1, 9), 8):
        line_up = list(comb)[0:3] + [0] + list(comb)[3:9]

        answer = max(answer, get_score(line_up))

    print(f"time: {time.time() - start:.4f}s")

    return answer


N = int(input())
hits = [list(map(int, input().split())) for _ in range(N)]

print(solution())
