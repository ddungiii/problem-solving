#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List
from collections import OrderedDict


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = OrderedDict()  

        if len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp.popitem()[1]


# @lc code=end
