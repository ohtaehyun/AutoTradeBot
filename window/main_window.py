import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from definition import BASE_DIR

from window.key_setting_dialog import KeySettingDialog

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(BASE_DIR + r'\ui\main_window.ui',self)
        self.keySettingButton.clicked.connect(self.set_key_btn_clicked)

    def set_key_btn_clicked(self):
        keySettingDial = KeySettingDialog()
        keySettingDial.exec()
