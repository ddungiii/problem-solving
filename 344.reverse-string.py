#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#


# @lc code=start
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i, char in enumerate(s):
            temp = s[-(i + 1)]
            s[-(i + 1)] = char
            s[i] = temp

            if i == len(s) // 2 - 1:
                break


# @lc code=end
