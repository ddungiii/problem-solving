#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
import enum
from functools import reduce
import sys


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        min_product, max_product, result = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_product, max_product = max_product, min_product

            min_product = min(min_product * nums[i], nums[i])
            max_product = max(max_product * nums[i], nums[i])

            result = max(max_product, result)

        return result


# @lc code=end
import time

soluion = Solution()
start = time.time()
input_string = input("_: ")
input_list = input_string.split()
input = [int(str) for str in input_list]
print(soluion.maxProduct(input))
print(f"time: {time.time() - start:.4f}s ")
