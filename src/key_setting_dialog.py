import os
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

from src.binanceInfoSingleton import BinanceInfoSingleton

class KeySettingDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
        uic.loadUi(BASE_DIR + r"\key_setting_dialog.ui",self)
        self.keyEditBtn.clicked.connect(self.set_binance_key)

    def set_binance_key(self):
        binance_info = BinanceInfoSingleton.instance()
        binance_info.set_public(self.pubKeyEdit.text())
        binance_info.set_private(self.privKeyEdit.text())

