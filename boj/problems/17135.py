"""
https://www.acmicpc.net/problem/17135
"""
"""
5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
"""

from itertools import combinations

n, m, d = map(int, input().split())

M = [list(map(int, input().split())) for _ in range(n)]
defensers_comb = combinations(range(m), 3)


def kill(new_M, defenser):
    for i in range(d - 1, 0, -1):
        for j in range(defenser - i, defenser + i + 1):
            if new_M[-1 - i][j]:
                new_M[-1 - i][j] = 0
                return 1

    return 0


count = 0
for defensers in defensers_comb:
    new_M = M[:]
    _count = 0
    while new_M:
        for defenser in defensers:
            _count += kill(new_M, defenser)
        new_M.pop()

    count += _count

print(count)
