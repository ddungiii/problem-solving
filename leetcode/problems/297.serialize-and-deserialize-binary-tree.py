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
    def get_depth(self, root):
        def dfs(node, depth):
            if not node:
                return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            return max(left, right)

        return dfs(root, 0)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        depth = self.get_depth(root)

        def dfs(node, curr_depth):
            if curr_depth == depth:
                return

            val = node.val if node else None
            left = node.left if node else None
            right = node.right if node else None

            result.append(f"{val}")
            dfs(left, curr_depth + 1)
            dfs(right, curr_depth + 1)

        dfs(root, 0)
        result = " ".join(result)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        data = data.split(" ")
        data = collections.deque([ast.literal_eval(e) for e in data])
        depth = int(log(len(data) + 1, 2))

        def dfs(node, curr_depth):
            if curr_depth == depth:
                return

            left = TreeNode(data.popleft())
            dfs(left, curr_depth + 1)
            right = TreeNode(data.popleft())
            dfs(right, curr_depth + 1)

            if left.val is not None:
                node.left = left
            if right.val is not None:
                node.right = right

        root = TreeNode(data.popleft())
        dfs(root, 1)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
