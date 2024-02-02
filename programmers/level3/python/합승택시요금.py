import collections
import heapq
import math

dp = {}


def make_graph(fares):
    graph = collections.defaultdict(list)
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    return graph


def djikstra(graph, start):
    Q = [(0, start)]
    dist = collections.defaultdict(lambda: math.inf)

    while Q:
        weight, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = weight
            for v, w in graph[node]:
                heapq.heappush(Q, (weight + w, v))

    return dist


def solution(n, s, a, b, fares):
    graph = make_graph(fares)

    for i in range(1, n + 1):
        dp[i] = djikstra(graph, i)

    min_fare = math.inf
    for i in range(1, n + 1):
        fare = dp[s][i] + dp[i][a] + dp[i][b]
        min_fare = min(min_fare, fare)

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

print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
