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
        max = reduce(lambda a, c: a * c, nums, 1)

        left, right = 0, len(nums) - 1

        while left < right and right >= 0 and left <= len(nums) - 1:
            candidates = []
            # 0. l
            candidates.append(max / nums[left] if nums[left] != 0 else -sys.maxsize)

            # 1. r
            candidates.append(max / nums[right] if nums[right] != 0 else -sys.maxsize)

            # 2. l, r
            candidates.append(
                max / (nums[left] * nums[right])
                if nums[left] != 0 and nums[right] != 0 and left + 1 < right
                else -sys.maxsize
            )

            # 3. l, l+1
            candidates.append(
                max / (nums[left] * nums[left + 1])
                if nums[left] != 0 and nums[left + 1] != 0 and left + 1 < right
                else -sys.maxsize
            )

            # 4. r, r-1
            candidates.append(
                max / (nums[right] * nums[right - 1])
                if nums[right] != 0 and nums[right - 1] != 0 and left + 1 < right
                else -sys.maxsize
            )

            index = -1
            for i, candidate in enumerate(candidates):
                if candidate > max:
                    max = candidate
                    index = i

            if index == 0:
                left += 1
            elif index == 1:
                right -= 1
            elif index == 2:
                left += 1
                right -= 1
            elif index == 3:
                left += 2
            elif index == 4:
                right -= 2
            else:
                left += 2
                right -= 2

        return int(max)


# @lc code=end
import time

soluion = Solution()
start = time.time()
input_string = input("_: ")
input_list = input_string.split()
input = [int(str) for str in input_list]
print(soluion.maxProduct(input))
print(f"time: {time.time() - start:.4f}s ")
