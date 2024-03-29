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
            loops[i] = start

    return loops


def interprete(c):
    global pc, data_index, input_index

    if c == "-":
        data_array[data_index] -= 1
        data_array[data_index] %= 2**8
    elif c == "+":
        data_array[data_index] += 1
        data_array[data_index] %= 2**8
    elif c == "<":
        data_index -= 1
        data_index %= size_mem
    elif c == ">":
        data_index += 1
        data_index %= size_mem
    elif c == "[":
        if not data_array[data_index]:
            pc = loops[pc]
    elif c == "]":
        if data_array[data_index]:
            pc = loops[pc]
    elif c == ".":
        pass
    elif c == ",":
        data_array[data_index] = (
            ord(input[input_index]) if input_index < size_input else 255
        )
        input_index += 1


def brain_fuck():
    global loop_start, pc

    loop_count = 0
    while pc < size_program:
        loop_count += 1
        interprete(program[pc])
        if loop_count > 50_000_000:
            loop_start = min(loop_start, pc)
        if loop_count > 2 * 50_000_000:
            print(f"Loops {loop_start} {loops[loop_start]}")
            return

        pc += 1

    print("Terminates")


N = int(input())
tests = []
for _ in range(N):
    metadata = list(map(int, input().split()))
    program = input()
    input_program = input()
    tests.append((metadata, program, input_program))

for test in tests:
    size_mem, size_program, size_input = test[0]
    program = test[1]
    input = test[2]

    # indexes
    data_index = 0
    input_index = 0
    pc = 0

    data_array = [0 for _ in range(size_mem)]
    loops = find_loops(program)

    loop_start = size_program
    brain_fuck()
