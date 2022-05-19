import time
from PyQt5.QtCore import QThread, pyqtSignal
from binance.client import Client
from singleton.binanceInfoSingleton import BinanceInfoSingleton

class PriceWorker(QThread):
    dataSent = pyqtSignal(float)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True
        self.binance = Client('','')
    def run(self):
        while self.alive:
            data  = self.binance.get_symbol_ticker(symbol=self.ticker)
            self.dataSent.emit(float(data['price']))
            time.sleep(1)

    def close(self):
        self.alive = False