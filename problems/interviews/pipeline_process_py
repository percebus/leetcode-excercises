from datetime import datetime


# FIXME abstract class
class Processor:
    def __init__(self):
        pass

    # FIXME virtual def process()
    def process(self, data):
        raise NotImplementedError('Unimplemented')


class PrinterProcessor(Processor):
    def __init__(self):
        pass

    def process(self, average: float):
        print(average)


class AverageProcessor(Processor):
    def __init__(self, processor: Processor):
        self.next = processor
        self.previous = datetime.utcfromtimestamp(0)
        self.total = 0
        self.count = 0

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
        self.next.process(total / count)


class FilterProcessor(Processor):
    def __init__(self, processor: Processor):
        self.next = processor
        self.previous = datetime.utcfromtimestamp(0)

    def process(self, data: tuple):
        timestamp, temperature = data
        if timestamp < self.previous:
            print('Error')
            return

        self.previous = timestamp
        self.next.process(data)


class ParserProcessor(Processor):
    def __init__(self, processor: Processor):
        self.next = processor
        self.delimeter = ','
        self.mappings = [
            lambda string: datetime.strptime(string, "%Y-%m-%d %H:%M:%S"),
            float
        ]

    def process(self, line: str):
        fields = line.split(self.delimeter)
        try:
            # TODO use map()
            parsed = [
                self.mappings[i](field)
                for i, field in enumerate(fields)
            ]

            self.next.process(parsed)
        except Exception as ex:
            print(ex)


def run():
    data = '''2022-03-25 23:50:00,56
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
