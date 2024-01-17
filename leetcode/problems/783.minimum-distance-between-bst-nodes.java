/*
 * @lc app=leetcode id=783 lang=java
 *
 * [783] Minimum Distance Between BST Nodes
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private int prev = Integer.MIN_VALUE;
    private int min_diff = Integer.MAX_VALUE;

    public int minDiffInBST(TreeNode root) {
        if (root.left != null) {
            this.minDiffInBST(root.left);
        }
        if (prev != Integer.MIN_VALUE) {
            min_diff = Math.min(min_diff, root.val - prev);
        }
        prev = root.val;

        if (root.right != null) {
            this.minDiffInBST(root.right);
        }

        return min_diff;
    }
}
// @lc code=end
