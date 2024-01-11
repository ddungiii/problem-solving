/*
 * @lc app=leetcode id=310 lang=java
 *
 * [310] Minimum Height Trees
 */

// @lc code=start

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (edges.length == 0) {
            ArrayList<Integer> list = new ArrayList<Integer>();
            list.add(0);
            return list;
        }

        HashMap<Integer, HashSet<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            if (!graph.containsKey(u)) {
                graph.put(u, new HashSet<>());
            }
            if (!graph.containsKey(v)) {
                graph.put(v, new HashSet<>());
            }

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        HashSet<Integer> leaves = new HashSet();
        for (int i = 0; i < n; i++) {
            if (graph.containsKey(i) && graph.get(i).size() == 1) {
                leaves.add(i);
            }
        }

        while (n > 2) {
            n -= leaves.size();

            HashSet<Integer> new_leaves = new HashSet<>();
            for (int leaf : leaves) {
                int node = graph.get(leaf).iterator().next();
                graph.get(node).remove(leaf);

                if (graph.get(node).size() == 1) {
                    new_leaves.add(node);
                }
            }
            leaves = new_leaves;
        }

        return new ArrayList<Integer>(leaves);
    }
}
// @lc code=end
