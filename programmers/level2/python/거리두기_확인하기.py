def cal_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_ps(place):
    ps = []

    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                ps.append((r, c))

    return ps


def can_go(a, b, place):
    """
    ex) can not go
    P X P

    P X
    X P

    P
    X
    P
    """
    betweens = []
    if abs(a[0] - b[0]) == 2:
        betweens.append(((a[0] + (b[0] - a[0]) // 2), a[1]))
    elif abs(a[1] - b[1]) == 2:
        betweens.append((a[0], a[1] + (b[1] - a[1]) // 2))
    else:
        betweens.append((a[0], b[1]))
        betweens.append((b[0], a[1]))

    # 안막혀있으면 무조건 can go
    for between in betweens:
        if place[between[0]][between[1]] != "X":
            return True

    return False


def has_neighbor(p, ps, place):
    neighbors = [n for n in ps if cal_distance(p, n) <= 2]
    for neighbor in neighbors:
        if can_go(p, neighbor, place):
            return True

    return False


def is_safe(place):
    ps = get_ps(place)
    if len(ps) <= 1:
        return 1

    for i in range(len(ps)):
        if has_neighbor(ps[i], ps[i + 1 :], place):
            return 0

    return 1


def solution(places):
    return [is_safe(place) for place in places]
