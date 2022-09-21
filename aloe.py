import subprocess

# FIXME monkeypatch
# SRC https://stackoverflow.com/questions/69515086/beautifulsoup-attributeerror-collections-has-no-attribute-callable
import collections
import collections.abc
collections.Callable = collections.abc.Callable


def aloe():
    subprocess.run(['aloe', '--verbose'])

if __name__ == '__main__':
    aloe()
