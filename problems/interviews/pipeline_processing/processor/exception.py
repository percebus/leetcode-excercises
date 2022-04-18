

# TODO? inherit from Process and treat it like another processor?
class ExceptionHandler:
    # pylint: disable=too-few-public-methods
    def __init__(self):
        pass
    # pylint: enable=too-few-public-methods

    @classmethod
    def handle(cls, exception: Exception):
        print(exception)
