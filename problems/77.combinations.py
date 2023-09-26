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
        nums = list(range(1, n + 1))

        def dfs(parent: List[int], child: List[int] = []):
            if len(child) == k:
                result.append(child)
                return

            for i, element in enumerate(parent):
                new_parent = parent[i + 1 :]
                new_child = child[:]

                new_child.append(element)
                dfs(new_parent, new_child)

        result: List[List[int]] = []
        dfs(nums)

        return result


# @lc code=end
