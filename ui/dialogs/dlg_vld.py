# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_vld.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_VldDlg(object):
    def setupUi(self, VldDlg):
        if not VldDlg.objectName():
            VldDlg.setObjectName(u"VldDlg")
        VldDlg.resize(424, 82)
        self.lbVld = QLabel(VldDlg)
        self.lbVld.setObjectName(u"lbVld")
        self.lbVld.setGeometry(QRect(30, 10, 371, 31))
        self.btnOk = QPushButton(VldDlg)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setGeometry(QRect(180, 50, 75, 24))

        self.retranslateUi(VldDlg)

        QMetaObject.connectSlotsByName(VldDlg)
    # setupUi

    def retranslateUi(self, VldDlg):
        VldDlg.setWindowTitle(QCoreApplication.translate("VldDlg", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435!", None))
        self.lbVld.setText("")
        self.btnOk.setText(QCoreApplication.translate("VldDlg", u"Ok!", None))
    # retranslateUi

