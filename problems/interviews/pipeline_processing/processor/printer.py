from .processor import Processor


# pylint: disable=too-few-public-methods
class PrinterProcessor(Processor):

    def process(self, data: float):
        print(data)
# pylint: enable=too-few-public-methods
