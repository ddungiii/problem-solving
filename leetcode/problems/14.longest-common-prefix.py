#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        strs.sort(key=lambda x: len(x))
        target = strs[0]

        for i in range(len(target)):
            char = target[i]
            for str in strs:
                if char != str[i]:
                    return prefix
            prefix += char

        return prefix


# @lc code=end
