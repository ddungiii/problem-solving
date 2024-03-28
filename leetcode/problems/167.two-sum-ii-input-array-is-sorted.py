#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
import bisect


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i, number in enumerate(numbers):
            remain = target - number
            j = bisect.bisect_left(numbers, remain, lo=i + 1, hi=len(numbers) - 1)
            if numbers[j] == remain:
                return [i + 1, j + 1]


# @lc code=end
