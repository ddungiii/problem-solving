#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List
from itertools import combinations


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(comb) for comb in combinations(range(1, n + 1), k)]


# @lc code=end
