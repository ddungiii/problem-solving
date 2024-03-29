#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#


# @lc code=start
import bisect


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_search(l):
            i = bisect.bisect_left(l, target, hi=M - 1)
            return l[i] == target

        N, M = len(matrix), len(matrix[0])

        for r in range(N):
            if binary_search(matrix[r]):
                return True

        return False


# @lc code=end
