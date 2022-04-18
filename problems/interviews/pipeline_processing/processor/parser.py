from datetime import datetime
from .exception import ExceptionHandler
from .processor import Processor


class ParserProcessor(Processor):
    # pylint: disable=too-few-public-methods
    def __init__(self, processor: Processor):
        super().__init__()
        self.next = processor
        self.delimeter = ','
        self.mappings = [
            lambda string: datetime.strptime(string, "%Y-%m-%d %H:%M:%S"),
            float
        ]

    # pylint: enable=too-few-public-methods

    def process(self, data: str):
        fields = data.split(self.delimeter)
        try:
            # TODO use map()
            parsed = [
                self.mappings[i](field)
                for i, field in enumerate(fields)
            ]
        except Exception as oException:
            ExceptionHandler.handle(oException)

        try:
            self.next.process(parsed)

        except AssertionError as oException:
            ExceptionHandler.handle(oException)

        except Exception as oException:
            ExceptionHandler.handle(oException)
