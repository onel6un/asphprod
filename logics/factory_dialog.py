from data.models import Factory
from PySide6.QtWidgets import QDialog
from ui.dialogs.dlg_add_factory import Ui_AddFactory


class FactoryDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_AddFactory()
        self.ui.setupUi(self)

        self.ui.btnAddFct.clicked.connect(self.on_btnAddFct_click)

    def on_btnAddFct_click(self):
        factory_name = self.ui.inpName.text()
        Factory.create(factory_name=factory_name)

        self.accept()
