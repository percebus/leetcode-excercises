

# FIXME abstract class
class Processor:
    # pylint: disable=too-few-public-methods
    def __init__(self):
        pass
    # pylint: enable=too-few-public-methods

    # FIXME virtual def process()
    def process(self, data):
        raise NotImplementedError('(Sub)Processor.process(data) is Unimplemented')
