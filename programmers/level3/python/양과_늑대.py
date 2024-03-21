import collections

"""
Challenges

1. 어떻게 다시 백트래킹 할 것인가?
    -> visited를 해도 다시 가야함
"""

visited = collections.defaultdict(lambda: False)


def get_family_size(tree, parent):
    if len(tree[parent]) == 0:
        return 1

    count = 0
    for child in tree[parent]:
        count += get_family_size(tree, child)

    return count + 1


def search(info, tree, parent, sheep, wolf):
    is_sheep = info[parent] == 0
    if not visited[parent]:
        if is_sheep:
            sheep += 1
        else:
            wolf += 1

    visited[parent] = True

    if not is_sheep:
        return
    family_size = get_family_size(tree, parent)

    return 1


def solution(info, edges):
    # 1. Create Tree
    tree = collections.defaultdict(list)
    for edge in edges:
        p, c = edge
        tree[p].append(c)

    # 2. Search with Back Tracking, greedy
    return search(info, tree, 0, 0, 0)
