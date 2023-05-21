#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#


# @lc code=start
from lib2to3.fixes.fix_print import parend_expr
import re
from typing import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Ban log word first
        banned.sort(key=lambda ban: -len(ban))

        paragraph = paragraph.lower()

        for banned_str in banned:
            paragraph = paragraph.replace(banned_str, "")

        paragraph = re.sub("[!?',;.]", " ", paragraph)

        paragraph_list = paragraph.split()
        counter = Counter(paragraph_list)

        return counter.most_common(1)[0][0]


# @lc code=end
