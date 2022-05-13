import string
import time
import ccxt
from PyQt5.QtCore import QThread, pyqtSignal

from singleton.binanceInfoSingleton import BinanceInfoSingleton

class PriceWorker(QThread):
    dataSent = pyqtSignal(float)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True
        self.binance = BinanceInfoSingleton.instance().get_client()

    def run(self):
        while self.alive:
            if(self.binance is None):
                self.binance = BinanceInfoSingleton.instance().get_client()

            if(self.binance is not None):
                data  = self.binance.get_symbol_ticker(symbol=self.ticker)
                self.dataSent.emit(float(data['price']))
          
            time.sleep(1)

    def close(self):
        self.alive = False