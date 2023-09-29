#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
# s
from typing import List


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (
                (i < 0 or i > len(grid) - 1)
                or (j < 0 or j > len(grid[0]) - 1)
                or grid[i][j] != "1"
            ):
                return

            grid[i][j] = "0"

            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1

        return num_islands


# @lc code=end
