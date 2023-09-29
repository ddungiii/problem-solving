#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from itertools import permutations
from typing import List


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(parents: List[int], childs: List[int] = []):
            if len(parents) == 0:
                result.append(childs)

            for i in range(len(parents)):
                new_parents = parents[:]
                new_childs = childs[:]

                poped = new_parents.pop(i)
                new_childs.append(poped)
                dfs(new_parents, new_childs)

        result = []
        dfs(nums)

        return result


# @lc code=end
