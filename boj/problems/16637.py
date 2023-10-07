"""
https://www.acmicpc.net/problem/16637
"""

len = int(input())
expression = input()

# pre-processing
len += 1
expression = "+" + expression


def dfs(i: int, result: int):
    if i == len:
        return result

    operator = expression[i]
    a = expression[i + 1]

    if i == len - 2:
        return eval(f"{result} {operator} {a}")

    operator_2 = expression[i + 2]
    b = expression[i + 3]

    return max(
        dfs(i + 2, eval(f"{result} {operator} {a}")),
        dfs(i + 4, eval(f"{result} {operator} ({a} {operator_2} {b})")),
    )


result = dfs(0, 0)

print(result)
