#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
import enum


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        element = 1

        # product left except self
        for num in nums:
            result.append(element)
            element *= num

        element = 1
        # product left except self
        for i, num in enumerate(nums):
            result[len(nums) - 1 - i] *= element
            element *= nums[len(nums) - 1 - i]

        return result


# @lc code=end
import time

soluion = Solution()
start = time.time()
input_string = input("input: ")
input_list = input_string.split()
input = [int(str) for str in input_list]
print(soluion.productExceptSelf(input))
print(f"time: {time.time() - start:.4f}s ")
