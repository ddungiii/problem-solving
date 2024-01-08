#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = True

    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def dfs(node, depth):
            if not node:
                return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            if abs(left - right) > 1:
                self.result = False

            return max(left, right)

        dfs(root, 0)

        return self.result


# @lc code=end
