import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from problems.interviews.pipeline_processing.processor.average import AverageProcessor
from problems.interviews.pipeline_processing.processor.filtering import FilterProcessor
from problems.interviews.pipeline_processing.processor.parser import ParserProcessor
from problems.interviews.pipeline_processing.processor.printer import PrinterProcessor


def run():  # FIXME move data to csv
    data = '''2022-03-25 23:50:00,56
2022-03-24 23:50:00,56
2022-03-25 23:50:15,56
2022-03-25 23:50:30,54
2022-03-25 23:50:45,56
2022-03-25 23:51:00,56
2022-03-25 23:51:15,56
2022-03-25 23:51:30,55
2022-03-25 23:51:45,53
2022-03-25 23:52:00,54
2022-03-26 23:52:15,52'''

    # CSV > Parse > Filter (Validate) > Average (Aggregator) > Result
    oProcessor = PrinterProcessor()
    oProcessor = AverageProcessor(oProcessor)
    oProcessor = FilterProcessor(oProcessor)
    oProcessor = ParserProcessor(oProcessor)

    for line in data.split('\n'):
        oProcessor.process(line)


if __name__ == '__main__':
    run()
