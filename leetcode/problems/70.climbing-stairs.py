#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
import collections


# @lc code=start
class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        self.dp[1] = 1
        self.dp[2] = 2

        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]


# @lc code=end
