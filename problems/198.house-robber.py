#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    dp = defaultdict(int)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        self.dp[0] = nums[0]
        self.dp[1] = nums[1]

        for i in range(2, len(nums)):
            self.dp[i] = max(self.dp[i - 2] + nums[i], self.dp[i - 1])

        return max(self.dp.values())


# @lc code=end
