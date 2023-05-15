# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_add_factory.ui'
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

class Ui_AddFactory(object):
    def setupUi(self, AddFactory):
        if not AddFactory.objectName():
            AddFactory.setObjectName(u"AddFactory")
        AddFactory.resize(232, 133)
        self.btnAddFct = QPushButton(AddFactory)
        self.btnAddFct.setObjectName(u"btnAddFct")
        self.btnAddFct.setGeometry(QRect(60, 80, 111, 21))
        self.label = QLabel(AddFactory)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 30, 51, 21))
        self.inpName = QLineEdit(AddFactory)
        self.inpName.setObjectName(u"inpName")
        self.inpName.setGeometry(QRect(10, 30, 113, 22))

        self.retranslateUi(AddFactory)

        QMetaObject.connectSlotsByName(AddFactory)
    # setupUi

    def retranslateUi(self, AddFactory):
        AddFactory.setWindowTitle(QCoreApplication.translate("AddFactory", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0432\u043e\u0434", None))
        self.btnAddFct.setText(QCoreApplication.translate("AddFactory", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("AddFactory", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

