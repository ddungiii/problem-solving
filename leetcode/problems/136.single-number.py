#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


# @lc code=end
