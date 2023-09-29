#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
from collections import defaultdict


# @lc code=start
class Solution:
    dp = defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]


# @lc code=end
