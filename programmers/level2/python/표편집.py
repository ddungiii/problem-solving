def up(table, k, x):
    while x > 0:
        k -= 1
        while table[k] == "X":
            k -= 1

        x -= 1

    return k


def down(table, k, x):
    while x > 0:
        k += 1
        while table[k] == "X":
            k += 1

        x -= 1

    return k


def is_last(table, k):
    for deleted in table[k:]:
        if deleted == "O":
            return False

    return True


def solution(n, k, cmd):
    # 1. Create table, Delete Queue
    table = ["O"] * n
    delete_queue = []

    for stmt in cmd:
        splited = stmt.split(" ")
        operator = splited[0]

        if operator == "U":
            operand = splited[1]
            k = up(table, k, int(operand))

        elif operator == "D":
            operand = splited[1]
            k = down(table, k, int(operand))

        elif operator == "C":
            table[k] = "X"
            delete_queue.append(k)

            if is_last(table, k):
                k = up(table, k, 1)
            else:
                k = down(table, k, 1)

        elif operator == "Z":
            poped = delete_queue.pop()
            table[poped] = "O"

    return "".join(table)
