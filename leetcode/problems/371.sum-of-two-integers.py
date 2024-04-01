#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        if a > INT_MAX:
            a = ~(a ^ MASK)

        return a


# @lc code=end
