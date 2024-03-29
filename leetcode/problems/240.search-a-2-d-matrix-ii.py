#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])

        r, c = 0, M - 1

        while r < N and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True

        return False


# @lc code=end
