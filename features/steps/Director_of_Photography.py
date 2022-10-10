# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world
from problems.meta.coding.puzzles.level1.director_of_photography import getArtisticPhotographCount


@step("a (?P<mask>.+) string 'C', of (?P<length>.+) 'N'")
def step_impl(self, mask, length):
    world.mask = mask
    world.length = int(length)


@step("distance between (?P<minimum>.+) and (?P<maximum>.+)")
def step_impl(self, minimum, maximum):
    world.minimum = int(minimum)
    world.maximum = int(maximum)


@step("I call getArtisticPhotographCount")
def step_impl(self):
    world.result = getArtisticPhotographCount(world.length, world.mask, world.minimum, world.maximum)


@step("I get the number of different artistic (?P<photographs>.+) which could potentially be taken at the set")
def step_impl(self, photographs):
    expected = int(photographs)
    assert world.result == expected, f'expected:{expected}, got:{world.result}'
