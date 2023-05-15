# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(211, 241)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnPrice = QPushButton(self.centralwidget)
        self.btnPrice.setObjectName(u"btnPrice")
        self.btnPrice.setGeometry(QRect(30, 20, 75, 24))
        self.btnAsph = QPushButton(self.centralwidget)
        self.btnAsph.setObjectName(u"btnAsph")
        self.btnAsph.setGeometry(QRect(30, 60, 111, 24))
        self.btnCalc = QPushButton(self.centralwidget)
        self.btnCalc.setObjectName(u"btnCalc")
        self.btnCalc.setGeometry(QRect(30, 110, 75, 24))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 160, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 211, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnPrice.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0439\u0441", None))
        self.btnAsph.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u0439", None))
        self.btnCalc.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

