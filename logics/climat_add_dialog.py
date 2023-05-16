from .validate import Validator
from ui.dialogs.dlg_add_clm import Ui_DlgAddClm
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QListWidgetItem
from data.models import Climat


class ClimatAddDialog(QDialog):
    validator = Validator()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAddClm()
        self.ui.setupUi(self)

        self.load_climat()

        self.ui.btnAddClm.clicked.connect(self.on_btnAddClm_click)
        self.ui.btnDel.clicked.connect(self.on_btnDel_click)

    def __check_item_None(self, item) -> bool:
        return self.validator.is_None_or_empty(
            item,
            'Выберете, позицию для удаления!'
        )

    def __check_inputs(self, climat_name):
        validate_name = self.validator.is_str(
            climat_name,
            'Название должно быть не пустой строкой!'
        )
        return validate_name

    def on_btnAddClm_click(self):
        climat_name = self.ui.inpName.text()

        if not self.__check_inputs(climat_name):
            return

        Climat.create(climat_name=climat_name)
        self.accept()

    def load_climat(self):
        self.ui.lstClm.clear()
        rows = Climat.all()
        for r in rows:
            item = QListWidgetItem(
                f"{r.climat_name}"
            )
            item.setData(QtCore.Qt.ItemDataRole.UserRole, r)
            self.ui.lstClm.addItem(item)

    def on_btnDel_click(self):
        item = self.ui.lstClm.currentItem()

        if self.__check_item_None(item):
            return

        data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        Climat.delete(climat_id=data.climat_id)

        self.load_climat()
