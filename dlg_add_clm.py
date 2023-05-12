# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_add_clm.ui'
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

class Ui_DlgAddClm(object):
    def setupUi(self, DlgAddClm):
        if not DlgAddClm.objectName():
            DlgAddClm.setObjectName(u"DlgAddClm")
        DlgAddClm.resize(260, 110)
        self.inpName = QLineEdit(DlgAddClm)
        self.inpName.setObjectName(u"inpName")
        self.inpName.setGeometry(QRect(20, 20, 113, 22))
        self.label = QLabel(DlgAddClm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 51, 21))
        self.btnAddClm = QPushButton(DlgAddClm)
        self.btnAddClm.setObjectName(u"btnAddClm")
        self.btnAddClm.setGeometry(QRect(70, 70, 111, 21))

        self.retranslateUi(DlgAddClm)

        QMetaObject.connectSlotsByName(DlgAddClm)
    # setupUi

    def retranslateUi(self, DlgAddClm):
        DlgAddClm.setWindowTitle(QCoreApplication.translate("DlgAddClm", u"\u041d\u043e\u0432\u0430\u044f \u043a\u043b\u0438\u043c\u0430\u0442 \u0437\u043e\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("DlgAddClm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.btnAddClm.setText(QCoreApplication.translate("DlgAddClm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

