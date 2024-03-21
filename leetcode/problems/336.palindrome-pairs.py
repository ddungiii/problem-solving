#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#


# @lc code=start
import collections


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.index = -1
        self.palindrome_ids = []


class Trie:
    def __init__(self):
        self.root = Node()

    def is_palindrome(self, word: str):
        return word == word[::-1]

    def insert(self, word: str, index: int) -> None:
        node = self.root
        for i, c in enumerate(word):
            if self.is_palindrome(word[len(word) - i]):
                node.palindrome_ids.append(i)

            node = node.children[c]
        node.index = index

    def search(self, index, word: str) -> bool:
        node = self.root
        result = []

        while word:
            if word[0] not in node.children:
                return result

            word = word[1:]

        if node.index >= 0 and node.index != index:
            result.append([index, node.index])

        return result


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word, i)

        pairs = []
        for i, word in enumerate(words):
            pairs.extend(trie.search(i, word))

        return pairs


# @lc code=end
