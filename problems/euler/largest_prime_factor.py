

def get_factors(x):
    nums = range(x + 1)
    return (
        (a, b)
        for a in nums
        for b in (num for num in nums if num >= a)
        if (a * b) == x
    )


def is_prime_number(x):
    if x == 0:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False

    count = 0
    for pair in get_factors(x):
        count += 1
        if count > 1:
            return False

    return True


def get_prime_factors(num):
    nums = [
        num
        for pair in get_factors(num)
        for num in pair
    ]

    nums.sort(reverse=True)
    for num in nums:
        if is_prime_number(num):
            return num

    return None


def run(x: int, expected=None):
    result = get_prime_factors(x)
    assert result == expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


if __name__ == '__main__':
    # The prime factors of 13195 are 5, 7, 13 and 29.
    run(13195, expected=29)

    # What is the largest prime factor of the number 600851475143 ?
    run(600851475143, expected=10)
