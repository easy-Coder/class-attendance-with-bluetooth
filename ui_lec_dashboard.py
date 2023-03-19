# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lec_dashboard.ui'
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
        MainWindow.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMinimumSize(QtCore.QSize(0, 70))
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.Top_Bar.setStyleSheet("background-color: rgb(226, 226, 240);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Top_Bar)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.Top_Bar)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_bar = QtWidgets.QFrame(self.Content)
        self.side_menu_bar.setMinimumSize(QtCore.QSize(140, 0))
        self.side_menu_bar.setMaximumSize(QtCore.QSize(140, 16777215))
        self.side_menu_bar.setStyleSheet("background-color: rgb(237, 237, 252);")
        self.side_menu_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.side_menu_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_bar.setObjectName("side_menu_bar")
        self.btn_attendance_record = QtWidgets.QPushButton(self.side_menu_bar)
        self.btn_attendance_record.setGeometry(QtCore.QRect(0, 20, 141, 51))
        self.btn_attendance_record.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_attendance_record.setFont(font)
        self.btn_attendance_record.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 161, 255);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(34, 50, 226);\n"
"}")
        self.btn_attendance_record.setObjectName("btn_attendance_record")
        self.btn_take_attendance = QtWidgets.QPushButton(self.side_menu_bar)
        self.btn_take_attendance.setGeometry(QtCore.QRect(0, 80, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_take_attendance.sizePolicy().hasHeightForWidth())
        self.btn_take_attendance.setSizePolicy(sizePolicy)
        self.btn_take_attendance.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_take_attendance.setFont(font)
        self.btn_take_attendance.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 161, 255);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(34, 50, 226);\n"
"}")
        self.btn_take_attendance.setObjectName("btn_take_attendance")
        self.btn_back = QtWidgets.QPushButton(self.side_menu_bar)
        self.btn_back.setGeometry(QtCore.QRect(0, 600, 141, 51))
        self.btn_back.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 161, 255);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(34, 50, 226);\n"
"}")
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.side_menu_bar)
        self.main_content = QtWidgets.QFrame(self.Content)
        self.main_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_content.setObjectName("main_content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_content)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pages = QtWidgets.QStackedWidget(self.main_content)
        self.pages.setObjectName("pages")
        self.attendance_record_page = QtWidgets.QWidget()
        self.attendance_record_page.setObjectName("attendance_record_page")
        self.frame = QtWidgets.QFrame(self.attendance_record_page)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 861, 651))
        self.frame.setMinimumSize(QtCore.QSize(861, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_18 = QtWidgets.QFrame(self.frame_13)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 32))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_18)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 821, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_8.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(64, 0))
        self.label_9.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.course_code_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.course_code_comboBox.setObjectName("course_code_comboBox")
        self.horizontalLayout_8.addWidget(self.course_code_comboBox)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(72, 0))
        self.label_8.setMaximumSize(QtCore.QSize(72, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.course_dateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.course_dateTimeEdit.setObjectName("course_dateTimeEdit")
        self.horizontalLayout_8.addWidget(self.course_dateTimeEdit)
        self.get_attendance = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.get_attendance.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 115, 0);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.get_attendance.setObjectName("get_attendance")
        self.horizontalLayout_8.addWidget(self.get_attendance)
        self.verticalLayout_13.addWidget(self.frame_18)
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.attendance_table = QtWidgets.QTableView(self.frame_17)
        self.attendance_table.setObjectName("attendance_table")
        self.horizontalLayout_6.addWidget(self.attendance_table)
        self.verticalLayout_14.addWidget(self.frame_17)
        self.horizontalLayout_2.addWidget(self.frame_16)
        self.verticalLayout_13.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_15.setStyleSheet("background-color: rgb(28, 39, 186);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_13.addWidget(self.frame_15)
        self.verticalLayout_12.addWidget(self.frame_13)
        self.pages.addWidget(self.attendance_record_page)
        self.take_attendance_page = QtWidgets.QWidget()
        self.take_attendance_page.setObjectName("take_attendance_page")
        self.frame_2 = QtWidgets.QFrame(self.take_attendance_page)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 872, 662))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 70))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 592))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 592))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(870, 520))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMinimumSize(QtCore.QSize(432, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(432, 500))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setGeometry(QtCore.QRect(80, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_10 = QtWidgets.QFrame(self.frame_12)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.layoutWidget = QtWidgets.QWidget(self.frame_10)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 355, 110))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.course_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.course_comboBox.setMinimumSize(QtCore.QSize(300, 30))
        self.course_comboBox.setObjectName("course_comboBox")
        self.horizontalLayout_4.addWidget(self.course_comboBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget)
        self.timeEdit.setMinimumSize(QtCore.QSize(300, 30))
        self.timeEdit.setMaximumSize(QtCore.QSize(300, 30))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_5.addWidget(self.timeEdit)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setMinimumSize(QtCore.QSize(300, 30))
        self.dateEdit.setMaximumSize(QtCore.QSize(300, 30))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDate(QtCore.QDate(2021, 9, 14))
        self.dateEdit.setDate(QtCore.QDate(2021, 9, 14))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_7.addWidget(self.dateEdit)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_8.addWidget(self.frame_10)
        self.btn_take_attendance_2 = QtWidgets.QPushButton(self.frame_12)
        self.btn_take_attendance_2.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_take_attendance_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 73, 73);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(176, 21, 0);\n"
