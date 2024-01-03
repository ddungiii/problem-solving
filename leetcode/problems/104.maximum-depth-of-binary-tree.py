#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def search(node, depth):
            if not node:
                return depth
            left, right = node.left, node.right

            return max(search(left, depth + 1), search(right, depth + 1))

        return search(root, 0)


# @lc code=end
