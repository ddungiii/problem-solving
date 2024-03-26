#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start


class Solution:
    def find_pivot(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        return lo

    def search(self, nums: list[int], target: int) -> int:
        pivot = self.find_pivot(nums)

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            pivotted_mid = (mid + pivot) % len(nums)

            if nums[pivotted_mid] < target:
                lo = mid + 1
            elif nums[pivotted_mid] > target:
                hi = mid - 1
            else:
                return pivotted_mid

        return -1


# @lc code=end
