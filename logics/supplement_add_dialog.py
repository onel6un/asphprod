from ui.dialogs.dlg_add_spp import Ui_DlgAddSpp
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QListWidgetItem
from .validate import Validator
from data.models import Supplement


class SppAddDialog(QDialog):
    validator = Validator()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAddSpp()
        self.ui.setupUi(self)

        self.load_supplement()

        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)
        self.ui.btnDel.clicked.connect(self.on_btnDel_click)

    def _check_item_None(self, item) -> bool:
        return self.validator.is_None_or_empty(
            item,
            'Выберете, позицию для удаления!'
        )

    def _check_empty_name(self, name) -> bool:
        return self.validator.is_None_or_empty(
            name,
            "Поле названия не должно быть пустым!"
        )

    def load_supplement(self):
        self.ui.lstSpp.clear()

        rows = Supplement.all()
        for r in rows:
            item = QListWidgetItem(r.supplement_name)
            item.setData(QtCore.Qt.ItemDataRole.UserRole, r)
            self.ui.lstSpp.addItem(item)

    def on_btnAdd_click(self):
        name = self.ui.inpName.text()

        if self._check_empty_name(name):
            return

        Supplement.create(supplement_name=name)
        self.load_supplement()

    def on_btnDel_click(self):
        item = self.ui.lstSpp.currentItem()

        if self._check_item_None(item):
            return

        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        Supplement.delete(supplement_id=data.supplement_id)

        self.load_supplement()
