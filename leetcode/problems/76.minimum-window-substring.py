#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check_substring(sub, t):
            """
            check sub contains all chars in t
            """
            counter = collections.Counter(sub)
            for c in t:
                count = counter[c]
                if count == 0:
                    return False
                else:
                    counter[c] -= 1

            return True

        M, N = len(s), len(t)
        if M < N:
            return ""

        window_size = N
        while window_size <= M:
            for r in range(window_size, M + 1):
                l = r - window_size
                if check_substring(s[l:r], t):
                    return s[l:r]

            window_size += 1

        return ""


# @lc code=end
