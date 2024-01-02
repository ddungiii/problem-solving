#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#


# @lc code=start
import ast
import collections
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Preprocessing nodes
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # BFS
        visited = set({k})
        queue = collections.deque([(k, 0)])
        taken_time = 0

        while queue:
            node, weight = queue.popleft()
            neighbors = graph[node]
            for v, w in neighbors:
                if v not in visited:
                    visited.add(v)

                    new_w = weight + w
                    queue.append((v, new_w))
                    taken_time = max(taken_time, new_w)

        if len(visited) != n:
            return -1

        return taken_time


# @lc code=end
import time

soluion = Solution()
start = time.time()

times = ast.literal_eval(input("times: "))
times = [[int(element) for element in sublist] for sublist in times]
n = int(input("n: "))
k = int(input("k: "))


print(soluion.networkDelayTime(times, n, k))
print(f"time: {time.time() - start:.4f}s ")
