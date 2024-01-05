#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
import collections
from re import L
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def get_depth(root) -> int:
            def dfs(node, depth):
                if not node:
                    return depth

                depth_left = dfs(node.left, depth + 1)
                depth_right = dfs(node.right, depth + 1)

                return max(depth_left, depth_right)

            return dfs(root, 0)

        def deseralize(root, depth) -> list:
            l = []

            def dfs(node, curr_depth):
                if curr_depth == depth:
                    return

                l.append(node.val if node else None)

                left = node.left if node else None
                right = node.right if node else None
                dfs(left, curr_depth + 1)
                dfs(right, curr_depth + 1)

            dfs(root, 0)
            return l

        def serialize(array, depth):
            root = TreeNode(array.popleft())

            def dfs(root, curr_depth):
                if curr_depth == depth:
                    return

                left = TreeNode(array.popleft())
                dfs(left, curr_depth + 1)

                right = TreeNode(array.popleft())
                dfs(right, curr_depth + 1)

                if root:
                    if left.val:
                        root.left = left
                    if right.val:
                        root.right = right

            dfs(root, 1)
            return root

        # Deserialize (Tree to List)
        depth = max(get_depth(root1), get_depth(root2))
        if depth == 0:
            return root1

        list1 = deseralize(root1, depth)
        list2 = deseralize(root2, depth)

        # Merge
        merged = collections.deque([])
        for x, y in zip(list1, list2):
            if x is None and y is None:
                merged.append(None)
            else:
                x = x if x else 0
                y = y if y else 0

                merged.append(x + y)

        # Serialize (List to Tree)
        new_root = serialize(merged, depth)

        return new_root


# @lc code=end
