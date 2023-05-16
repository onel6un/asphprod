from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QHeaderView
from ui.dialogs.dlg_asph import Ui_DlgAsph
from data.models import Asphalt, Supplement
from .asphalt_add_dialog import AsphAddDialog
from .asphalt_cng_dialog import AsphCngDialog


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

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation,
                   role: int):
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
            suplements_str = (suplements_str +
                              f"{obj.supplement_name} - {obj.amount}\n")
            lst_obj.append(obj)

        return {
            'str': suplements_str,
            'lst_obj': lst_obj
        }
