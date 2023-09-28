#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
import enum
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, combs=[]):
            if sum(combs) == target:
                result.append(combs)
                return
            elif sum(combs) > target:
                return
            
            for i in range(index, len(candidates)):
                new_comb = combs[:]
                new_comb.append(candidates[i])
                dfs(i, new_comb)

        result = []
        dfs(0)

        return result

        
# @lc code=end

