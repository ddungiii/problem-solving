#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#


# @lc code=start
from pydoc import splitdoc
import re
from typing import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [
            word
            for word in re.sub("[^\w]", " ", paragraph).lower().split()
            if word not in banned
        ]

        counter = Counter(words)

        return counter.most_common(1)[0][0]


# @lc code=end
