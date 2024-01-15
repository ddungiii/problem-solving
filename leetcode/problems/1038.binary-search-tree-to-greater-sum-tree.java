/*
 * @lc app=leetcode id=1038 lang=java
 *
 * [1038] Binary Search Tree to Greater Sum Tree
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
    int val = 0;

    public TreeNode bstToGst(TreeNode root) {
        if (root != null) {
            this.bstToGst(root.right);
            this.val += root.val;
            root.val = this.val;
            this.bstToGst(root.left);

        }

        return root;
    }
}
// @lc code=end
