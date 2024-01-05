#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
import ast
import collections
from math import log


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                result.append("#")
                continue

            result.append(f"{node.val}")

            queue.append(node.left)
            queue.append(node.right)

        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == "#":
            return
        data = data.split()
        data = data
        root = TreeNode(int(data[0]))

        queue = collections.deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if data[index] != "#":
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1

            if data[index] != "#":
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
