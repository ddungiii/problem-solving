#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#


# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


# @lc code=end
