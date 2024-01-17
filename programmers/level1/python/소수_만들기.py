def solution(nums):
    def is_prime(n):
        if n == 1:
            return False

        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                return False

        return True

    import itertools

    count = 0
    comb = itertools.combinations(nums, 3)

    for i, j, k in comb:
        if is_prime(i + j + k):
            count += 1

    return count
