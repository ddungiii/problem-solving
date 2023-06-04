#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            complement = target - n

            rest = nums[i + 1 :]
            if complement in rest:
                return [i, rest.index(complement) + i + 1]


# @lc code=end
import time

soluion = Solution()
nums_string = input("nums: ")
nums_list = nums_string.split()
nums = [int(n) for n in nums_list]
target = int(input("target: "))
start = time.time()
print(soluion.twoSum(nums, target))
print(f"time: {time.time() - start:.4f}s ")
