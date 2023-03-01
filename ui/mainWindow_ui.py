# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(903, 637)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSelect_Input = QAction(MainWindow)
        self.actionSelect_Input.setObjectName(u"actionSelect_Input")
        self.actionCapture_Settings = QAction(MainWindow)
        self.actionCapture_Settings.setObjectName(u"actionCapture_Settings")
        self.actionQRSS3 = QAction(MainWindow)
        self.actionQRSS3.setObjectName(u"actionQRSS3")
        self.actionQRSS3.setCheckable(True)
        self.actionQRSS10 = QAction(MainWindow)
        self.actionQRSS10.setObjectName(u"actionQRSS10")
        self.actionQRSS10.setCheckable(True)
        self.actionQRSS20 = QAction(MainWindow)
        self.actionQRSS20.setObjectName(u"actionQRSS20")
        self.actionQRSS20.setCheckable(True)
        self.actionQRSS30 = QAction(MainWindow)
        self.actionQRSS30.setObjectName(u"actionQRSS30")
        self.actionQRSS30.setCheckable(True)
        self.actionQRSS60 = QAction(MainWindow)
        self.actionQRSS60.setObjectName(u"actionQRSS60")
        self.actionQRSS60.setCheckable(True)
        self.actionQRSS120 = QAction(MainWindow)
        self.actionQRSS120.setObjectName(u"actionQRSS120")
        self.actionQRSS120.setCheckable(True)
        self.actionFull_Speed = QAction(MainWindow)
        self.actionFull_Speed.setObjectName(u"actionFull_Speed")
        self.actionFull_Speed.setCheckable(True)
        self.actionWaterfall_Note = QAction(MainWindow)
        self.actionWaterfall_Note.setObjectName(u"actionWaterfall_Note")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pvSignal = QProgressBar(self.centralwidget)
        self.pvSignal.setObjectName(u"pvSignal")
        self.pvSignal.setMaximumSize(QSize(10, 16777215))
        self.pvSignal.setMaximum(255)
        self.pvSignal.setValue(0)
        self.pvSignal.setTextVisible(False)
        self.pvSignal.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.pvSignal)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(4)

        self.verticalLayout_9.addWidget(self.label)

        self.txtCenterFrequency = QLineEdit(self.centralwidget)
        self.txtCenterFrequency.setObjectName(u"txtCenterFrequency")
        self.txtCenterFrequency.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_9.addWidget(self.txtCenterFrequency)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(4)

        self.verticalLayout_9.addWidget(self.label_2)

        self.txtFrequencySpan = QLineEdit(self.centralwidget)
        self.txtFrequencySpan.setObjectName(u"txtFrequencySpan")

        self.verticalLayout_9.addWidget(self.txtFrequencySpan)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.txtOffset = QLineEdit(self.centralwidget)
        self.txtOffset.setObjectName(u"txtOffset")

        self.verticalLayout_9.addWidget(self.txtOffset)

        self.btnSetFrequency = QPushButton(self.centralwidget)
        self.btnSetFrequency.setObjectName(u"btnSetFrequency")

        self.verticalLayout_9.addWidget(self.btnSetFrequency)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.sliderBase = QSlider(self.centralwidget)
        self.sliderBase.setObjectName(u"sliderBase")
        self.sliderBase.setMinimum(1)
        self.sliderBase.setMaximum(100)
        self.sliderBase.setValue(30)
        self.sliderBase.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.sliderBase)

        self.sliderContrast = QSlider(self.centralwidget)
        self.sliderContrast.setObjectName(u"sliderContrast")
        self.sliderContrast.setMinimum(1)
        self.sliderContrast.setValue(70)
        self.sliderContrast.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.sliderContrast)

        self.lblGradient = QLabel(self.centralwidget)
        self.lblGradient.setObjectName(u"lblGradient")
        self.lblGradient.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.lblGradient)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.sliderSpeed = QSlider(self.centralwidget)
        self.sliderSpeed.setObjectName(u"sliderSpeed")
        self.sliderSpeed.setMaximum(4)
        self.sliderSpeed.setPageStep(1)
        self.sliderSpeed.setValue(2)
        self.sliderSpeed.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.sliderSpeed)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self.cbInvert = QCheckBox(self.centralwidget)
        self.cbInvert.setObjectName(u"cbInvert")

        self.verticalLayout_9.addWidget(self.cbInvert)

        self.cbAGC = QCheckBox(self.centralwidget)
        self.cbAGC.setObjectName(u"cbAGC")

        self.verticalLayout_9.addWidget(self.cbAGC)

        self.cbCapture1 = QCheckBox(self.centralwidget)
        self.cbCapture1.setObjectName(u"cbCapture1")

        self.verticalLayout_9.addWidget(self.cbCapture1)

        self.cbCapture2 = QCheckBox(self.centralwidget)
        self.cbCapture2.setObjectName(u"cbCapture2")

        self.verticalLayout_9.addWidget(self.cbCapture2)


        self.verticalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.lblImage = QLabel(self.centralwidget)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setAutoFillBackground(False)
        self.lblImage.setStyleSheet(u"")
        self.lblImage.setPixmap(QPixmap(u"WFTest.jpg"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lblImage)

        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 903, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInput = QMenu(self.menubar)
        self.menuInput.setObjectName(u"menuInput")
        self.menuCapture = QMenu(self.menubar)
        self.menuCapture.setObjectName(u"menuCapture")
        self.menuMode = QMenu(self.menubar)
        self.menuMode.setObjectName(u"menuMode")
        self.menuPreferences = QMenu(self.menubar)
        self.menuPreferences.setObjectName(u"menuPreferences")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuCapture.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuInput.addAction(self.actionSelect_Input)
        self.menuCapture.addAction(self.actionCapture_Settings)
        self.menuMode.addAction(self.actionFull_Speed)
        self.menuMode.addAction(self.actionQRSS3)
        self.menuMode.addAction(self.actionQRSS10)
        self.menuMode.addAction(self.actionQRSS20)
        self.menuMode.addAction(self.actionQRSS30)
        self.menuMode.addAction(self.actionQRSS60)
        self.menuMode.addAction(self.actionQRSS120)
        self.menuPreferences.addAction(self.actionWaterfall_Note)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Roscoe", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSelect_Input.setText(QCoreApplication.translate("MainWindow", u"Select Input", None))
        self.actionCapture_Settings.setText(QCoreApplication.translate("MainWindow", u"Capture Settings", None))
        self.actionQRSS3.setText(QCoreApplication.translate("MainWindow", u"QRSS3", None))
        self.actionQRSS10.setText(QCoreApplication.translate("MainWindow", u"QRSS10", None))
        self.actionQRSS20.setText(QCoreApplication.translate("MainWindow", u"QRSS20", None))
        self.actionQRSS30.setText(QCoreApplication.translate("MainWindow", u"QRSS30", None))
        self.actionQRSS60.setText(QCoreApplication.translate("MainWindow", u"QRSS60", None))
        self.actionQRSS120.setText(QCoreApplication.translate("MainWindow", u"QRSS120", None))
        self.actionFull_Speed.setText(QCoreApplication.translate("MainWindow", u"Full Speed", None))
        self.actionWaterfall_Note.setText(QCoreApplication.translate("MainWindow", u"Waterfall Note", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Frequency (Hz)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Frequency Span (Hz)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Display Offset (Hz)", None))
        self.btnSetFrequency.setText(QCoreApplication.translate("MainWindow", u"Set Frequency", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Color Gain Adjust", None))
#if QT_CONFIG(tooltip)
        self.sliderBase.setToolTip(QCoreApplication.translate("MainWindow", u"Base display level", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sliderContrast.setToolTip(QCoreApplication.translate("MainWindow", u"Contrast", None))
#endif // QT_CONFIG(tooltip)
        self.lblGradient.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Waterfall Speed", None))
        self.cbInvert.setText(QCoreApplication.translate("MainWindow", u"Invert Scale", None))
        self.cbAGC.setText(QCoreApplication.translate("MainWindow", u"Slow AGC", None))
        self.cbCapture1.setText(QCoreApplication.translate("MainWindow", u"Enable Capture 1", None))
        self.cbCapture2.setText(QCoreApplication.translate("MainWindow", u"Enable Capture 2", None))
        self.lblImage.setText("")
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuInput.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.menuCapture.setTitle(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuPreferences.setTitle(QCoreApplication.translate("MainWindow", u"Preferences", None))
    # retranslateUi

