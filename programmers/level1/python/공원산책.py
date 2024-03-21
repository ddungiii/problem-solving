directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def execute(map, route, loc):
    direction, distance = route.split(" ")

    if direction == "E":
        direction = directions[0]
    elif direction == "W":
        direction = directions[1]
    elif direction == "S":
        direction = directions[2]
    else:
        direction = directions[3]

    nr, nc = loc
    dr, dc = direction
    for _ in range(int(distance)):
        nr += dr
        nc += dc
        if (
            0 > nr
            or nr >= len(map)
            or 0 > nc
            or nc >= len(map[0])
            or map[nr][nc] == "X"
        ):
            return loc

    return nr, nc


def solution(park, routes):
    map = [[c for c in p] for p in park]
    H = len(map)
    W = len(map[0])

    loc = None
    for r in range(H):
        for c in range(W):
            if map[r][c] == "S":
                loc = r, c

    for route in routes:
        loc = execute(map, route, loc)

    return list(loc)
