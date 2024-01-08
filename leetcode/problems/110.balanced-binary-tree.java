/*
 * @lc app=leetcode id=110 lang=java
 *
 * [110] Balanced Binary Tree
 */

// @lc code=start

//  Definition for a binary tree node.
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
    boolean result = true;

    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }

        dfs(root, 0);

        return this.result;
    }

    private int dfs(TreeNode node, int depth) {
        if (node == null) {
            return depth;
        }

        int left = dfs(node.left, depth + 1);
        int right = dfs(node.right, depth + 1);

        if (Math.abs(left - right) > 1) {
            this.result = false;
        }

        return Math.max(left, right);
    }
}
// @lc code=end
