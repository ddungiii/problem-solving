#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        answer = []
        q = collections.deque()  # store index

        for i, v in enumerate(nums):
            while q and nums[q[-1]] < v:
                q.pop()
            q.append(i)
            if i < k - 1:
                continue

            left = i - k + 1
            if q[0] < left:
                q.popleft()

            answer.append(nums[q[0]])

        return answer


# @lc code=end
