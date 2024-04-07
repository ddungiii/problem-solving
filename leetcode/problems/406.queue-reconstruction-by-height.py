#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#


# @lc code=start
import heapq


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        queue = []
        for h, g in people:
            heapq.heappush(queue, (-h, g))

        result = []
        while queue:
            h, index = heapq.heappop(queue)
            result.insert(index, (-h, index))

        return result


# @lc code=end
