#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y

        return x


# @lc code=end
