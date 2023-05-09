import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,
                               QListWidgetItem, QHeaderView)
from main_window import Ui_MainWindow
from dlg_price import Ui_dlgPrice
from dlg_asph import Ui_DlgAsph

from models import Price, Asphalt, Factory, Supplement


class TableAsph(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = []

    def set_items(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 7

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        # if not index.isValid():
        #     return

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            curr_data = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{curr_data[0].asphalt_name}'
            elif col == 1:
                return f'{curr_data[0].bitumen}'
            elif col == 2:
                return f'{curr_data[0].send}'
            elif col == 3:
                return f'{curr_data[0].breakstone}'
            elif col == 4:
                return f'{curr_data[0].category_name}'
            elif col == 5:
                return f'{curr_data[0].climat_name}'
            elif col == 6:
                suplements_str = curr_data[1]['str']
                return suplements_str

        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.items[index.row()]

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Название',
                    1: 'Битум',
                    2: 'Песок',
                    3: 'Щебень',
                    4: 'Класс',
                    5: 'Климат',
                    6: 'Добавки',
                }.get(section)


class AsphDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAsph()
        self.ui.setupUi(self)

        self.table_model = TableAsph()
        self.ui.tbAsph.setModel(self.table_model)
        self.ui.tbAsph.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        self.ui.tbAsph.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        self.load_asphalt()

        self.ui.btnDelAsph.clicked.connect(self.on_btnDelAsph_click)
        self.ui.btnAddAsph.clicked.connect(self.on_btnAddAsph_click)

    def load_asphalt(self):
        rows = Asphalt.all()
        items = []
        for r in rows:
            suplements_dict = self._load_supplement(r.asphalt_id)
            items.append((r, suplements_dict))
        self.table_model.set_items(items)

    def on_btnDelAsph_click(self):
        item = self.ui.tbAsph.currentIndex()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        asphalt_id = data[0].asphalt_id
        Asphalt.delete(asphalt_id=asphalt_id)

        self.load_asphalt()
    
    def on_btnAddAsph_click(self):
        pass


    @staticmethod
    def _load_supplement(asphalt_id) -> dict:
        suplements_obj = Supplement.filter(asphalt_id=asphalt_id)
        suplements_str = "\n".join(
            list(
                map(
                    lambda x: f"{x.supplement_name} - {x.amount}",
                    suplements_obj
                )
            )
        )
        return {
            'str': suplements_str,
            'objs': suplements_obj
        }


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
        self.ui.btnAddAsph.clicked.connect(self.on_btnAddAsph_click)

    def load_price(self):
        self.ui.listPrice.clear()
        rows = Price.all()
        for r in rows:
            item = QListWidgetItem(
                f"{r.factory_name} {r.asphalt_name} {r.price}"
            )
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

    def on_btnAddAsph_click(self):
        dialog = AsphDialog()
        dialog.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnPrice.clicked.connect(self.on_btnPrice_click)
        self.ui.btnAsph.clicked.connect(self.on_btnAsph_click)

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
