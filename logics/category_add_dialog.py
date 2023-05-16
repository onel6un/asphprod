from .validate import Validator
from ui.dialogs.dlg_add_ctg import Ui_DlgAddCtg
from PySide6.QtWidgets import QDialog
from data.models import Category


class CategoryAddDialog(QDialog):
    validator = Validator()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAddCtg()
        self.ui.setupUi(self)

        self.ui.btnAddCtg.clicked.connect(self.on_btnAddClm_click)

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

    def on_btnAddClm_click(self):
        category_name = self.ui.inpName.text()
        durable = self.ui.inpDrb.text()

        if not self.__check_inputs(category_name=category_name,
                                   durable=durable):
            return

        Category.create(category_name=category_name, durable=durable)
        self.accept()
