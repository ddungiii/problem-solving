#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start


import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if not edges:
            return [0]

        graph = collections.defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)

            new_leaves = []
            for leaf in leaves:
                node = graph[leaf].pop()
                graph[node].remove(leaf)

                if len(graph[node]) == 1:
                    new_leaves.append(node)

            leaves = new_leaves

        return leaves


# @lc code=end
