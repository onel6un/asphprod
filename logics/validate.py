from PySide6.QtWidgets import QDialog
from ui.dialogs.dlg_vld import Ui_VldDlg


class ValidateDlg(QDialog):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_VldDlg()
        self.ui.setupUi(self)

        self.ui.lbVld.setText(msg)

        self.ui.btnOk.clicked.connect(self.on_btnOk_click)

    def on_btnOk_click(self):
        self.accept()


class Validator:
    def is_str(self, string: str, msg='error') -> bool:
        if not isinstance(string, str) or not string:
            self.run_validate_dialog(msg)
            return False
        return True

    def is_None_or_empty(self, value: str | None, msg='error') -> bool:
        if not value or value is None:
            self.run_validate_dialog(msg)
            return True
        return False

    def input_is_real(self, value: str, msg='error') -> bool:
        try:
            float(value)
            return True

        except ValueError:
            self.run_validate_dialog(msg)
            return False

    def input_is_int(self, value: str, msg='error') -> bool:
        try:
            int(value)
            return True

        except ValueError:
            self.run_validate_dialog(msg)
            return False

    def run_validate_dialog(self, msg):
        dialog = ValidateDlg(msg)
        dialog.exec()
