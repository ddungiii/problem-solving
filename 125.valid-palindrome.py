#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for _s in s:
            if _s.isalnum():
                s_list.append(_s.lower())

        for i, char in enumerate(s_list):
            if char != s_list[-(i + 1)]:
                return False

        return True


# @lc code=end
