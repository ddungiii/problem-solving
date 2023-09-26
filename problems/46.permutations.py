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
        return [list(perm) for perm in permutations(nums)]
# @lc code=end
