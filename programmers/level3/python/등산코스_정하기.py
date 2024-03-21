import collections
import math
import copy

MAX = 100_000_000


def dfs(graph, visited, node, target, intensity):
    if node == target:
        return intensity

    visited.add(node)
    count = 0
    for neighbor, w in graph[node]:
        if neighbor not in visited:
            max_intensity = max(intensity, w)
            intensity = min(
                intensity,
                dfs(graph, copy.deepcopy(visited), neighbor, target, max_intensity),
            )
            count += 1

    if not count:
        return MAX

    return intensity


def find_path(graph, gate, summit):
    shortest = MAX
    for neighbor, w in graph[summit]:
        shortest = min(shortest, dfs(graph, set([summit]), neighbor, gate, w))

    return shortest


def get_shortest(graph, gates, summit):
    shortest = MAX
    for gate in gates:
        intensity = find_path(graph, gate, summit)
        shortest = min(shortest, intensity)

    return summit, shortest


def solution(n, paths, gates, summits):
    # 1. Create graph
    graph = collections.defaultdict(list)
    for path in paths:
        i, j, w = path
        graph[i].append((j, w))
        graph[j].append((i, w))

    answer = []
    for summit in summits:
        answer.append(get_shortest(graph, gates, summit))

    # sort by intensity, summit
    answer.sort(key=lambda x: (x[1], x[0]))

    return answer[0]


s
