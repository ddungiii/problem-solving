"""
[[2, 3], [4, 3], [1, 1], [2, 1]]

[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
"""

import collections


def make_graph(edges):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])

    return graph


def get_starting_node(graph, edges):
    sources = set([e[0] for e in edges])
    destinations = set([e[1] for e in edges])

    for sourse in sources:
        if (sourse not in destinations) and len(graph[sourse]) > 1:
            return sourse

    raise Exception


def get_type(graph, neighbor):
    """
    1: donut
    2: bar
    3: 8

    -1: not found
    """
    next = graph[neighbor]

    while len(next) > 0:
        if len(next) > 1:
            return 3

        if neighbor in next:
            return 1

        next = graph[next[0]]

    return 2


def find_answer(graph, node):
    """
    return [created node, # of donut, # of bar, # of 8]
    """
    neighbors = graph[node]
    answer = [node, 0, 0, 0]

    for neighbor in neighbors:
        type = get_type(graph, neighbor)
        if type < 0:
            return [-1, -1, -1, -1]

        answer[type] += 1

    return answer


def solution(edges):
    graph = make_graph(edges)
    starting_node = get_starting_node(graph, edges)

    answer = find_answer(graph, starting_node)

    return answer


edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
edges = [
    [4, 11],
    [1, 12],
    [8, 3],
    [12, 7],
    [4, 2],
    [7, 11],
    [4, 8],
    [9, 6],
    [10, 11],
    [6, 10],
    [3, 5],
    [11, 1],
    [5, 3],
    [11, 9],
    [3, 8],
]

print(solution(edges))
