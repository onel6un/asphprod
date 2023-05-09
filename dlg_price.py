# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_price.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_dlgPrice(object):
    def setupUi(self, dlgPrice):
        if not dlgPrice.objectName():
            dlgPrice.setObjectName(u"dlgPrice")
        dlgPrice.resize(593, 300)
        self.btnAdd = QPushButton(dlgPrice)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(450, 200, 75, 24))
        self.btnDel = QPushButton(dlgPrice)
        self.btnDel.setObjectName(u"btnDel")
        self.btnDel.setGeometry(QRect(100, 250, 75, 24))
        self.cmbAsph = QComboBox(dlgPrice)
        self.cmbAsph.setObjectName(u"cmbAsph")
        self.cmbAsph.setGeometry(QRect(290, 40, 151, 22))
        self.label_3 = QLabel(dlgPrice)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 160, 48, 16))
        self.btnAddFactory = QPushButton(dlgPrice)
        self.btnAddFactory.setObjectName(u"btnAddFactory")
        self.btnAddFactory.setGeometry(QRect(450, 120, 111, 24))
        self.cmbFactory = QComboBox(dlgPrice)
        self.cmbFactory.setObjectName(u"cmbFactory")
        self.cmbFactory.setGeometry(QRect(290, 120, 151, 22))
        self.inpPrice = QLineEdit(dlgPrice)
        self.inpPrice.setObjectName(u"inpPrice")
        self.inpPrice.setGeometry(QRect(290, 200, 113, 22))
        self.btnAddAsph = QPushButton(dlgPrice)
        self.btnAddAsph.setObjectName(u"btnAddAsph")
        self.btnAddAsph.setGeometry(QRect(450, 40, 111, 24))
        self.label_2 = QLabel(dlgPrice)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 80, 71, 16))
        self.label = QLabel(dlgPrice)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 10, 48, 16))
        self.listPrice = QListWidget(dlgPrice)
        self.listPrice.setObjectName(u"listPrice")
        self.listPrice.setGeometry(QRect(20, 20, 256, 192))

        self.retranslateUi(dlgPrice)

        QMetaObject.connectSlotsByName(dlgPrice)
    # setupUi

    def retranslateUi(self, dlgPrice):
        dlgPrice.setWindowTitle(QCoreApplication.translate("dlgPrice", u"\u041f\u0440\u0430\u0439\u0441", None))
        self.btnAdd.setText(QCoreApplication.translate("dlgPrice", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnDel.setText(QCoreApplication.translate("dlgPrice", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("dlgPrice", u"\u0426\u0435\u043d\u0430", None))
        self.btnAddFactory.setText(QCoreApplication.translate("dlgPrice", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0432\u043e\u0434", None))
        self.btnAddAsph.setText(QCoreApplication.translate("dlgPrice", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0441\u0444\u0430\u043b\u044c\u0442", None))
        self.label_2.setText(QCoreApplication.translate("dlgPrice", u"\u0417\u0430\u0432\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("dlgPrice", u"\u0410\u0441\u0444\u0430\u043b\u044c\u0442", None))
    # retranslateUi

