import collections

max_sheep = 0


def dfs(info, tree, parent, sheep, wolf, nexts):
    global max_sheep

    sheep += info[parent] ^ 1
    wolf += info[parent]

    max_sheep = max(max_sheep, sheep)
    if sheep <= wolf:
        return

    for child in tree[parent]:
        nexts.add(child)

    for i, next in enumerate(nexts):
        new_nexts = set(nexts)
        new_nexts.remove(next)
        dfs(info, tree, next, sheep, wolf, new_nexts)


def solution(info, edges):
    # 1. Create Tree
    tree = collections.defaultdict(list)
    for edge in edges:
        p, c = edge
        tree[p].append(c)

    dfs(info, tree, 0, 0, 0, set(tree[0]))
    return max_sheep
