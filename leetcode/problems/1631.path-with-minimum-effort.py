#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start

import collections
import heapq
import math


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        W, H = len(heights), len(heights[0])

        efforts = {(r, c): math.inf for c in range(H) for r in range(W)}
        efforts[(0, 0)] = 0

        Q = collections.deque([(0, 0)])

        def inside(r, c):
            return 0 <= r < W and 0 <= c < H

        while Q:
            r, c = Q.popleft()
            curr_height = heights[r][c]
            curr_effort = efforts[(r, c)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if inside(new_r, new_c):
                    new_height = heights[new_r][new_c]
                    new_effort = max(curr_effort, abs(new_height - curr_height))
                    if new_effort < efforts[(new_r, new_c)]:
                        efforts[(new_r, new_c)] = new_effort
                        Q.append((new_r, new_c))

        return efforts[(W - 1, H - 1)]


# @lc code=end
import time
import ast

soluion = Solution()
start = time.time()

heights = ast.literal_eval(input("height: "))
heights = [[int(e) for e in l] for l in heights]

print(soluion.minimumEffortPath(heights))
print(f"time: {time.time() - start:.4f}s ")
