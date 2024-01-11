/*
 * @lc app=leetcode id=108 lang=java
 *
 * [108] Convert Sorted Array to Binary Search Tree
 */

// @lc code=start

import java.util.Arrays;

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
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }

        int mid = nums.length / 2;

        TreeNode left = this.sortedArrayToBST(Arrays.copyOfRange(nums, 0, mid));
        TreeNode right = this.sortedArrayToBST(Arrays.copyOfRange(nums, mid + 1, nums.length));
        return new TreeNode(nums[mid], left, right);
    }
}
// @lc code=end
