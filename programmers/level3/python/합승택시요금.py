import collections
import math

dp_and = collections.defaultdict(lambda: -1)  ## 합승 요금
dp_a = collections.defaultdict(lambda: -1)  ## a 요금
dp_b = collections.defaultdict(lambda: -1)  ## b 요금


def make_fares_dict(fares):
    dict = {}

    for c, d, f in fares:
        dict[(c, d)] = f
        dict[(d, c)] = f

    return dict


def make_graph(fares):
    graph = collections.defaultdict(list)
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    return graph


def find_min_path(start, dest):
    pass


def find_min_fare(fares_dict, graph, start, a, b, dest):
    min_fare = dp_and[dest] + dp_a[dest] + dp_b[dest]

    for neighbor in graph[start]:
        if dp_and[neighbor] < 0:
            dp_and[neighbor] = dp_and[dest] + fares_dict[(dest, neighbor)]

        min_fare = min(
            min_fare, find_min_fare(fares_dict, graph, start, a, b, neighbor)
        )

    return min_fare


def solution(n, s, a, b, fares):
    fares_dict = make_fares_dict(fares)
    graph = make_graph(fares)
    dp_and[s] = 0

    min_fare = find_min_fare(fares_dict, graph, s, a, b, s)

    return min_fare


print(
    solution(
        6,
        4,
        6,
        2,
        [
            [4, 1, 10],
            [3, 5, 24],
            [5, 6, 2],
            [3, 1, 41],
            [5, 1, 24],
            [4, 6, 50],
            [2, 4, 66],
            [2, 3, 22],
            [1, 6, 25],
        ],
    )
)
