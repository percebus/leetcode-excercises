from datetime import datetime
from .exception import ExceptionHandler
from .processor import Processor


class AverageProcessor(Processor):
    # pylint: disable=too-few-public-methods
    def __init__(self, processor: Processor):
        super().__init__()
        self.next = processor
        self.previous = datetime.utcfromtimestamp(0)
        self.total = 0
        self.count = 0
    # pylint: enable=too-few-public-methods

    def process(self, data: tuple):
        timestamp, temperature = data
        if self.previous.date() == timestamp.date():
            self.total += temperature
            self.count += 1
            return

        self.previous = timestamp
        self.total = temperature
        self.count = 1
        total = self.total
        count = self.count

        try:
            self.next.process(total / count)

        except Exception as oException:
            ExceptionHandler.handle(oException)
