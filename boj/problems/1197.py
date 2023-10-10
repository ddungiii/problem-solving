"""
https://www.acmicpc.net/problem/1197

3 3
1 2 1
2 3 2
1 3 3
"""


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_parent(a, b):
    a = parent[a]
    b = parent[b]

    if a != b:
        parent[a] = b


def kruskal():
    answer, count = 0, 0

    for a, b, dist in graph:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)

            answer += dist
            count += 1

    return answer, count


V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])

parent = [i for i in range(V + 1)]

answer, count = kruskal()

print(answer)
