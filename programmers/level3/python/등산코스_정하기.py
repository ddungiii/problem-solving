import collections
import heapq


def dijkstra(graph, gates):
    intensities = collections.defaultdict(int)
    Q = [(0, gate) for gate in gates]

    while Q:
        intensity, node = heapq.heappop(Q)
        if node in intensities:
            continue

        intensities[node] = intensity
        for v, inten in graph[node]:
            new_inten = max(inten, intensity)
            heapq.heappush(Q, (new_inten, v))

    return intensities


def solution(n, paths, gates, summits):
    # 1. Create graph
    graph = collections.defaultdict(list)
    for path in paths:
        i, j, w = path
        graph[i].append((j, w))
        graph[j].append((i, w))

    intensities = dijkstra(graph, gates)
    submit_inten = [
        (inten, intensities[inten]) for inten in intensities if inten in summits
    ]
    submit_inten.sort(key=lambda x: (x[1], x[0]))

    return submit_inten[0]
