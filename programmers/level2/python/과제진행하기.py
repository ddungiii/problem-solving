# 40분


def solution(plans):
    # preprocessing plans
    for i in range(len(plans)):
        start, time, playtime = plans[i]
        hour, minute = time.split(":")
        time_min = int(hour) * 60 + int(minute)

        plans[i] = [start, time_min, int(playtime)]

    plans.sort(key=lambda x: x[1])

    stack = []
    finish = []
    doing = None
    # do plan
    for plan in plans:
        start, time, playtime = plan

        if not doing:
            doing = plan
        else:
            s, t, p = doing
            doing = plan

            taken_time = time - t
            if taken_time >= p:
                taken_time -= p
                finish.append(s)
                while stack and taken_time > 0:
                    remain = stack.pop()
                    remain[1] -= taken_time
                    taken_time -= remain[1]

                    if remain[1] <= 0:
                        finish.append(remain[0])
                    else:
                        stack.append(remain)

            else:
                stack.append([s, p - taken_time])

    if doing:
        finish.append(doing[0])
    while stack:
        finish.append(stack.pop()[0])

    return finish
