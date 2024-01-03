#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start

import collections
import heapq
import math
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dr = (1, 0, -1, 0)
        dc = (0, 1, 0, -1)
        dst = (len(heights)-1, len(heights)-1)

        Q = [(0, (0,0))]
        min_effort = math.inf
        visited = set((0, 0))

        while Q:
            effort, (x, y)= heapq.heappop(Q)
            if (x, y) == dst:
                return effort

            min_effort = min(min_effort, effort)
            
            for r in dr:
                for c in dc:
                    new_r, new_c = x+r, y+c
                    if (new_r, new_c) not in visited:
                        if (new_r >= 0 and new_r < len(heights)) and (new_c >= 0 and new_c < len(heights)):
                            new_effort = abs(heights[new_r][new_c] - heights[x][y])
                            heapq.heappush(Q, (new_effort, (new_r, new_c)))
                            visited.add((new_r, new_c))
# @lc code=end
import time
import ast
soluion = Solution()
start = time.time()

heights = ast.literal_eval(input("height: "))
heights = [[int(e) for e in l] for l in heights]

print(soluion.minimumEffortPath(heights))
print(f'time: {time.time() - start:.4f}s ')

