# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newfaquan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import ziyuan

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 608)
        #MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("background:pink;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setStyleSheet("color:#232C51;\n"
"background:white;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("border-image: url(:/img/头部.jpg);\n"
"color:#232C51;\n"
"background:white;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.label_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_4.setText("")
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setMaximumSize(QtCore.QSize(600, 800))
        self.label_2.setStyleSheet("border-image: url(:/img/空白.jpg);\n"
"color:white;\n"
"background:white;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border:none;\n"
"font-size:44px;\n"
"font-weight:700;\n"
"font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet("border-image: url(:/img/识别.jpg);\n"
"color:#232C51;\n"
"background:white;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.pushButton.setText("")
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-image: url(:/img/优惠券.jpg);\n"
"color:#232C51;\n"
"background:white;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(618, 147))
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setTabletTracking(False)
        self.comboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setToolTip("")
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("\n"
"color:white;\n"
"background:#c683b6;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("border-image: url(:/img/空白.jpg);\n"
"color:white;\n"
"background:white;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"font-size:150px;\n"
"font-weight:1000;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: url(:/img/提示.jpg);\n"
"color:#232C51;\n"
"background:white;\n"
"border-top:1px solid darkGray;\n"
"border-bottom:1px solid darkGray;\n"
"border-right:1px solid darkGray;\n"
"border-left:1px solid darkGray;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border:none;\n"
"        font-size:16px;\n"
"        font-weight:700;\n"
"        font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">摄像头显示区域</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">请把小票放入识别框内</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "云"))
        self.comboBox.setItemText(1, _translate("MainWindow", "川"))
        self.comboBox.setItemText(2, _translate("MainWindow", "贵"))
        self.comboBox.setItemText(3, _translate("MainWindow", "藏"))
        self.comboBox.setItemText(4, _translate("MainWindow", "陕"))
        self.comboBox.setItemText(5, _translate("MainWindow", "甘"))
        self.comboBox.setItemText(6, _translate("MainWindow", "青"))
        self.comboBox.setItemText(7, _translate("MainWindow", "宁"))
        self.comboBox.setItemText(8, _translate("MainWindow", "京"))
        self.comboBox.setItemText(9, _translate("MainWindow", "沪"))
        self.comboBox.setItemText(10, _translate("MainWindow", "津"))
        self.comboBox.setItemText(11, _translate("MainWindow", "渝"))
        self.comboBox.setItemText(12, _translate("MainWindow", "鲁"))
        self.comboBox.setItemText(13, _translate("MainWindow", "冀"))
        self.comboBox.setItemText(14, _translate("MainWindow", "晋"))
        self.comboBox.setItemText(15, _translate("MainWindow", "蒙"))
        self.comboBox.setItemText(16, _translate("MainWindow", "辽"))
        self.comboBox.setItemText(17, _translate("MainWindow", "吉"))
        self.comboBox.setItemText(18, _translate("MainWindow", "黑"))
        self.comboBox.setItemText(19, _translate("MainWindow", "苏"))
        self.comboBox.setItemText(20, _translate("MainWindow", "浙"))
        self.comboBox.setItemText(21, _translate("MainWindow", "皖"))
        self.comboBox.setItemText(22, _translate("MainWindow", "闽"))
        self.comboBox.setItemText(23, _translate("MainWindow", "赣"))
        self.comboBox.setItemText(24, _translate("MainWindow", "豫"))
        self.comboBox.setItemText(25, _translate("MainWindow", "湘"))
        self.comboBox.setItemText(26, _translate("MainWindow", "鄂"))
        self.comboBox.setItemText(27, _translate("MainWindow", "粤"))
        self.comboBox.setItemText(28, _translate("MainWindow", "桂"))
        self.comboBox.setItemText(29, _translate("MainWindow", "琼"))

