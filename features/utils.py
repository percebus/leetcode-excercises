
def assert_is_in_range(x, constraint):
    minimum = constraint['min']
    maximum = constraint['max']
    assert x >= minimum, "min:{expected}, got:{actual}".format(expected=minimum, actual=x)
    assert x <= maximum, "max:{expected}, got:{actual}".format(expected=maximum, actual=x)
