# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_add_asph.ui'
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

class Ui_dlgAddAsph(object):
    def setupUi(self, dlgAddAsph):
        if not dlgAddAsph.objectName():
            dlgAddAsph.setObjectName(u"dlgAddAsph")
        dlgAddAsph.resize(496, 430)
        self.inpBtm = QLineEdit(dlgAddAsph)
        self.inpBtm.setObjectName(u"inpBtm")
        self.inpBtm.setGeometry(QRect(40, 130, 113, 21))
        self.inpSnd = QLineEdit(dlgAddAsph)
        self.inpSnd.setObjectName(u"inpSnd")
        self.inpSnd.setGeometry(QRect(40, 170, 113, 21))
        self.inpBrk = QLineEdit(dlgAddAsph)
        self.inpBrk.setObjectName(u"inpBrk")
        self.inpBrk.setGeometry(QRect(40, 210, 113, 21))
        self.cmbCtg = QComboBox(dlgAddAsph)
        self.cmbCtg.setObjectName(u"cmbCtg")
        self.cmbCtg.setGeometry(QRect(40, 50, 131, 21))
        self.cmbClm = QComboBox(dlgAddAsph)
        self.cmbClm.setObjectName(u"cmbClm")
        self.cmbClm.setGeometry(QRect(40, 90, 131, 21))
        self.cmbSpp = QComboBox(dlgAddAsph)
        self.cmbSpp.setObjectName(u"cmbSpp")
        self.cmbSpp.setGeometry(QRect(260, 260, 101, 21))
        self.label = QLabel(dlgAddAsph)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 50, 61, 20))
        self.label_2 = QLabel(dlgAddAsph)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 90, 48, 16))
        self.label_3 = QLabel(dlgAddAsph)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 130, 48, 16))
        self.label_4 = QLabel(dlgAddAsph)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 170, 48, 16))
        self.label_5 = QLabel(dlgAddAsph)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 210, 48, 16))
        self.label_6 = QLabel(dlgAddAsph)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 260, 48, 16))
        self.lstSpp = QListWidget(dlgAddAsph)
        self.lstSpp.setObjectName(u"lstSpp")
        self.lstSpp.setGeometry(QRect(20, 260, 211, 151))
        self.inpSppAmnt = QLineEdit(dlgAddAsph)
        self.inpSppAmnt.setObjectName(u"inpSppAmnt")
        self.inpSppAmnt.setGeometry(QRect(260, 300, 113, 21))
        self.label_7 = QLabel(dlgAddAsph)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 300, 61, 16))
        self.btnAddSpp = QPushButton(dlgAddAsph)
        self.btnAddSpp.setObjectName(u"btnAddSpp")
        self.btnAddSpp.setGeometry(QRect(260, 330, 75, 24))
        self.btnDelSpp = QPushButton(dlgAddAsph)
        self.btnDelSpp.setObjectName(u"btnDelSpp")
        self.btnDelSpp.setGeometry(QRect(260, 370, 75, 24))
        self.btnAddAsph = QPushButton(dlgAddAsph)
        self.btnAddAsph.setObjectName(u"btnAddAsph")
        self.btnAddAsph.setGeometry(QRect(310, 140, 161, 71))
        self.inpName = QLineEdit(dlgAddAsph)
        self.inpName.setObjectName(u"inpName")
        self.inpName.setGeometry(QRect(40, 10, 113, 21))
        self.label_8 = QLabel(dlgAddAsph)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 10, 61, 20))
        self.btnAddCtg = QPushButton(dlgAddAsph)
        self.btnAddCtg.setObjectName(u"btnAddCtg")
        self.btnAddCtg.setGeometry(QRect(270, 50, 191, 21))
        self.bntAddClm = QPushButton(dlgAddAsph)
        self.bntAddClm.setObjectName(u"bntAddClm")
        self.bntAddClm.setGeometry(QRect(270, 90, 191, 21))

        self.retranslateUi(dlgAddAsph)

        QMetaObject.connectSlotsByName(dlgAddAsph)
    # setupUi

    def retranslateUi(self, dlgAddAsph):
        dlgAddAsph.setWindowTitle(QCoreApplication.translate("dlgAddAsph", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0441\u0444\u0430\u043b\u0442", None))
        self.label.setText(QCoreApplication.translate("dlgAddAsph", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("dlgAddAsph", u"\u041a\u043b\u0438\u043c\u0430\u0442", None))
        self.label_3.setText(QCoreApplication.translate("dlgAddAsph", u"\u0411\u0438\u0442\u0443\u043c", None))
        self.label_4.setText(QCoreApplication.translate("dlgAddAsph", u"\u041f\u0435\u0441\u043e\u043a", None))
        self.label_5.setText(QCoreApplication.translate("dlgAddAsph", u"\u0429\u0435\u0431\u0435\u043d\u044c", None))
        self.label_6.setText(QCoreApplication.translate("dlgAddAsph", u"\u0414\u043e\u0431\u0430\u0432\u043a\u0438", None))
        self.label_7.setText(QCoreApplication.translate("dlgAddAsph", u"\u041a\u043e\u043b - \u0432\u043e", None))
        self.btnAddSpp.setText(QCoreApplication.translate("dlgAddAsph", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnDelSpp.setText(QCoreApplication.translate("dlgAddAsph", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnAddAsph.setText(QCoreApplication.translate("dlgAddAsph", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0441\u0444\u0430\u043b\u044c\u0442", None))
        self.label_8.setText(QCoreApplication.translate("dlgAddAsph", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.btnAddCtg.setText(QCoreApplication.translate("dlgAddAsph", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.bntAddClm.setText(QCoreApplication.translate("dlgAddAsph", u"\u041d\u043e\u0432\u0430\u044f \u043a\u043b\u0438\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0437\u043e\u043d\u0430", None))
    # retranslateUi

