def up(table, k, x):
    for i in range(x):
        k = table[k][0]

    return k


def down(table, k, x):
    for i in range(x):
        k = table[k][1]

    return k


def is_last(table, k):
    return table[k][1] == -1


def solution(n, k, cmd):
    # 1. Create table, Delete Stack
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[n - 1] = [n - 2, -1]
    delete_stack = []
    answer = ["O"] * n

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
            delete_stack.append(k)
            answer[k] = "X"

            prev, next = table[k]

            if prev != -1:
                table[prev][1] = next
            if next != -1:
                table[next][0] = prev

            if is_last(table, k):
                k = up(table, k, 1)
            else:
                k = down(table, k, 1)

        elif operator == "Z":
            poped = delete_stack.pop()
            answer[poped] = "O"
            prev, next = table[poped]

            if prev != -1:
                table[prev][1] = poped
            if next != -1:
                table[next][0] = poped

    return "".join(answer)
