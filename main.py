import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,
                               QListWidgetItem)
from main_window import Ui_MainWindow
from dlg_price import Ui_dlgPrice
from dlg_asph import Ui_DlgAsph

from models import Price, Asphalt, Factory, Supplement


class AsphDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAsph()
        self.ui.setupUi(self)

        self.load_asphalt()

    def load_asphalt(self):
        self.ui.listAsph.clear()
        rows = Asphalt.all()
        for r in rows:
            suplements_obj = Supplement.filter(asphalt_id=r.asphalt_id)
            suplemnts_str = "\n".join(list(map(lambda x: x.supplement_name, suplements_obj)))
            print(suplemnts_str)
            item = QListWidgetItem(f"{r.asphalt_name} {r.send} {r.breakstone} {r.bitumen}")
            item.setData(QtCore.Qt.ItemDataRole.UserRole, r)
            self.ui.listAsph.addItem(item)


class PriceDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_dlgPrice()
        self.ui.setupUi(self)

        self.load_factory()
        self.load_asphalt()
        self.load_price()

        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)
        self.ui.btnDel.clicked.connect(self.on_btnDel_click)

    def load_price(self):
        self.ui.listPrice.clear()
        rows = Price.all()
        for r in rows:
            item = QListWidgetItem(f"{r.factory_name} {r.asphalt_name} {r.price}")
            item.setData(QtCore.Qt.ItemDataRole.UserRole, r)
            self.ui.listPrice.addItem(item)

    def load_asphalt(self):
        rows = Asphalt.all()
        for r in rows:
            self.ui.cmbAsph.addItem(r.asphalt_name, r)

    def load_factory(self):
        rows = Factory.all()
        for r in rows:
            self.ui.cmbFactory.addItem(r.factory_name, r)

    def on_btnAdd_click(self):
        factory_id = self.ui.cmbFactory.currentData().factory_id
        asphalt_id = self.ui.cmbAsph.currentData().asphalt_id
        price = self.ui.inpPrice.text()

        Price.create(
            factory_id=factory_id,
            asphalt_id=asphalt_id,
            price=price
        )

        self.load_price()

    def on_btnDel_click(self):
        item = self.ui.listPrice.currentItem()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        Price.delete(price_id=data.price_id)

        self.load_price()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnPrice.clicked.connect(self.on_btnPrice_click)

    def on_btnPrice_click(self):
        dialog = PriceDialog()
        dialog.exec()

    def on_btnAsph_click(self):
        dialog = AsphDialog()
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
