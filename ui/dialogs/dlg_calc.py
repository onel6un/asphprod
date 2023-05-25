# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_calc.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_DlgCalc(object):
    def setupUi(self, DlgCalc):
        if not DlgCalc.objectName():
            DlgCalc.setObjectName(u"DlgCalc")
        DlgCalc.resize(671, 487)
        self.lstAsph = QListWidget(DlgCalc)
        self.lstAsph.setObjectName(u"lstAsph")
        self.lstAsph.setGeometry(QRect(30, 230, 351, 141))
        self.btnCalc = QPushButton(DlgCalc)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(450, 420, 141, 24))
        self.inpTrf = QLineEdit(DlgCalc)
        self.inpTrf.setObjectName(u"inpTrf")
        self.inpTrf.setGeometry(QRect(30, 80, 201, 21))
        self.cmbClm = QComboBox(DlgCalc)
        self.cmbClm.setObjectName(u"cmbClm")
        self.cmbClm.setGeometry(QRect(30, 20, 201, 22))
        self.btnSelect = QPushButton(DlgCalc)
        self.btnSelect.setObjectName(u"btnSelect")
        self.btnSelect.setGeometry(QRect(30, 140, 241, 21))
        self.inpHght = QLineEdit(DlgCalc)
        self.inpHght.setObjectName(u"inpHght")
        self.inpHght.setGeometry(QRect(300, 420, 101, 21))
        self.inpWdth = QLineEdit(DlgCalc)
        self.inpWdth.setObjectName(u"inpWdth")
        self.inpWdth.setGeometry(QRect(170, 420, 101, 21))
        self.inpLngh = QLineEdit(DlgCalc)
        self.inpLngh.setObjectName(u"inpLngh")
        self.inpLngh.setGeometry(QRect(40, 420, 101, 21))
        self.label = QLabel(DlgCalc)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 20, 101, 16))
        self.label_2 = QLabel(DlgCalc)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 390, 91, 16))
        self.label_3 = QLabel(DlgCalc)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 80, 81, 16))
        self.label_4 = QLabel(DlgCalc)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 390, 91, 16))
        self.label_5 = QLabel(DlgCalc)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 390, 81, 16))
        self.lbVolume = QLabel(DlgCalc)
        self.lbVolume.setObjectName(u"lbVolume")
        self.lbVolume.setGeometry(QRect(510, 20, 131, 21))
        self.label_6 = QLabel(DlgCalc)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(407, 20, 91, 20))
        self.label_7 = QLabel(DlgCalc)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(407, 50, 91, 20))
        self.lbCost = QLabel(DlgCalc)
        self.lbCost.setObjectName(u"lbCost")
        self.lbCost.setGeometry(QRect(510, 50, 131, 21))
        self.line = QFrame(DlgCalc)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 163, 671, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(DlgCalc)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(383, 0, 20, 171))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(DlgCalc)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 190, 48, 16))
        self.label_9 = QLabel(DlgCalc)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 190, 111, 16))
        self.label_10 = QLabel(DlgCalc)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 190, 91, 16))

        self.retranslateUi(DlgCalc)

        QMetaObject.connectSlotsByName(DlgCalc)
    # setupUi

    def retranslateUi(self, DlgCalc):
        DlgCalc.setWindowTitle(QCoreApplication.translate("DlgCalc", u"\u0420\u0430\u0441\u0447\u0435\u0442", None))
        self.btnCalc.setText(QCoreApplication.translate("DlgCalc", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.btnSelect.setText(QCoreApplication.translate("DlgCalc", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u0435 \u0438\u0437 \u043f\u0440\u0430\u0439\u0441\u0430", None))
        self.label.setText(QCoreApplication.translate("DlgCalc", u"\u041a\u043b\u0438\u043c\u0430\u0442", None))
        self.label_2.setText(QCoreApplication.translate("DlgCalc", u"\u0412\u044b\u0441\u043e\u0442\u0430 (\u043c\u0435\u0442\u0440)", None))
        self.label_3.setText(QCoreApplication.translate("DlgCalc", u"\u0422\u0440\u0430\u0444\u0438\u043a (\u043c/\u0441\u0443\u0442)", None))
        self.label_4.setText(QCoreApplication.translate("DlgCalc", u"\u0428\u0438\u0440\u0438\u043d\u0430 (\u043c\u0435\u0442\u0440)", None))
        self.label_5.setText(QCoreApplication.translate("DlgCalc", u"\u0414\u043b\u0438\u043d\u0430 (\u043c\u0435\u0442\u0440)", None))
        self.lbVolume.setText("")
        self.label_6.setText(QCoreApplication.translate("DlgCalc", u"\u041e\u0431\u044a\u0435\u043c (\u043c.\u043a\u0443\u0431)", None))
        self.label_7.setText(QCoreApplication.translate("DlgCalc", u"\u0426\u0435\u043d\u0430 (\u0441\u0443\u043c\u043c):", None))
        self.lbCost.setText("")
        self.label_8.setText(QCoreApplication.translate("DlgCalc", u"\u0417\u0430\u0432\u043e\u0434", None))
        self.label_9.setText(QCoreApplication.translate("DlgCalc", u"\u0422\u0438\u043f \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u044f", None))
        self.label_10.setText(QCoreApplication.translate("DlgCalc", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u043c.\u043a\u0443\u0431", None))
    # retranslateUi

