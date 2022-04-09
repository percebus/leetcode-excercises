# [LeetCode.com](LeetCode.com) excercises

LeetCode.com excercises

## Requisites

* `python@3.X` (tested with python 3.6 - 3.10)

## Issues

### suite.py

Monkeypatch nose/suite.py, by adding

[AttributeError 'collections' has no attribute 'Callable'](https://stackoverflow.com/questions/69515086/beautifulsoup-attributeerror-collections-has-no-attribute-callable)
```python
collections.Callable = collections.abc.Callable
```
