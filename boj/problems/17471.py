"""
https://www.acmicpc.net/problem/17471

6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
"""
import itertools, collections


def bfs(comb: list):
    start = comb[0]
    sum = 0
    visited = set([start])
    deque = collections.deque([start])

    while deque:
        node = deque.popleft()
        sum += population[node]

        for v in neighbors_list[node]:
            if v not in visited and v in comb:
                deque.append(v)
                visited.add(v)

    return sum, len(visited)


def solution():
    """
    bfs

    1. Divide combinations of nodes fist.
    2. And check whether it is possible.
      2-1. Using BFS, check all nodes can visited
    3. If possible, calculate
    """
    answer = float("inf")
    for i in range(1, N // 2 + 1):
        for combs in itertools.combinations(range(N), i):
            remain_comb = [j for j in range(N) if j not in combs]
            sum_1, visited_1 = bfs(list(combs))
            sum_2, visited_2 = bfs(remain_comb)

            if visited_1 + visited_2 == N:
                answer = min(answer, abs(sum_1 - sum_2))

    return answer if answer != float("inf") else -1


N = int(input())
population = list(map(int, input().split()))
neighbors_list = []
for i in range(N):
    neighbor = list(map(int, input().split()[1:]))
    neighbor = [n - 1 for n in neighbor]
    neighbors_list.append(neighbor)

print(solution())
