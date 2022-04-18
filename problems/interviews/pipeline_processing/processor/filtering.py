from datetime import datetime
from .exception import ExceptionHandler
from .processor import Processor


class FilterProcessor(Processor):
    # pylint: disable=too-few-public-methods
    def __init__(self, processor: Processor):
        super().__init__()
        self.next = processor
        self.previous = datetime.utcfromtimestamp(0)
    # pylint: enable=too-few-public-methods

    def process(self, data: tuple):
        # pylint: disable=(unused-variable)
        timestamp, temperature = data
        # pylint: enable=(unused-variable)

        assert timestamp >= self.previous, f'entry:{timestamp} is out of order, previous:{self.previous}'
        self.previous = timestamp

        try:
            self.next.process(data)

        except Exception as oException:
            ExceptionHandler.handle(oException)
