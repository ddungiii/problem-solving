#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        # Initialize
        stack = collections.deque([root])
        longest_length = 0

        path = [root]
        length = -1

        # Define sub-functions
        def is_child(parent, node):
            return parent.left == node or parent.right == node

        def is_on_the_path(node):
            for parent in path:
                if parent.val == node.val and is_child(parent, node):
                    return True

            return False

        # DFS
        while stack:
            node = stack.pop()
            if not node:
                continue

            if is_on_the_path(node):
                length += 1
                path.append(node)
            else:
                length = 0
                path = [node]

            longest_length = max(longest_length, length)

            left, right = node.left, node.right
            stack.append(left)
            stack.append(right)

        return longest_length


# @lc code=end
