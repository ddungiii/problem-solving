#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0

    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if not root:
            return

        if low <= root.val <= high:
            self.sum += root.val

        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)

        return self.sum


# @lc code=end
