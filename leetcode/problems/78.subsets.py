#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index: int, subset: List[int] = []):
            result.append(subset)

            for i in range(index, len(nums)):
                new_subset = subset[:]
                new_subset.append(nums[i])
                dfs(i + 1, new_subset)

        result = []
        dfs(0)

        return result


# @lc code=end
