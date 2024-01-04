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
    result = 0

    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result


# @lc code=end
