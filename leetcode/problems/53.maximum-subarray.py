#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + (nums[i - 1] if nums[i - 1] > 0 else 0)

        return max(nums)


# @lc code=end
