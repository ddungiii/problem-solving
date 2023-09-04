#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#


# @lc code=start
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])


# @lc code=end
import time

soluion = Solution()
start = time.time()
input_string = input("nums: ")
input_list = input_string.split()
input = [int(str) for str in input_list]
print(soluion.arrayPairSum(input))
print(f"time: {time.time() - start:.4f}s ")
