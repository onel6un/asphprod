from data.models import Asphalt, Climat
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QListWidgetItem
from ui.dialogs.dlg_calc import Ui_DlgCalc
from sqlalchemy.engine import Result

from .validate import Validator


class CalcDialog(QDialog):
    validator = Validator()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_DlgCalc()
        self.ui.setupUi(self)

        self.load_climat()
        self.ui.btnSelect.clicked.connect(self.on_btnSlect_click)
        self.ui.btnCalc.clicked.connect(self.on_btnCalc_click)

    def _check_inputs(self, lenght, widht, height):
        validate_lengh = self.validator.input_is_real(
            lenght,
            "Длина должна быть числом!"
        )
        validate_widht = self.validator.input_is_real(
            widht,
            "Ширина должна быть числом!"
        )
        validate_height = self.validator.input_is_real(
            height,
            "Высота должна быть числом!"
        )
        return all((validate_widht, validate_lengh, validate_height))

    def _check_durable(self, durable):
        return self.validator.input_is_int(
            durable,
            "Нагрузка должна быть целым числом!"
        )

    def _check_item(self, item):
        return not self.validator.is_None_or_empty(
            item,
            "Выберите покрыте для расчета!"
        )

    def __check_empty_result(self, result: Result) -> bool:
        return self.validator.is_None_or_empty(
            result.all(),
            "В прайсе нет подходящего покрытия!"
        )

    def load_climat(self):
        rows = Climat.all()
        for r in rows:
            self.ui.cmbClm.addItem(r.climat_name, r)

    def on_btnSlect_click(self):
        self.ui.lstAsph.clear()
        durable = self.ui.inpTrf.text()

        if not self._check_durable(durable):
            return

        durable = int(durable)

        climat_id = self.ui.cmbClm.currentData().climat_id
        data = Asphalt.filter_add_price(durable=durable, climat_id=climat_id)
        data_freeze = data.freeze()

        self.__check_empty_result(data_freeze())

        for obj in data_freeze():
            item = QListWidgetItem(
                f"{obj.factory_name}    {obj.asphalt_name}    {obj.price}"
            )
            item.setData(QtCore.Qt.ItemDataRole.UserRole, obj)
            self.ui.lstAsph.addItem(item)

    def on_btnCalc_click(self):
        lenght = self.ui.inpLngh.text()
        width = self.ui.inpWdth.text()
        height = self.ui.inpHght.text()

        if not self._check_inputs(lenght=lenght, widht=width, height=height):
            return

        curr_item = self.ui.lstAsph.currentItem()

        if not self._check_item(curr_item):
            return

        curr_asphalt_obj = curr_item.data(QtCore.Qt.ItemDataRole.UserRole)
        price = curr_asphalt_obj.price

        volume = float(lenght) * float(width) * float(height)
        cost = volume * price

        self.ui.lbVolume.setText(f'{volume}')
        self.ui.lbCost.setText(f'{cost}')
