#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [0, 2]


# @lc code=end
import time

soluion = Solution()
nums_string = input("nums: ")
nums_list = nums_string.split()
nums = [int(n) for n in nums_list]
print(f"nums: {nums}")
target = int(input("target: "))
start = time.time()
print(soluion.twoSum(nums, target))
print(f"time: {time.time() - start:.4f}s ")
