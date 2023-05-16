# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_asph.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_DlgAsph(object):
    def setupUi(self, DlgAsph):
        if not DlgAsph.objectName():
            DlgAsph.setObjectName(u"DlgAsph")
        DlgAsph.resize(698, 303)
        self.btnAddAsph = QPushButton(DlgAsph)
        self.btnAddAsph.setObjectName(u"btnAddAsph")
        self.btnAddAsph.setGeometry(QRect(550, 40, 75, 24))
        self.btnDelAsph = QPushButton(DlgAsph)
        self.btnDelAsph.setObjectName(u"btnDelAsph")
        self.btnDelAsph.setGeometry(QRect(550, 80, 75, 24))
        self.btnCngAsph = QPushButton(DlgAsph)
        self.btnCngAsph.setObjectName(u"btnCngAsph")
        self.btnCngAsph.setGeometry(QRect(550, 120, 75, 24))
        self.tbAsph = QTableView(DlgAsph)
        self.tbAsph.setObjectName(u"tbAsph")
        self.tbAsph.setGeometry(QRect(20, 10, 451, 251))

        self.retranslateUi(DlgAsph)

        QMetaObject.connectSlotsByName(DlgAsph)
    # setupUi

    def retranslateUi(self, DlgAsph):
        DlgAsph.setWindowTitle(QCoreApplication.translate("DlgAsph", u"Dialog", None))
        self.btnAddAsph.setText(QCoreApplication.translate("DlgAsph", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnDelAsph.setText(QCoreApplication.translate("DlgAsph", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnCngAsph.setText(QCoreApplication.translate("DlgAsph", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

