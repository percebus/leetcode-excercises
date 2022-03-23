from aloe import step, world
from problems.interviews.shortest_common_prefixes import get_prefixes


def clean(word):
    return word.replace("''", '')


def parse(words):
    return [
        clean(word)
        for word
        in words.split(', ')
    ]


@step("a list of (?P<words>.+)")
def step_impl(self, words):
    world.words = parse(words)


@step("I call longest_common_prefixes")
def step_impl(self):
    world.result = get_prefixes(world.words)


@step("find the shortest common (?P<prefixes>.+) strings amongst an array of strings")
def step_impl(self, prefixes):
    expected = parse(prefixes)
    assert ''.join(expected) == ''.join(world.result), f"expected:{expected}, got:{world.result}"
