from itertools import islice


DEBUG = False


def noop(x):
    return x


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())
