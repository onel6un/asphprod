import sys
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,
                               QListWidgetItem, QHeaderView)
from main_window import Ui_MainWindow
from dlg_price import Ui_dlgPrice
from dlg_asph import Ui_DlgAsph
from dlg_add_asph import Ui_dlgAddAsph
from dlg_cng_asph import Ui_dlgCngAsph
from dlg_add_clm import Ui_DlgAddClm
from dlg_add_ctg import Ui_DlgAddCtg
from models import (Price, Asphalt, Factory, Supplement, Category,
                    Climat, AsphSupp)


class ClimatAddDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAddClm()
        self.ui.setupUi(self)

        self.ui.btnAddClm.clicked.connect(self.on_btnAddClm_click)

    def on_btnAddClm_click(self):
        climat_name = self.ui.inpName.text()
        Climat.create(climat_name=climat_name)

        self.accept()


class CategoryAddDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAddCtg()
        self.ui.setupUi(self)

        self.ui.btnAddCtg.clicked.connect(self.on_btnAddClm_click)

    def on_btnAddClm_click(self):
        category_name = self.ui.inpName.text()
        durable = float(self.ui.inpDrb.text())
        Category.create(category_name=category_name, durable=durable)

        self.accept()


class TableAsph(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = []

    def set_items(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 7

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        # if not index.isValid():
        #     return

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            curr_data = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{curr_data[0].asphalt_name}'
            elif col == 1:
                return f'{curr_data[0].bitumen}'
            elif col == 2:
                return f'{curr_data[0].send}'
            elif col == 3:
                return f'{curr_data[0].breakstone}'
            elif col == 4:
                return f'{curr_data[0].category_name}'
            elif col == 5:
                return f'{curr_data[0].climat_name}'
            elif col == 6:
                suplements_str = curr_data[1]['str']
                return suplements_str

        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.items[index.row()]

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: 'Название',
                    1: 'Битум',
                    2: 'Песок',
                    3: 'Щебень',
                    4: 'Класс',
                    5: 'Климат',
                    6: 'Добавки',
                }.get(section)


class AsphDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgAsph()
        self.ui.setupUi(self)

        self.table_model = TableAsph()
        self.ui.tbAsph.setModel(self.table_model)
        self.ui.tbAsph.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )
        self.ui.tbAsph.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        self.load_asphalt()

        self.ui.btnDelAsph.clicked.connect(self.on_btnDelAsph_click)
        self.ui.btnAddAsph.clicked.connect(self.on_btnAddAsph_click)
        self.ui.btnCngAsph.clicked.connect(self.on_btnCngAsph_click)

    def load_asphalt(self):
        rows = Asphalt.all()
        items = []
        for r in rows:
            suplements_dict = self._load_supplement(r.asphalt_id)
            items.append((r, suplements_dict))
        self.table_model.set_items(items)

    def __get_current_data(self):
        item = self.ui.tbAsph.currentIndex()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        return data

    def on_btnDelAsph_click(self):
        data = self.__get_current_data()
        asphalt_id = data[0].asphalt_id
        Asphalt.delete(asphalt_id=asphalt_id)

        self.load_asphalt()

    def on_btnAddAsph_click(self):
        dialog = AsphAddDialog()
        dialog.exec()

        self.load_asphalt()

    def on_btnCngAsph_click(self):
        dialog = AsphCngDialog(instance=self.__get_current_data())
        dialog.exec()

        self.load_asphalt()

    @staticmethod
    def _load_supplement(asphalt_id) -> dict:
        suplements_obj = Supplement.filter(asphalt_id=asphalt_id)

        suplements_str = ''
        lst_obj = []
        for obj in suplements_obj:
            suplements_str = suplements_str + f"{obj.supplement_name} - {obj.amount}\n"
            lst_obj.append(obj)

        return {
            'str': suplements_str,
            'lst_obj': lst_obj
        }


class AsphAddDialog(QDialog):
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
        rows = Supplement.all()
        for r in rows:
            self.ui.cmbSpp.addItem(r.supplement_name, r)

    def on_btnAddAsph_click(self):
        asph_name = self.ui.inpName.text()
        climat_id = self.ui.cmbClm.currentData().climat_id
        category_id = self.ui.cmbCtg.currentData().category_id
        amount_btm = float(self.ui.inpBtm.text())
        amount_snd = float(self.ui.inpSnd.text())
        amount_brk = float(self.ui.inpBrk.text())

        Asphalt.create(asphalt_name=asph_name, climat_id=climat_id,
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


class AsphCngDialog(AsphAddDialog):
    def __init__(self, instance, *args, **kwargs):
        super(AsphAddDialog, self).__init__(*args, **kwargs)
        self.ui = Ui_dlgCngAsph()
        self.ui.setupUi(self)

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
        amount_btm = float(self.ui.inpBtm.text())
        amount_snd = float(self.ui.inpSnd.text())
        amount_brk = float(self.ui.inpBrk.text())

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

                AsphSupp.create(asphalt_id=asphalt_id, supplement_id=spp_id,
                                amount=amount_spp)

        self.accept()


class PriceDialog(QDialog):
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


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnPrice.clicked.connect(self.on_btnPrice_click)
        self.ui.btnAsph.clicked.connect(self.on_btnAsph_click)

    def on_btnPrice_click(self):
        dialog = PriceDialog()
        dialog.exec()

    def on_btnAsph_click(self):
        dialog = AsphDialog()
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
