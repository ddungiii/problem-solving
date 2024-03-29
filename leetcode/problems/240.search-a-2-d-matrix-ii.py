#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])

        for r in range(N):
            for c in range(M):
                if matrix[r][c] == target:
                    return True

        return False


# @lc code=end
