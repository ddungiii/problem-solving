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
    public TreeNode bstToGst(TreeNode root) {
        this.dfs(root, 0);

        return root;
    }

    int dfs(TreeNode node, int acc) {
        if (node == null) {
            return acc;
        }

        acc = this.dfs(node.right, acc);
        acc += node.val;
        node.val = acc;
        acc = this.dfs(node.left, acc);

        return acc;
    }
}
// @lc code=end
