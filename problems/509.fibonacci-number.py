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
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.dp[n]


# @lc code=end
