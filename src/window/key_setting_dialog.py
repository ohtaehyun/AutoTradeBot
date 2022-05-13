from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

from singleton.binanceInfoSingleton import BinanceInfoSingleton

class KeySettingDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("./src/ui/key_setting_dialog.ui",self)
        self.keyEditBtn.clicked.connect(self.set_binance_key)

    def set_binance_key(self):
        binance_info = BinanceInfoSingleton.instance()
        binance_info.set_public(self.pubKeyEdit.text())
        binance_info.set_private(self.privKeyEdit.text())

