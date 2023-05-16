from .validate import Validator
from ui.dialogs.dlg_add_clm import Ui_DlgAddClm
from PySide6.QtWidgets import QDialog
from data.models import Climat


class ClimatAddDialog(QDialog):
    validator = Validator()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAddClm()
        self.ui.setupUi(self)

        self.ui.btnAddClm.clicked.connect(self.on_btnAddClm_click)

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
