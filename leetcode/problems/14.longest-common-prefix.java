/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 */

// @lc code=start

import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = new String();
        Arrays.sort(strs);
        String target = strs[0];

        for (int i = 0; i < target.length(); i++) {
            for (String str : strs) {
                if (str.charAt(i) != target.charAt(i)) {
                    return prefix;
                }
            }

            prefix += target.charAt(i);
        }

        return prefix;
    }
}
// @lc code=end
