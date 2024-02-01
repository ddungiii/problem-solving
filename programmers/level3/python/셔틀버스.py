import collections


def time_to_tuple(time):
    """
    input: "08:00"
    output: (8, 0)
    """
    time = time.split(":")
    return int(time[0]), int(time[1])


def tuple_to_time(tuple):
    """
    input: (8, 0)
    output: "08:00"
    """
    hour, minute = f"{tuple[0]}", f"{tuple[1]}"
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute

    return f"{hour}:{minute}"


def convert_timetable(timetable):
    converted = [time_to_tuple(time) for time in timetable]
    converted.sort()
    return converted


def carry_over(time):
    hour, minute = time
    while minute >= 60:
        minute -= 60
        hour += 1

    return hour, minute


def carry_down(time):
    hour, minute = time
    while minute < 0:
        minute += 60
        hour -= 1

    return hour, minute


def lte_time(a, b):
    """
    13: 00 <= 14:00
    """
    for t1, t2 in zip(a, b):
        if t1 > t2:
            return False
        elif t1 < t2:
            return True

    return True


def split_timetable(n, t, m, timetable):
    """
    1, 1, 2, ["08:00", "08:01", "08:02", "08:03"]
    time: [09:00, 09:01]
    [["08:00", "08:01"], ["08:02", "08:03"]]

    => "08:02"
    """
    arrive_times = [(9, i * t) for i in range(n)]
    for i, time in enumerate(arrive_times):
        arrive_times[i] = carry_over(time)

    buses = collections.defaultdict(list)
    for arrive_time in arrive_times:
        if not timetable:
            buses[arrive_time] = []
            continue

        if not lte_time(timetable[0], arrive_time):
            buses[arrive_time] = []
            continue

        start = 0
        end = 0
        for i in range(min(m, len(timetable))):
            time = timetable[i]
            if lte_time(time, arrive_time):
                end = i

        buses[arrive_time] = timetable[start : end + 1]
        timetable = timetable[end + 1 :]

    return buses


def solution(n, t, m, timetable):
    # Timetable을 n, t, m 에 맞게 나눈다.
    # Success Crew, Fail Crew를 구분한다.
    # Success Crew 마지막에 추가한다.
    timetable = convert_timetable(timetable)
    buses = split_timetable(n, t, m, timetable)

    last_bus = list(buses.keys())[-1]
    last_bus_crews = buses[last_bus]

    if len(last_bus_crews) < m:
        return tuple_to_time(last_bus)
    elif len(last_bus_crews) == m:
        last_bus_crew = last_bus_crews[-1]
        faster = carry_down((last_bus_crew[0], last_bus_crew[1] - 1))
        return tuple_to_time(faster)
    else:
        return tuple_to_time(last_bus_crews[-1])


print(
    solution(
        3,
        2,
        2,
        ["08:00", "08:01", "08:02", "08:03", "08:04", "08:05", "08:06", "08:07"],
    )
)

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 1, ["23:59"]))
