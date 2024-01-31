#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc code=start
class Node:
    def __init__(self, val=None, end=False):
        self.val = val
        self.end = end
        self.children = []

    def __str__(self):
        return f"{self.val}, {self.children}"


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            success = False
            for child in node.children:
                if c == child.val:
                    node = child
                    success = True
                    break

            if success:
                continue

            # Fail to find node
            new_node = Node(c)
            node.children.append(new_node)
            node = new_node

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            success = False
            for child in node.children:
                if c == child.val:
                    node = child
                    success = True
                    break

            if not success:
                return False

        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            success = False
            for child in node.children:
                if c == child.val:
                    node = child
                    success = True
                    break

            if not success:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
