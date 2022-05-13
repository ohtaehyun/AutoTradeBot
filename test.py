
from window.chart_widget import ChartWidget
from window.main_window import MainWindow

if __name__ == "__main__":

    import os
    import sys
    from PyQt5.QtWidgets import QApplication

    file_dir = os.path.dirname(__file__)
    sys.path.append(file_dir)

    app = QApplication(sys.argv)
    cw = MainWindow()
    cw.show()
    app.exec_()