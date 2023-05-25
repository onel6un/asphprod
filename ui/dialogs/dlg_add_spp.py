# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_add_spp.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_DlgAddSpp(object):
    def setupUi(self, DlgAddSpp):
        if not DlgAddSpp.objectName():
            DlgAddSpp.setObjectName(u"DlgAddSpp")
        DlgAddSpp.resize(423, 216)
        self.label = QLabel(DlgAddSpp)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 20, 61, 16))
        self.lstSpp = QListWidget(DlgAddSpp)
        self.lstSpp.setObjectName(u"lstSpp")
        self.lstSpp.setGeometry(QRect(20, 21, 211, 181))
        self.inpName = QLineEdit(DlgAddSpp)
        self.inpName.setObjectName(u"inpName")
        self.inpName.setGeometry(QRect(260, 40, 113, 22))
        self.btnAdd = QPushButton(DlgAddSpp)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(260, 70, 93, 28))
        self.btnDel = QPushButton(DlgAddSpp)
        self.btnDel.setObjectName(u"btnDel")
        self.btnDel.setGeometry(QRect(260, 170, 93, 28))

        self.retranslateUi(DlgAddSpp)

        QMetaObject.connectSlotsByName(DlgAddSpp)
    # setupUi

    def retranslateUi(self, DlgAddSpp):
        DlgAddSpp.setWindowTitle(QCoreApplication.translate("DlgAddSpp", u"\u041d\u043e\u0432\u0430\u044f \u0434\u043e\u0431\u0430\u0432\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("DlgAddSpp", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.btnAdd.setText(QCoreApplication.translate("DlgAddSpp", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnDel.setText(QCoreApplication.translate("DlgAddSpp", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

