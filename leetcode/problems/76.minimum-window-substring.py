#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M, N = len(s), len(t)
        if M < N:
            return ""

        need = collections.Counter(t)
        missing = N
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                # move until missing == 0
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # update start, end
                best_min = end - start
                curr_min = right - left
                if not end or curr_min < best_min:
                    start, end = left, right

                # move left
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]


# @lc code=end
