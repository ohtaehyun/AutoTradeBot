from datetime import datetime
from decimal import Decimal
from time import time
from tracemalloc import start


class Candle(object):
    def __init__(self,open:Decimal, close:Decimal, high:Decimal, low:Decimal,start_time,end_time,trade) -> None:
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.start_time = datetime.fromtimestamp(start_time/1000).strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = datetime.fromtimestamp(end_time/1000).strftime("%Y-%m-%d %H:%M:%S")
        self.trade = trade
        pass

