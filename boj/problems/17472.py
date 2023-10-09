"""
https://www.acmicpc.net/problem/17472

7 8
0 0 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1

1. find all islands as a list
2. find all possible bridges for a island.
3. find minimum distance
"""

import collections
import itertools


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


def bfs(r: int, c: int, visited: set):
    deque = collections.deque([(r, c)])
    island = [(r, c)]

    while deque:
        _r, _c = deque.popleft()

        for i in range(4):
            nr = _r + dr[i]
            nc = _c + dc[i]
            if (
                (0 <= nr < N)
                and (0 <= nc < M)
                and (nr, nc) not in visited
                and matrix[nr][nc] == 1
            ):
                visited.add((nr, nc))
                deque.append((nr, nc))
                island.append((nr, nc))

    return island


def find_islands():
    """
    Find all islands using BFS
    """
    visited = set()
    islands = []

    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 1 and (r, c) not in visited:
                islands.append(bfs(r, c, visited))

    return islands


def build_bridges(id: int, island: list):
    def can_go(r, c):
        return (0 <= r < N) and (0 <= c < M) and matrix[r][c] != 1

    def find_reached_island(r, c):
        for i, island in enumerate(islands):
            if (r, c) in island:
                return i

        return -1

    bridges = set()
    for r, c in island:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            len = 0
            while can_go(nr, nc):
                len += 1

                nr = nr + dr[i]
                nc = nc + dc[i]

            reached_island = find_reached_island(nr, nc)

            if len < 2 or reached_island == -1:
                continue

            bridges.add((id, reached_island, len))

    return bridges


def bfs_min(comb: list):
    start = comb[0]
    deque = collections.deque([start])
    visited = set([start])
    visited_island = set([start[0], start[1]])

    while deque:
        bridge = deque.popleft()
        a, b, length = bridge

        for _b, _length in bridges_dict[b]:
            new_node = (b, _b, _length)
            if new_node not in visited and new_node in comb:
                deque.append(new_node)
                visited.add(new_node)
                visited_island.add(b)
                visited_island.add(_b)

    return (
        sum([length for _, _, length in comb])
        if len(visited_island) == len(islands)
        else float("inf")
    )


"""
Solve Problem
"""
islands = find_islands()
bridges_dict = collections.defaultdict(list)
bridges = []
for id, island in enumerate(islands):
    _bridges = build_bridges(id, island)
    for _bridge in _bridges:
        a, b, length = _bridge
        bridges_dict[a].append((b, length))
        bridges.append(_bridge)


answer = float("inf")
for i in range(1, len(bridges) + 1):
    combs = itertools.combinations(bridges, i)
    for comb in combs:
        answer = min(answer, bfs_min(list(comb)))

print(answer if answer != float("inf") else -1)
