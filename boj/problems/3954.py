"""
https://www.acmicpc.net/problem/3954

4
10 4 3
+-.,
qwe
1000 5 1
+[+-]
a
100 74 4
+++++[->++<]>[-<+++++++>]<[->+>+>+>+<<<<]>+++>--->++++++++++>---<<<.>.>.>.
xxyz
9999 52 14
+++++[>+++++++++<-],+[-[>--.++>+<<-]>+.->[<.>-]<<,+]
this_is_a_test
"""


def find_loops(program):
    stack = []
    loops = {}
    for i, c in enumerate(program):
        if c == "[":
            stack.append(i)
        if c == "]":
            start = stack.pop()
            loops[start] = i

    return loops


def brain_fuck(test):
    def interprete(c):
        nonlocal pc, loop_start, data_index, input_index

        if c == "-":
            data_array[data_index] -= 1
            data_array[data_index] %= 2**8
            pc += 1
        elif c == "+":
            data_array[data_index] += 1
            data_array[data_index] %= 2**8
            pc += 1
        elif c == "<":
            data_index -= 1
            data_index %= len(data_array)
            pc += 1
        elif c == ">":
            data_index += 1
            data_index %= len(data_array)
            pc += 1
        elif c == "[":
            loop_start = pc
            if data_array[data_index]:
                pc = loops[loop_start] - 1
            else:
                pc += 1
        elif c == "]":
            if not data_array[data_index]:
                pc = loop_start - 1
            else:
                pc += 1
        elif c == ".":
            pc += 1
        elif c == ",":
            data_array[data_index] = (
                ord(input[input_index]) if input_index < size_input else 255
            )
            input_index += 1
            pc += 1

    size_mem, size_program, size_input = test[0]
    program = test[1]
    input = test[2]

    # indexes
    data_index = 0
    input_index = 0
    pc = 0

    data_array = [0 for _ in range(size_mem // 8)]
    loops = find_loops(program)

    loop_count = 0
    loop_start = -1
    while pc < size_program:
        loop_count += 1

        interprete(program[pc])

        if loop_count > 50_000_000:
            return f"Loops {loop_start} {loops[loop_start]}"

    return "terminated"


def solution():
    # import time

    # start = time.time()

    for test in tests:
        print(brain_fuck(test))

    # print(f"time: {time.time() - start:.4f}s")


N = int(input())
tests = []
for _ in range(N):
    metadata = list(map(int, input().split()))
    program = input()
    input_program = input()
    tests.append((metadata, program, input_program))


solution()
