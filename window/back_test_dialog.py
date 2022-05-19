from decimal import Decimal
import math
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from algorithm.khs001 import KHS001
from definition import BASE_DIR
from model.candle import Candle
from singleton.binanceInfoSingleton import BinanceInfoSingleton


class BackTestDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(BASE_DIR + r"\ui\back_test_dialog.ui",self)
        self.btProgressBar.setValue(0)
        self.btCloseBtn.clicked.connect(self.close)
        self.btStartBtn.clicked.connect(self.back_test_start)

    def back_test_start(self):
        try:
            self.client = BinanceInfoSingleton.instance().get_client()
            self.btProgressBar.setValue(1)
            data = self.client.get_historical_klines(
                symbol = "BTCUSDT",
                interval = self.timeCombo.currentText(),
                start_str = self.btStartDate.date().toString(),
                limit = 1000
            )
            self.algo = KHS001()
            length = len(data)
            for idx, row in enumerate(data):
                candle = Candle(Decimal(row[1]),Decimal(row[4]),Decimal(row[2]),Decimal(row[3]),row[0],row[6],row[8])
                self.algo.append_5m(candle)
                self.btProgressBar.setValue(math.floor(idx/length))
        except Exception as e:
            print(e)
