#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        max_diameter = 0

        def get_depth(node, depth):
            if not node:
                return depth

            depth_left = get_depth(node.left, depth + 1)
            depth_right = get_depth(node.right, depth + 1)

            diameter = (depth_left - depth - 1) + (depth_right - depth - 1)
            nonlocal max_diameter
            max_diameter = max(max_diameter, diameter)

            return max(depth_left, depth_right)

        get_depth(root, 0)

        return max_diameter


# @lc code=end
