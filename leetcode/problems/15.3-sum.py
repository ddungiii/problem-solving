#
# @lc app=leetcode id=15 lang=python3

#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            # for removing duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # for removing duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1

        return results


# @lc code=end
import time

soluion = Solution()
input_string = input("nums: ")
input_list = input_string.split()
input = [int(str) for str in input_list]

start = time.time()
print(soluion.threeSum(input))
print(f"time: {time.time() - start:.4f}s ")
