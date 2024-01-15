def solution(nums):
    def is_prime(n):
        if n == 1:
            return False

        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                return False

        return True

    length = len(nums)
    count = 0

    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    count += 1

    return count
