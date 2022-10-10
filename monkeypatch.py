# FIXME monkeypatch
# SRC https://stackoverflow.com/questions/69515086/beautifulsoup-attributeerror-collections-has-no-attribute-callable
import collections
import collections.abc
collections.Callable = collections.abc.Callable

import aloe
from aloe import step, world
