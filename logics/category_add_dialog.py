from .validate import Validator
from ui.dialogs.dlg_add_ctg import Ui_DlgAddCtg
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QListWidgetItem
from data.models import Category


class CategoryAddDialog(QDialog):
    validator = Validator()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAddCtg()
        self.ui.setupUi(self)

        self.load_category()

        self.ui.btnAddCtg.clicked.connect(self.on_btnAddClm_click)
        self.ui.btnDel.clicked.connect(self.on_btnDel_click)

    def __check_inputs(self, category_name, durable):
        validate_durable = self.validator.input_is_real(
            durable,
            'Нагрузка, должна быть числом'
        )

        validate_name = self.validator.is_str(
            category_name,
            'Название должно быть не пустой строкой!'
        )
        return all((validate_durable, validate_name))

    def __check_item_None(self, item) -> bool:
        return self.validator.is_None_or_empty(
            item,
            'Выберете, позицию для удаления!'
        )

    def on_btnAddClm_click(self):
        category_name = self.ui.inpName.text()
        durable = self.ui.inpDrb.text()

        if not self.__check_inputs(category_name=category_name,
                                   durable=durable):
            return

        Category.create(category_name=category_name, durable=durable)
        self.accept()

    def load_category(self):
        self.ui.lstCtg.clear()
        rows = Category.all()
        for r in rows:
            item = QListWidgetItem(
                f"{r.category_name}-----{r.durable}"
            )
            item.setData(QtCore.Qt.ItemDataRole.UserRole, r)
            self.ui.lstCtg.addItem(item)

    def on_btnDel_click(self):
        item = self.ui.lstCtg.currentItem()

        if self.__check_item_None(item):
            return

        data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        Category.delete(category_id=data.category_id)

        self.load_category()
