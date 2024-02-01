#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#


# @lc code=start
import string


class Solution:
    def is_palindrome(self, word: string):
        return word == word[::-1]

    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        length = len(words)

        pairs = []
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue

                if self.is_palindrome(words[i] + words[j]):
                    pairs.append((i, j))

        return pairs


# @lc code=end
