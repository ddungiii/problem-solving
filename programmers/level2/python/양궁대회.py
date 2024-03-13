def update_max(apeach, ryan):
    global answer, point

    point_apeach = 0
    point_ryan = 0
    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue

        if apeach[i] >= ryan[i]:
            point_apeach += 10 - i
        else:
            point_ryan += 10 - i

    new_point = point_ryan - point_apeach
    if new_point > point:
        point = new_point
        answer = ryan


def dfs(info, n, i, l):
    global answer, point
    if n == 0:
        update_max(info, l)
        return

    for j in range(10, i - 1, -1):
        p = info[j]
        new_point = p + 1 if n > p + 1 else n

        new_l = l[:]
        new_l[j] = new_point
        dfs(info, n - new_point, j + 1, new_l)


def solution(n, info):
    global answer, point
    answer = [-1]
    point = 0
    dfs(info, n, 0, [0] * 11)

    return answer
