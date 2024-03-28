#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(numbers)):
            number = numbers[i]
            remain = target - number
            if remain not in d:
                d[number] = i
            else:
                # 1-indexing
                return [d[remain] + 1, i + 1]


# @lc code=end
