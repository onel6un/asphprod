from data.models import Asphalt, Factory, Price
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QListWidgetItem
from ui.dialogs.dlg_price import Ui_dlgPrice

from .validate import Validator
from .factory_dialog import FactoryDialog
from .asphalt_dialog import AsphDialog


class PriceDialog(QDialog):
    validator = Validator()

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
        self.ui.btnAddFactory.clicked.connect(self.on_btnAddFactory_click)

    def _check_price(self, price):
        return self.validator.input_is_real(
            price,
            "Цена должна быть числом!"
        )

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

        if not self._check_price(price):
            return

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
        self.ui.cmbAsph.clear()
        dialog = AsphDialog()
        dialog.exec()

        self.load_asphalt()

    def on_btnAddFactory_click(self):
        self.ui.cmbFactory.clear()
        dialog = FactoryDialog()
        dialog.exec()

        self.load_factory()
