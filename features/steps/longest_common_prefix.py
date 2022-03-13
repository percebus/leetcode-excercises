import string
from aloe import before, step, world
from test.utils import assert_is_in_range
from problems.leetcode.longest_common_prefix import longest_common_prefix


valid_chars = list(string.ascii_lowercase) + ['']

constraints = {
    'words': {'min': 1, 'max': 200},  # 1 <= strs.length <= 200
    'word' : {'min': 0, 'max': 200}   # 0 <= strs[i].length <= 200
}


def validate_chars(word):
    for char in list(word):  # strs[i] consists of only lower-case English letters. # TODO
        if char not in valid_chars:
            raise Exception("invalid character")
    return True


def validate_word(word):
    assert_is_in_range(len(word), constraints['word'])
    validate_chars(word)
    return True


def validate_words(words):
    assert_is_in_range(len(words), constraints['words'])
    for word in words:
        validate_word(word)
    return True


def clean(word):
    return word.replace("''", '')


def parse(words):
    return [
        clean(word)
        for word
        in words.split(', ')
    ]


def log(exception):
    print(exception)


@before.each_example
def before_example(scenario, outline, steps):
    world.words = None
    world.result = None
    world.exception = None


@step("some (?P<words>.+)")
def step_impl(self, words):
    world.words = parse(words)
    validate_words(world.words)


@step("an array of invalid (?P<strings>.+)")
def step_impl(self, strings):
    strings = parse(strings)
    try:
        validate_words(strings)
        world.words = strings
    except Exception as exception:
        world.exception = exception


@step("I call longest_common_prefix")
def step_impl(self):
    world.result = longest_common_prefix(world.words)


@step("find the longest common (?P<prefix>.+) string amongst an array of strings")
def step_impl(self, prefix):
    expected = clean(prefix)
    assert world.result == expected, f"expected:'{expected}', got:{world.result}"


@step("returns an empty string")
def step_impl(self):
    prefix = ''
    assert world.result == prefix, f"expected:'{prefix}', got:'{world.result}'"


@step("log the exception")
def step_impl(self):
    assert world.words is None, f'{world.words}'
