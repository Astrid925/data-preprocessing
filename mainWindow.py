# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QToolBar, QVBoxLayout, QWidget)
import resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 720)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actSaveFile = QAction(MainWindow)
        self.actSaveFile.setObjectName(u"actSaveFile")
        icon = QIcon()
        icon.addFile(u":/images/pic/fileSave.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actSaveFile.setIcon(icon)
        self.actUnpacking = QAction(MainWindow)
        self.actUnpacking.setObjectName(u"actUnpacking")
        icon1 = QIcon()
        icon1.addFile(u":/images/pic/dataPacket.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actUnpacking.setIcon(icon1)
        self.actNUC = QAction(MainWindow)
        self.actNUC.setObjectName(u"actNUC")
        icon2 = QIcon()
        icon2.addFile(u":/images/pic/NUC.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actNUC.setIcon(icon2)
        self.actBPR = QAction(MainWindow)
        self.actBPR.setObjectName(u"actBPR")
        icon3 = QIcon()
        icon3.addFile(u":/images/pic/BRP.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actBPR.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(60)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.horizontalLayout_2.addWidget(self.titleLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")

        self.horizontalLayout_3.addWidget(self.imageLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actSaveFile)
        self.menu.addAction(self.actUnpacking)
        self.menu_2.addAction(self.actNUC)
        self.menu_2.addAction(self.actBPR)
        self.toolBar.addAction(self.actSaveFile)
        self.toolBar.addAction(self.actUnpacking)
        self.toolBar.addAction(self.actNUC)
        self.toolBar.addAction(self.actBPR)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5c0f\u884c\u661f\u6570\u636e\u5904\u7406\u8f6f\u4ef6", None))
        self.actSaveFile.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u50a8\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.actSaveFile.setToolTip(QCoreApplication.translate("MainWindow", u"\u5b58\u50a8\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actSaveFile.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actUnpacking.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u89e3\u5305", None))
#if QT_CONFIG(shortcut)
        self.actUnpacking.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actNUC.setText(QCoreApplication.translate("MainWindow", u"\u975e\u5747\u5300\u6027\u6821\u6b63", None))
#if QT_CONFIG(shortcut)
        self.actNUC.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actBPR.setText(QCoreApplication.translate("MainWindow", u"\u76f2\u5143\u8865\u507f", None))
#if QT_CONFIG(shortcut)
        self.actBPR.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.titleLabel.setText("")
        self.imageLabel.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u9884\u5904\u7406", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