"}")
        self.btn_take_attendance_2.setObjectName("btn_take_attendance_2")
        self.verticalLayout_8.addWidget(self.btn_take_attendance_2)
        self.verticalLayout_7.addWidget(self.frame_12)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMinimumSize(QtCore.QSize(412, 500))
        self.frame_8.setMaximumSize(QtCore.QSize(432, 500))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_8)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 45))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 45))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.blt_device_list = QtWidgets.QListView(self.frame_8)
        self.blt_device_list.setMinimumSize(QtCore.QSize(330, 375))
        self.blt_device_list.setMaximumSize(QtCore.QSize(16777215, 375))
        self.blt_device_list.setViewMode(QtWidgets.QListView.ListMode)
        self.blt_device_list.setObjectName("blt_device_list")
        self.verticalLayout_5.addWidget(self.blt_device_list)
        self.btn_scan_btl = QtWidgets.QPushButton(self.frame_8)
        self.btn_scan_btl.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_scan_btl.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 115, 0);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.btn_scan_btl.setObjectName("btn_scan_btl")
        self.verticalLayout_5.addWidget(self.btn_scan_btl)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_6.setStyleSheet("background-color: rgb(28, 39, 186);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.pages.addWidget(self.take_attendance_page)
        self.create_course_page = QtWidgets.QWidget()
        self.create_course_page.setObjectName("create_course_page")
        self.frame_3 = QtWidgets.QFrame(self.create_course_page)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 870, 660))
        self.frame_3.setMinimumSize(QtCore.QSize(870, 660))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMinimumSize(QtCore.QSize(0, 70))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.frame_20 = QtWidgets.QFrame(self.frame_3)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_22)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_17.addWidget(self.lineEdit)
        self.verticalLayout_17.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_22)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(300, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_16.addWidget(self.lineEdit_2)
        self.verticalLayout_17.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.comboBox = QtWidgets.QComboBox(self.frame_22)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_15.addWidget(self.comboBox)
        self.verticalLayout_17.addLayout(self.horizontalLayout_15)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.btn_add_course = QtWidgets.QPushButton(self.frame_22)
        self.btn_add_course.setMinimumSize(QtCore.QSize(140, 50))
        self.btn_add_course.setMaximumSize(QtCore.QSize(140, 50))
        self.btn_add_course.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(156, 161, 255);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(34, 50, 226);\n"
"}")
        self.btn_add_course.setObjectName("btn_add_course")
        self.verticalLayout_18.addWidget(self.btn_add_course)
        self.horizontalLayout_14.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_20)
        self.frame_23.setMinimumSize(QtCore.QSize(290, 0))
        self.frame_23.setMaximumSize(QtCore.QSize(290, 16777215))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_14.addWidget(self.frame_23)
        self.verticalLayout_9.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_3)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_21.setStyleSheet("background-color: rgb(28, 39, 186);")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_9.addWidget(self.frame_21)
        self.pages.addWidget(self.create_course_page)
        self.verticalLayout_2.addWidget(self.pages)
        self.horizontalLayout.addWidget(self.main_content)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Class Attendance with bluetooth"))
        self.label_12.setText(_translate("MainWindow", "Class Attendance with Bluetooth and Python"))
        self.btn_attendance_record.setText(_translate("MainWindow", "Attendance Records"))
        self.btn_take_attendance.setText(_translate("MainWindow", "Take Attendance"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Attendance Records"))
        self.label_9.setText(_translate("MainWindow", "Course Code:"))
        self.label_8.setText(_translate("MainWindow", "Date and Time:"))
        self.course_dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm:ss AP"))
        self.get_attendance.setText(_translate("MainWindow", "Check Attendance"))
        self.label_3.setText(_translate("MainWindow", "Create Student"))
        self.label_6.setText(_translate("MainWindow", "Taking Attendance for"))
        self.label_4.setText(_translate("MainWindow", "Course:"))
        self.label_5.setText(_translate("MainWindow", "Time:"))
        self.label_2.setText(_translate("MainWindow", "Date:"))
        self.btn_take_attendance_2.setText(_translate("MainWindow", "Take Attendance"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:696; color:#ff0000;\">*Note</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt;\">: Scan for bluetooth devices in the class room before taking attendance.</span></p></body></html>"))
        self.btn_scan_btl.setText(_translate("MainWindow", "Scan for Device"))
        self.label_7.setText(_translate("MainWindow", "Create Course"))
        self.label_15.setText(_translate("MainWindow", "Course Code:"))
        self.label_16.setText(_translate("MainWindow", "Course Title:"))
        self.label_17.setText(_translate("MainWindow", "Lecturer In Charge:"))
        self.btn_add_course.setText(_translate("MainWindow", "Create Course"))