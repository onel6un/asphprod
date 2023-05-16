# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_add_ctg.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_DlgAddCtg(object):
    def setupUi(self, DlgAddCtg):
        if not DlgAddCtg.objectName():
            DlgAddCtg.setObjectName(u"DlgAddCtg")
        DlgAddCtg.resize(307, 137)
        self.btnAddCtg = QPushButton(DlgAddCtg)
        self.btnAddCtg.setObjectName(u"btnAddCtg")
        self.btnAddCtg.setGeometry(QRect(80, 100, 111, 21))
        self.label = QLabel(DlgAddCtg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 20, 51, 21))
        self.inpName = QLineEdit(DlgAddCtg)
        self.inpName.setObjectName(u"inpName")
        self.inpName.setGeometry(QRect(30, 20, 113, 22))
        self.inpDrb = QLineEdit(DlgAddCtg)
        self.inpDrb.setObjectName(u"inpDrb")
        self.inpDrb.setGeometry(QRect(30, 60, 113, 22))
        self.label_2 = QLabel(DlgAddCtg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 60, 51, 21))

        self.retranslateUi(DlgAddCtg)

        QMetaObject.connectSlotsByName(DlgAddCtg)
    # setupUi

    def retranslateUi(self, DlgAddCtg):
        DlgAddCtg.setWindowTitle(QCoreApplication.translate("DlgAddCtg", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.btnAddCtg.setText(QCoreApplication.translate("DlgAddCtg", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.label.setText(QCoreApplication.translate("DlgAddCtg", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.inpDrb.setText("")
        self.label_2.setText(QCoreApplication.translate("DlgAddCtg", u"\u041d\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
    # retranslateUi

