#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#


# @lc code=start


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        return list(s1.intersection(s2))


# @lc code=end
