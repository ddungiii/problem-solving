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
        def findPalindromeFromCenter(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s)):
            result = max(
                result,
                findPalindromeFromCenter(i, i + 1),
                findPalindromeFromCenter(i, i + 2),
                key=len,
            )

        return result

    # @lc code=end


soluion = Solution()
start = time.time()
print(soluion.longestPalindrome(input("input: ")))
print(f"time: {time.time() - start:.4f}s ")
