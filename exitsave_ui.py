# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exitsave.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_exitsave(object):
    def setupUi(self, exitsave):
        if not exitsave.objectName():
            exitsave.setObjectName(u"exitsave")
        exitsave.resize(400, 114)
        self.horizontalLayoutWidget = QWidget(exitsave)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 50, 301, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.label = QLabel(exitsave)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 261, 41))

        self.retranslateUi(exitsave)

        QMetaObject.connectSlotsByName(exitsave)
    # setupUi

    def retranslateUi(self, exitsave):
        exitsave.setWindowTitle(QCoreApplication.translate("exitsave", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("exitsave", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("exitsave", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("exitsave", u"Are you sure you want Exit without Saving?", None))
    # retranslateUi

