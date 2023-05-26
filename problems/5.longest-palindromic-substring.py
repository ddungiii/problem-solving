#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
import re


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str) -> bool:
            print(f"isPalindrome({s})")
            s = re.sub("[^a-z0-9]", "", s)
            return s == s[::-1]

        substr = ""

        for i in range(len(s)):
            print(f"i: {i}")
            for j in range(i + 1 + len(substr), len(s)):
                print(f"  j: {j}")
                if isPalindrome(s[i:j]):
                    substr = s[i:j]

        print(substr)


# @lc code=end
