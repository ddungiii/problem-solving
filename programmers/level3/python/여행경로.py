import collections


def solution(tickets):
    map = collections.defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        map[src].append(dst)

    path = []

    def dfs(src):
        while map[src]:
            dfs(map[src].pop())
        path.append(src)

    dfs("ICN")

    return path[::-1]
