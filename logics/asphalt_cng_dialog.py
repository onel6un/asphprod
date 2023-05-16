from data.models import Asphalt, AsphSupp
from PySide6 import QtCore
from PySide6.QtWidgets import QListWidgetItem
from ui.dialogs.dlg_cng_asph import Ui_dlgCngAsph

from .validate import Validator
from .asphalt_add_dialog import AsphAddDialog


class AsphCngDialog(AsphAddDialog):
    validator = Validator()

    def __init__(self, instance, *args, **kwargs):
        super(AsphAddDialog, self).__init__(*args, **kwargs)
        self.ui = Ui_dlgCngAsph()
        self.ui.setupUi(self)

        self.__check_instance(instance)
        self.obj_instance = instance

        self.load_category()
        self.load_climat()
        self.load_supplement()
        self.load_inputs()
        self.load_supplement_in_lstSpp()

        self.ui.btnAddSpp.clicked.connect(self.on_btnAddSpp_click)
        self.ui.btnDelSpp.clicked.connect(self.on_btnDelSpp_click)
        self.ui.btnCngAsph.clicked.connect(self.on_btnCngAsph_click)
        self.ui.bntAddClm.clicked.connect(self.on_btnAddClm_click)
        self.ui.btnAddCtg.clicked.connect(self.on_btnAddCtg_click)

    def __check_instance(self, instance) -> None:
        if self.validator.is_None_or_empty(
            instance,
            "Выберите, позицию которую нужно изменить!"
        ):
            self.accept()

    def load_category(self):
        super().load_category()
        asph_instance = self.obj_instance[0]
        ctg_name = asph_instance.category_name
        inst_indx = self.ui.cmbCtg.findText(ctg_name)
        self.ui.cmbCtg.setCurrentIndex(inst_indx)

    def load_climat(self):
        super().load_climat()
        asph_instance = self.obj_instance[0]
        clm_name = asph_instance.climat_name
        inst_indx = self.ui.cmbClm.findText(clm_name)
        self.ui.cmbClm.setCurrentIndex(inst_indx)

    def load_supplement_in_lstSpp(self):
        supp_dict_instance = self.obj_instance[1]
        supp_objs = supp_dict_instance.get("lst_obj")
        for obj in supp_objs:
            supp_name = obj.supplement_name
            supp_amount = obj.amount
            item = QListWidgetItem(
                f"{supp_name} - {supp_amount}"
            )
            item.setData(QtCore.Qt.ItemDataRole.UserRole, (obj, supp_amount))

            self.ui.lstSpp.addItem(item)

    def load_inputs(self):
        asph_instance = self.obj_instance[0]
        self.ui.inpBrk.setText(str(asph_instance.breakstone))
        self.ui.inpName.setText(asph_instance.asphalt_name)
        self.ui.inpBtm.setText(str(asph_instance.bitumen))
        self.ui.inpSnd.setText(str(asph_instance.send))

    def on_btnCngAsph_click(self):
        asph_instance = self.obj_instance[0]

        asphalt_id = asph_instance.asphalt_id
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

        Asphalt.update(asphalt_id=asphalt_id, climat_id=climat_id,
                       category_id=category_id, bitumen=amount_btm,
                       send=amount_snd, breakstone=amount_brk,
                       asphalt_name=asphalt_name)

        Asphalt.del_supp(asphalt_id=asphalt_id)

        count_spp = self.ui.lstSpp.count()
        if count_spp > 0:
            for i in range(count_spp):

                item_spp = self.ui.lstSpp.item(i)
                data_spp = item_spp.data(QtCore.Qt.ItemDataRole.UserRole)
                amount_spp = data_spp[1]
                spp_id = data_spp[0].supplement_id

                AsphSupp.create(asphalt_id=asphalt_id,
                                supplement_id=spp_id, amount=amount_spp)

        self.accept()
