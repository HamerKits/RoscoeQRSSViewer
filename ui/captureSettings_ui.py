# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'captureSettings_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 381, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cbCapture = QComboBox(self.verticalLayoutWidget)
        self.cbCapture.setObjectName(u"cbCapture")

        self.verticalLayout.addWidget(self.cbCapture)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lblFolder = QLabel(self.verticalLayoutWidget)
        self.lblFolder.setObjectName(u"lblFolder")
        self.lblFolder.setWordWrap(True)

        self.horizontalLayout.addWidget(self.lblFolder)

        self.btnBrowse = QPushButton(self.verticalLayoutWidget)
        self.btnBrowse.setObjectName(u"btnBrowse")

        self.horizontalLayout.addWidget(self.btnBrowse)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.txtImageName = QLineEdit(self.verticalLayoutWidget)
        self.txtImageName.setObjectName(u"txtImageName")

        self.horizontalLayout_2.addWidget(self.txtImageName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cbIncrement = QCheckBox(self.verticalLayoutWidget)
        self.cbIncrement.setObjectName(u"cbIncrement")

        self.horizontalLayout_3.addWidget(self.cbIncrement)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.txtCaptureInterval = QLineEdit(self.verticalLayoutWidget)
        self.txtCaptureInterval.setObjectName(u"txtCaptureInterval")

        self.horizontalLayout_3.addWidget(self.txtCaptureInterval)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Capture Settings", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Capture Folder: ", None))
        self.lblFolder.setText(QCoreApplication.translate("Dialog", u"/home/user/capture/", None))
        self.btnBrowse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"File Name: ", None))
        self.cbIncrement.setText(QCoreApplication.translate("Dialog", u"Increment Index", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Interval (seconds):", None))
        self.txtCaptureInterval.setText(QCoreApplication.translate("Dialog", u"1", None))
    # retranslateUi

