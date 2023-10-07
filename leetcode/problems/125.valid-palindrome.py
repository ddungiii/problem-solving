#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)

        return s == s[::-1]


# @lc code=end
