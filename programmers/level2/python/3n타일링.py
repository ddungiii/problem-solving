# dp[8] = dp[2]*dp[6] + dp[4]*dp[4] + d[6]*dp[2]
# dp[6] = dp[2]*dp[4] + dp[4]*dp[2]

import collections

MAGIC_NUMBER = 1_000_000_007

dp = collections.defaultdict(int)
dp[2] = 2
dp[4] = 11


def dfs(n):
    if dp[n]:
        return dp[n]

    result = 0
    a, b = n - 2, 2
    while a > 0:
        result += dfs(a) * dfs(b)
        a -= 2
        b += 2

    dp[n] = result

    return dp[n]


def solution(n):
    return dfs(n) % MAGIC_NUMBER
