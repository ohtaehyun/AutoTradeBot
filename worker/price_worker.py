import time
import ccxt
from PyQt5.QtCore import QThread, pyqtSignal

class PriceWorker(QThread):
    dataSent = pyqtSignal(float)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True
        self.binance = ccxt.binance()

    def run(self):
        while self.alive:
            data  = self.binance.fetch_ticker(self.ticker)
            time.sleep(1)
            self.dataSent.emit(data['open'])

    def close(self):
        self.alive = False