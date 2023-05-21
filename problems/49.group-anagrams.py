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
            str_list = list(str)
            str_list.sort()
            key = "".join(str_list)

            dict[key].append(str)

        return dict.values()


# @lc code=end
