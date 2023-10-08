"""
https://www.acmicpc.net/problem/17070
"""


import collections
from enum import Enum

Status = Enum("Status", ["RIGHT", "DOWN", "DIAGONAL"])

n = int(input())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))

"""
0: right
1: down
2: diagonal
"""
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, n):
    if not M[0][i]:
        dp[0][0][i] = dp[0][0][i - 1]

for x in range(1, n):
    for y in range(1, n):
        if not M[x][y]:
            # right
            dp[0][x][y] = dp[0][x][y - 1] + dp[2][x][y - 1]
            # down
            dp[1][x][y] = dp[1][x - 1][y] + dp[2][x - 1][y]
            # diagonal
            if not M[x - 1][y] and not M[x][y - 1]:
                dp[2][x][y] = (
                    dp[0][x - 1][y - 1] + dp[1][x - 1][y - 1] + dp[2][x - 1][y - 1]
                )
print(sum([dp[i][n - 1][n - 1] for i in range(3)]))
