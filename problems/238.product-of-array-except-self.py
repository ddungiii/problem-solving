#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def product_all(nums: list[int]) -> int:
            result = 1
            for num in nums:
                result *= num

            return result

        all = product_all(nums)

        return list(map(lambda x: int(all / x) if x else all, nums))


# @lc code=end
import time

soluion = Solution()
start = time.time()
input_string = input("input: ")
input_list = input_string.split()
input = [int(str) for str in input_list]
print(soluion.productExceptSelf(input))
print(f"time: {time.time() - start:.4f}s ")
