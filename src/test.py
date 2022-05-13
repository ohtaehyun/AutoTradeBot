
from window.chart_widget import ChartWidget

if __name__ == "__main__":

    import os
    import sys
    from PyQt5.QtWidgets import QApplication

    file_dir = os.path.dirname(__file__)
    print(file_dir)
    sys.path.append(file_dir)

    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    app.exec_()