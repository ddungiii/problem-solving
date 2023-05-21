#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = defaultdict(list)
        for str in strs:
            dict["".join(sorted(str))].append(str)

        return dict.values()


# @lc code=end
