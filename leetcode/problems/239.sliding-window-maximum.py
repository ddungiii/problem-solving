#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        answer = []
        for right in range(k, len(nums) + 1):
            left = right - k
            answer.append(max(nums[left:right]))

        return answer


# @lc code=end
