import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.main_window.main_window import Ui_MainWindow
from logics.asphalt_dialog import AsphDialog
from logics.calc_dialog import CalcDialog
from logics.price_dialog import PriceDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnPrice.clicked.connect(self.on_btnPrice_click)
        self.ui.btnAsph.clicked.connect(self.on_btnAsph_click)
        self.ui.btnCalc.clicked.connect(self.on_btnCalc_click)

    def on_btnPrice_click(self):
        dialog = PriceDialog()
        dialog.exec()

    def on_btnAsph_click(self):
        dialog = AsphDialog()
        dialog.exec()

    def on_btnCalc_click(self):
        dialog = CalcDialog()
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
