#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            num_dict[n] = i

        for i, n in enumerate(nums):
            complement = target - n

            if complement in num_dict and num_dict[complement] != i:
                return [i, num_dict[complement]]


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
