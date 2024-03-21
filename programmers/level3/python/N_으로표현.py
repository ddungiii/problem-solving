def solution(N, number):
    if N == number:
        return 1

    nums = [set() for _ in range(9)]

    for i in range(1, 9):
        nums[i].add(int(str(N) * i))
        for j in range(1, i):
            for num1 in nums[j]:
                for num2 in nums[i - j]:
                    nums[i].add(num1 + num2)
                    nums[i].add(num1 - num2)
                    nums[i].add(num1 * num2)
                    if num2 > 0:
                        nums[i].add(num1 // num2)

        if number in nums[i]:
            return i

    return -1
