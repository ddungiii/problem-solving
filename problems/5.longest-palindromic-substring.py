#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
import re
import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str) -> bool:
            s = re.sub("[^a-z0-9]", "", s)
            return s == s[::-1]

        if len(s) < 2 or s == s[::-1]:
            return s

        substr = s[0]

        for i in range(len(s)):
            # print(f"i: {i}")
            # print(f"substr: {substr}")
            for j in range(i + len(substr), len(s)):
                # print(f"  j: {j}")
                if isPalindrome(s[i : j + 1]):
                    substr = s[i : j + 1]

        # print(f"result: {substr}")
        return substr

    # @lc code=end


soluion = Solution()
start = time.time()
print(soluion.longestPalindrome(input("input: ")))
print(f"time: {time.time() - start:.4f}s ")
