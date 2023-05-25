# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_cng_asph.ui'
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

class Ui_dlgCngAsph(object):
    def setupUi(self, dlgCngAsph):
        if not dlgCngAsph.objectName():
            dlgCngAsph.setObjectName(u"dlgCngAsph")
        dlgCngAsph.resize(566, 444)
        self.btnCngAsph = QPushButton(dlgCngAsph)
        self.btnCngAsph.setObjectName(u"btnCngAsph")
        self.btnCngAsph.setGeometry(QRect(340, 140, 161, 71))
        self.btnDelSpp = QPushButton(dlgCngAsph)
        self.btnDelSpp.setObjectName(u"btnDelSpp")
        self.btnDelSpp.setGeometry(QRect(280, 380, 75, 24))
        self.inpSppAmnt = QLineEdit(dlgCngAsph)
        self.inpSppAmnt.setObjectName(u"inpSppAmnt")
        self.inpSppAmnt.setGeometry(QRect(280, 310, 113, 21))
        self.btnAddSpp = QPushButton(dlgCngAsph)
        self.btnAddSpp.setObjectName(u"btnAddSpp")
        self.btnAddSpp.setGeometry(QRect(280, 340, 75, 24))
        self.lstSpp = QListWidget(dlgCngAsph)
        self.lstSpp.setObjectName(u"lstSpp")
        self.lstSpp.setGeometry(QRect(40, 270, 211, 151))
        self.label_6 = QLabel(dlgCngAsph)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 270, 48, 16))
        self.cmbSpp = QComboBox(dlgCngAsph)
        self.cmbSpp.setObjectName(u"cmbSpp")
        self.cmbSpp.setGeometry(QRect(280, 270, 101, 21))
        self.label_7 = QLabel(dlgCngAsph)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 310, 61, 16))
        self.inpBtm = QLineEdit(dlgCngAsph)
        self.inpBtm.setObjectName(u"inpBtm")
        self.inpBtm.setGeometry(QRect(40, 140, 113, 21))
        self.cmbClm = QComboBox(dlgCngAsph)
        self.cmbClm.setObjectName(u"cmbClm")
        self.cmbClm.setGeometry(QRect(40, 100, 131, 21))
        self.label = QLabel(dlgCngAsph)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 60, 61, 20))
        self.inpBrk = QLineEdit(dlgCngAsph)
        self.inpBrk.setObjectName(u"inpBrk")
        self.inpBrk.setGeometry(QRect(40, 220, 113, 21))
        self.cmbCtg = QComboBox(dlgCngAsph)
        self.cmbCtg.setObjectName(u"cmbCtg")
        self.cmbCtg.setGeometry(QRect(40, 60, 131, 21))
        self.label_2 = QLabel(dlgCngAsph)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 100, 48, 16))
        self.inpName = QLineEdit(dlgCngAsph)
        self.inpName.setObjectName(u"inpName")
        self.inpName.setGeometry(QRect(40, 20, 113, 21))
        self.inpSnd = QLineEdit(dlgCngAsph)
        self.inpSnd.setObjectName(u"inpSnd")
        self.inpSnd.setGeometry(QRect(40, 180, 113, 21))
        self.label_8 = QLabel(dlgCngAsph)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 20, 61, 20))
        self.bntAddClm = QPushButton(dlgCngAsph)
        self.bntAddClm.setObjectName(u"bntAddClm")
        self.bntAddClm.setGeometry(QRect(270, 100, 191, 21))
        self.btnAddCtg = QPushButton(dlgCngAsph)
        self.btnAddCtg.setObjectName(u"btnAddCtg")
        self.btnAddCtg.setGeometry(QRect(270, 60, 191, 21))
        self.btnNewSpp = QPushButton(dlgCngAsph)
        self.btnNewSpp.setObjectName(u"btnNewSpp")
        self.btnNewSpp.setGeometry(QRect(440, 350, 111, 31))
        self.label_10 = QLabel(dlgCngAsph)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(190, 180, 101, 16))
        self.label_11 = QLabel(dlgCngAsph)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 220, 111, 16))
        self.label_3 = QLabel(dlgCngAsph)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 140, 101, 16))

        self.retranslateUi(dlgCngAsph)

        QMetaObject.connectSlotsByName(dlgCngAsph)
    # setupUi

    def retranslateUi(self, dlgCngAsph):
        dlgCngAsph.setWindowTitle(QCoreApplication.translate("dlgCngAsph", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.btnCngAsph.setText(QCoreApplication.translate("dlgCngAsph", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.btnDelSpp.setText(QCoreApplication.translate("dlgCngAsph", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnAddSpp.setText(QCoreApplication.translate("dlgCngAsph", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("dlgCngAsph", u"\u0414\u043e\u0431\u0430\u0432\u043a\u0438", None))
        self.label_7.setText(QCoreApplication.translate("dlgCngAsph", u"\u041a\u043e\u043b - \u0432\u043e", None))
        self.label.setText(QCoreApplication.translate("dlgCngAsph", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("dlgCngAsph", u"\u041a\u043b\u0438\u043c\u0430\u0442", None))
        self.label_8.setText(QCoreApplication.translate("dlgCngAsph", u"\u0422\u0438\u043f", None))
        self.bntAddClm.setText(QCoreApplication.translate("dlgCngAsph", u"\u041d\u043e\u0432\u0430\u044f \u043a\u043b\u0438\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0437\u043e\u043d\u0430", None))
        self.btnAddCtg.setText(QCoreApplication.translate("dlgCngAsph", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.btnNewSpp.setText(QCoreApplication.translate("dlgCngAsph", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0434\u043e\u0431\u0430\u0432\u043a\u0443", None))
        self.label_10.setText(QCoreApplication.translate("dlgCngAsph", u"\u041f\u0435\u0441\u043e\u043a (%\u043c\u0430\u0441\u0441.)", None))
        self.label_11.setText(QCoreApplication.translate("dlgCngAsph", u"\u0429\u0435\u0431\u0435\u043d\u044c (%\u043c\u0430\u0441\u0441.)", None))
        self.label_3.setText(QCoreApplication.translate("dlgCngAsph", u"\u0411\u0438\u0442\u0443\u043c (%\u043c\u0430\u0441\u0441.)", None))
    # retranslateUi

