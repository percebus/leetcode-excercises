from pprint import pprint
import string
import more_itertools

DEBUG = False

def categorize(words, prefix=''):
    if len(words) == 1:
        return words[0]

    result = {}
    for letter in string.ascii_lowercase:
        _prefix = prefix+letter
        subset = [
            word
            for word in words
            if word.startswith(_prefix)
        ]

        if subset:
            result[_prefix] = categorize(subset, _prefix)

    return result


def pluck(data):
    results = []

    def recurse(dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                recurse(value)
            # elif (type(value) is str): # TODO? or XXX? overkill?
            else:  # its a str then
                results.append(key)  # FIXME very inefficient

    recurse(data)  # FIXME procdural
    return results


def pluck2(data):
    def recurse(dictionary):
        return [
            recurse(value) if isinstance(value, dict) else key
            for key, value in dictionary.items()
        ]

    results = recurse(data)
    return more_itertools.collapse(results)


def get_prefixes(words):
    data = categorize(words)
    if DEBUG:
        pprint(data)

    # {
    #   'b': 'bananas',
    #   'd': {
    #       'do': {
    #           'dog': 'dog',
    #           'dov': 'dove'},
    #       'du': 'duck'
    #       },
    #   'z': 'zebra'
    # }

    # TODO benchmark pluck VS pluck2 performance
    return list(pluck2(data))


def run(words, expected=None):
    actual = get_prefixes(words)
    assert actual == expected, f'expected:{expected}, got:{actual}'


def run_all():
    run([], expected=[])
    run(('dog', 'zebra', 'bananas'), expected=['b', 'd', 'z'])
    run(('dog', 'zebra', 'duck', 'bananas'), expected=['b', 'do', 'du', 'z'])
    run(('dog', 'zebra', 'duck', 'dove', 'bananas'), expected=['b', 'dog', 'dov', 'du', 'z'])


if __name__ == '__main__':
    run_all()
