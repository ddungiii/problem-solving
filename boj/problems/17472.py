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
"""

import collections


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


def bfs(r: int, c: int, visited: set):
    deque = collections.deque([(r, c)])
    island = set([(r, c)])

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
                island.add((nr, nc))

    return list(island)


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


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        parent[a] = b


def kruskal():
    answer, count = 0, 0

    for a, b, length in bridges:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)

            answer += length
            count += 1

    return answer, count


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

parent = [i for i in range(len(islands) + 1)]
bridges.sort(key=lambda x: x[2])

answer, count = kruskal()

print(answer if count == len(islands) - 1 else -1)
