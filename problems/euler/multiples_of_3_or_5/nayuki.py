

# SRC: https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p001.py?ts=4
def sum_multiples(limit):
    return sum(x for x in range(limit) if (x % 3 == 0 or x % 5 == 0))
