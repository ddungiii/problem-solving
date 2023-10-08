"""
https://www.acmicpc.net/problem/17281
"""
from itertools import permutations
from collections import deque


def play_baseball(line_up, index, inning):
    out = 0
    score = 0

    base = deque([0, 0, 0])
    while out < 3:
        player = hits[inning][line_up[index - 1]]

        if player == 0:
            out += 1
        elif player == 1:
            base.appendleft(1)
            score += base.pop()
        elif player == 2:
            base.appendleft(1)
            base.appendleft(0)
            score += base.pop()
            score += base.pop()
        elif player == 3:
            base.appendleft(1)
            base.appendleft(0)
            base.appendleft(0)
            score += base.pop()
            score += base.pop()
            score += base.pop()
        elif player == 4:
            score += sum(base) + 1
            base = deque([0, 0, 0])

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
    answer = 0

    for comb in permutations(range(1, 9), 8):
        line_up = list(comb)[0:3] + [0] + list(comb)[3:8]

        answer = max(answer, get_score(line_up))

    return answer


N = int(input())
hits = [list(map(int, input().split())) for _ in range(N)]

print(solution())
