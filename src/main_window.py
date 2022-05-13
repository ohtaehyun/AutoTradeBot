import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from src.key_setting_dialog import KeySettingDialog

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
        uic.loadUi(BASE_DIR + r'\main_window.ui',self)
        self.keySettingButton.clicked.connect(self.set_key_btn_clicked)

    def set_key_btn_clicked(self):
        keySettingDial = KeySettingDialog()
        keySettingDial.exec()
