

# SRC: https://projecteuler.net/problem=1
def sum_multiples(limit, multiples):
    nums = set(
        num
        for num in range(limit)
        for multiple in multiples
        if (num % multiple) == 0)  # is even

    return sum(nums)
