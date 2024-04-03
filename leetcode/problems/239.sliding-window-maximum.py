#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = collections.deque()
        curr_max = float("-inf")
        answer = []

        for i, v in enumerate(nums):
            q.append(v)
            if i < k - 1:
                continue

            if curr_max == float("-inf"):
                curr_max = max(q)
            elif v > curr_max:
                curr_max = v

            answer.append(curr_max)

            if curr_max == q.popleft():
                curr_max = float("-inf")

        return answer


# @lc code=end
