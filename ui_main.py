# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 720))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.324, y1:0.221682, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(76, 94, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(120, 120, 120, 120)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 40, -1, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(16, 70, 741, 241))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 72))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 72))
        self.frame_3.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 721, 74))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_admin_page = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_admin_page.setMinimumSize(QtCore.QSize(0, 38))
        self.btn_admin_page.setStyleSheet("background-color: rgb(255, 253, 253);\n"
"color: blue;")
        self.btn_admin_page.setObjectName("btn_admin_page")
        self.horizontalLayout.addWidget(self.btn_admin_page)
        self.btn_lec_page = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_lec_page.setMinimumSize(QtCore.QSize(0, 38))
        self.btn_lec_page.setStyleSheet("background-color: rgb(255, 253, 253);\n"
"color: blue;")
        self.btn_lec_page.setObjectName("btn_lec_page")
        self.horizontalLayout.addWidget(self.btn_lec_page)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Class Attendance with bluetooth"))
        self.label.setText(_translate("MainWindow", "Class Attendance using Bluetooth and Python"))
        self.btn_admin_page.setText(_translate("MainWindow", "Admin Dashboard"))
        self.btn_lec_page.setText(_translate("MainWindow", "Lecturer Dashboard"))
