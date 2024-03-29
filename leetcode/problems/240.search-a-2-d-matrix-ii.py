#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        return any(target in row for row in matrix)


# @lc code=end
