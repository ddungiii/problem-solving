import collections


def solution(n):
    MAGIC_NUMBER = 1_000_000_007

    dp = collections.defaultdict(int)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3  # 가로2 타일 추가
        for j in range(0, i - 2, 2):
            dp[i] += dp[j] * 2  # 가로4 타일 추가

    return dp[n] % MAGIC_NUMBER
