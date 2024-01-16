/*
 * @lc app=leetcode id=938 lang=java
 *
 * [938] Range Sum of BST
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
    int sum = 0;

    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {
            return this.sum;
        }

        if (low <= root.val && root.val <= high) {
            this.sum += root.val;
        }

        this.rangeSumBST(root.left, low, high);
        this.rangeSumBST(root.right, low, high);

        return this.sum;
    }
}
// @lc code=end
