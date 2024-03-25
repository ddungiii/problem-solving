#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start


import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        index = bisect.bisect_left(nums, target, hi=len(nums) - 1)

        return index if nums[index] == target else -1


# @lc code=end
