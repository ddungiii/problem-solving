#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start


import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        def make_tree(root):
            tree = collections.defaultdict(list)
            visited = set([root])

            queue = [root]
            while queue:
                node = queue.pop()

                neighbors = graph[node]
                for neighbor in neighbors:
                    if not neighbor in visited:
                        tree[node].append(neighbor)
                        queue.append(neighbor)
                        visited.add(neighbor)

            return tree

        def get_height(tree, root, depth):
            heights = [depth]
            for node in tree[root]:
                heights.append(get_height(tree, node, depth + 1))

            return max(heights)

        # Preprocessing
        heights = []

        graph = collections.defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)

        # Get height
        for i in range(n):
            tree = make_tree(i)
            height = get_height(tree, i, 0)
            heights.append((i, height))

        # Get min heights
        heights.sort(key=lambda x: x[1])
        min_height = heights[0][1]

        heights = [node for node, h in heights if h == min_height]

        return heights


# @lc code=end
