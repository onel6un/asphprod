from data.models import Asphalt, AsphSupp, Category, Climat, Supplement
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QListWidgetItem
from ui.dialogs.dlg_add_asph import Ui_dlgAddAsph


from .category_add_dialog import CategoryAddDialog
from .climat_add_dialog import ClimatAddDialog
from .supplement_add_dialog import SppAddDialog
from .validate import Validator


class AsphAddDialog(QDialog):
    validator = Validator()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_dlgAddAsph()
        self.ui.setupUi(self)

        self.load_category()
        self.load_climat()
        self.load_supplement()

        self.ui.btnAddSpp.clicked.connect(self.on_btnAddSpp_click)
        self.ui.btnDelSpp.clicked.connect(self.on_btnDelSpp_click)
        self.ui.btnAddAsph.clicked.connect(self.on_btnAddAsph_click)
        self.ui.bntAddClm.clicked.connect(self.on_btnAddClm_click)
        self.ui.btnAddCtg.clicked.connect(self.on_btnAddCtg_click)
        self.ui.btnNewSpp.clicked.connect(self.on_btnNewSpp_click)

    def _check_inputs(self, asphalt_name, amount_btm, amount_snd, amount_brk):
        validate_name = self.validator.is_str(
            asphalt_name,
            "Название афсфальта, должно быть не пустой строкой!"
        )
        validate_btm = self.validator.input_is_real(
            amount_btm,
            "Долевая часть битума, должна быть числом!"
        )
        validate_snd = self.validator.input_is_real(
            amount_snd,
            "Долевая часть песка, должна быть числом!"
        )
        validate_brk = self.validator.input_is_real(
            amount_brk,
            "Долевая часть щебня, должна быть числом!"
        )
        return all((validate_name, validate_btm, validate_snd, validate_brk))

    def load_category(self):
        self.ui.cmbCtg.clear()
        rows = Category.all()
        for r in rows:
            self.ui.cmbCtg.addItem(r.category_name, r)

    def load_climat(self):
        self.ui.cmbClm.clear()
        rows = Climat.all()
        for r in rows:
            self.ui.cmbClm.addItem(r.climat_name, r)

    def load_supplement(self):
        self.ui.cmbSpp.clear()
        
        rows = Supplement.all()
        for r in rows:
            self.ui.cmbSpp.addItem(r.supplement_name, r)

    def on_btnAddAsph_click(self):
        asphalt_name = self.ui.inpName.text()
        climat_id = self.ui.cmbClm.currentData().climat_id
        category_id = self.ui.cmbCtg.currentData().category_id
        amount_btm = self.ui.inpBtm.text()
        amount_snd = self.ui.inpSnd.text()
        amount_brk = self.ui.inpBrk.text()

        if not self._check_inputs(
            asphalt_name=asphalt_name,
            amount_btm=amount_btm,
            amount_brk=amount_brk,
            amount_snd=amount_snd
        ):
            return

        Asphalt.create(asphalt_name=asphalt_name, climat_id=climat_id,
                       category_id=category_id, bitumen=amount_btm,
                       send=amount_snd, breakstone=amount_brk)

        last_asph_obj = Asphalt.last()
        last_asph_id = last_asph_obj.__next__().asphalt_id

        count_spp = self.ui.lstSpp.count()
        if count_spp > 0:
            for i in range(count_spp):

                item_spp = self.ui.lstSpp.item(i)
                data_spp = item_spp.data(QtCore.Qt.ItemDataRole.UserRole)

                amount_spp = data_spp[1]
                spp_id = data_spp[0].supplement_id

                AsphSupp.create(asphalt_id=last_asph_id, supplement_id=spp_id,
                                amount=amount_spp)

        self.accept()

    def on_btnAddSpp_click(self):
        spp_data = self.ui.cmbSpp.currentData()
        spp_amount = int(self.ui.inpSppAmnt.text())
        item = QListWidgetItem(
                f"{spp_data.supplement_name} - {spp_amount}"
            )
        item.setData(QtCore.Qt.ItemDataRole.UserRole, (spp_data, spp_amount))
        self.ui.lstSpp.addItem(item)

    def on_btnDelSpp_click(self):
        indx_item = self.ui.lstSpp.currentRow()
        self.ui.lstSpp.takeItem(indx_item)

    def on_btnAddClm_click(self):
        dialog = ClimatAddDialog()
        dialog.exec()

        self.load_climat()

    def on_btnAddCtg_click(self):
        dialog = CategoryAddDialog()
        dialog.exec()

        self.load_category()

    def on_btnNewSpp_click(self):
        dialog = SppAddDialog()
        dialog.exec()

        self.load_supplement()
