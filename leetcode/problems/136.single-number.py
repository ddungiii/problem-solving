#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#


# @lc code=start
from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = Counter(nums)
        for key in counter:
            if counter[key] == 1:
                return key


# @lc code=end
