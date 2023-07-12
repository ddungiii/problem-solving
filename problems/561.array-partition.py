#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#


# @lc code=start
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        filtered = [n for i, n in enumerate(nums) if i % 2 == 0]

        return sum(filtered)


# @lc code=end

import time

solution = Solution()
input_string = input("nums: ")
input_list = input_string.split()
input = [int(str) for str in input_list]

start = time.time()
print(solution.arrayPairSum(input))
print(f"time: {time.time() - start:.4f}s")
