# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ptoject2rGCuNW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 0, 0, 0);\n"
"border: none;\n"
"}\n"
"QFrame{\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}\n"
"color: rgb(0, 85, 127);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QFrame(self.centralwidget)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setStyleSheet(u"background:rgb(255, 255, 243)")
        self.top_widget.setFrameShape(QFrame.NoFrame)
        self.top_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.top_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.top_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.text_label_name = QLabel(self.frame_4)
        self.text_label_name.setObjectName(u"text_label_name")
        font = QFont()
        font.setPointSize(14)
        self.text_label_name.setFont(font)

        self.horizontalLayout_4.addWidget(self.text_label_name)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.top_widget)

        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.left_body = QFrame(self.header)
        self.left_body.setObjectName(u"left_body")
        self.left_body.setMinimumSize(QSize(150, 0))
        self.left_body.setMaximumSize(QSize(150, 16777215))
        self.left_body.setStyleSheet(u"background:rgb(255, 255, 243);")
        self.left_body.setFrameShape(QFrame.StyledPanel)
        self.left_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.left_body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.first = QPushButton(self.frame)
        self.first.setObjectName(u"first")
        font1 = QFont()
        font1.setPointSize(12)
        self.first.setFont(font1)

        self.verticalLayout_6.addWidget(self.first)

        self.second = QPushButton(self.frame)
        self.second.setObjectName(u"second")
        self.second.setFont(font1)

        self.verticalLayout_6.addWidget(self.second)

        self.third = QPushButton(self.frame)
        self.third.setObjectName(u"third")
        self.third.setFont(font1)

        self.verticalLayout_6.addWidget(self.third)

        self.forth = QPushButton(self.frame)
        self.forth.setObjectName(u"forth")
        self.forth.setFont(font1)

        self.verticalLayout_6.addWidget(self.forth)

        self.fifth = QPushButton(self.frame)
        self.fifth.setObjectName(u"fifth")
        self.fifth.setFont(font1)

        self.verticalLayout_6.addWidget(self.fifth)

        self.six = QPushButton(self.frame)
        self.six.setObjectName(u"six")
        self.six.setFont(font1)

        self.verticalLayout_6.addWidget(self.six)

        self.seven = QPushButton(self.frame)
        self.seven.setObjectName(u"seven")
        self.seven.setFont(font1)

        self.verticalLayout_6.addWidget(self.seven)

        self.task_but = QPushButton(self.frame)
        self.task_but.setObjectName(u"task_but")
        font2 = QFont()
        font2.setPointSize(10)
        self.task_but.setFont(font2)

        self.verticalLayout_6.addWidget(self.task_but)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.left_body)

        self.header_body = QFrame(self.header)
        self.header_body.setObjectName(u"header_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_body.sizePolicy().hasHeightForWidth())
        self.header_body.setSizePolicy(sizePolicy1)
        self.header_body.setStyleSheet(u"background-color: rgb(168, 255, 162);")
        self.header_body.setFrameShape(QFrame.StyledPanel)
        self.header_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.header_body)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.header_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.task = QWidget()
        self.task.setObjectName(u"task")
        self.verticalLayout_11 = QVBoxLayout(self.task)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.comboBox_number = QComboBox(self.task)
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.addItem("")
        self.comboBox_number.setObjectName(u"comboBox_number")
        self.comboBox_number.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.comboBox_number)

        self.frame_5 = QFrame(self.task)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_image = QLabel(self.frame_5)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setPixmap(QPixmap(u":/newPrefix/pict/task_1.10.svg"))

        self.verticalLayout_12.addWidget(self.label_image)

        self.labe_text = QLabel(self.frame_5)
        self.labe_text.setObjectName(u"labe_text")

        self.verticalLayout_12.addWidget(self.labe_text)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.task)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.line_otvet = QLineEdit(self.frame_2)
        self.line_otvet.setObjectName(u"line_otvet")
        self.line_otvet.setMaximumSize(QSize(200, 16777215))
        self.line_otvet.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.line_otvet)

        self.otvet_test = QPushButton(self.frame_2)
        self.otvet_test.setObjectName(u"otvet_test")

        self.horizontalLayout_10.addWidget(self.otvet_test)

        self.label_true = QLabel(self.frame_2)
        self.label_true.setObjectName(u"label_true")

        self.horizontalLayout_10.addWidget(self.label_true)


        self.verticalLayout_11.addWidget(self.frame_2, 0, Qt.AlignBottom)

        self.new_task = QPushButton(self.task)
        self.new_task.setObjectName(u"new_task")

        self.verticalLayout_11.addWidget(self.new_task)

        self.stackedWidget.addWidget(self.task)
        self.first_page = QWidget()
        self.first_page.setObjectName(u"first_page")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.first_page.sizePolicy().hasHeightForWidth())
        self.first_page.setSizePolicy(sizePolicy2)
        self.horizontalLayout_16 = QHBoxLayout(self.first_page)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.scrollArea = QScrollArea(self.first_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(239, 255, 240);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 703, 1295))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_3.addWidget(self.label_19)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_16.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.first_page)
        self.second_page = QWidget()
        self.second_page.setObjectName(u"second_page")
        self.horizontalLayout_2 = QHBoxLayout(self.second_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea_2 = QScrollArea(self.second_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(239, 255, 240);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 632, 542))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setSpacing(11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_5.addWidget(self.label_20)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.second_page)
        self.forth_page = QWidget()
        self.forth_page.setObjectName(u"forth_page")
        self.horizontalLayout_6 = QHBoxLayout(self.forth_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scrollArea_4 = QScrollArea(self.forth_page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"background-color: rgb(239, 255, 240);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 752, 1957))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_8.setSpacing(11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_22 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_8.addWidget(self.label_22)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_6.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.forth_page)
        self.seven_page = QWidget()
        self.seven_page.setObjectName(u"seven_page")
        self.horizontalLayout_9 = QHBoxLayout(self.seven_page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scrollArea_6 = QScrollArea(self.seven_page)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u"background-color: rgb(239, 255, 240);")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 799, 593))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_10.setSpacing(11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_24 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_10.addWidget(self.label_24)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_9.addWidget(self.scrollArea_6)

        self.stackedWidget.addWidget(self.seven_page)
        self.six_page = QWidget()
        self.six_page.setObjectName(u"six_page")
        self.horizontalLayout_8 = QHBoxLayout(self.six_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea_5 = QScrollArea(self.six_page)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"background-color: rgb(239, 255, 240);")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1184, 1145))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_9.setSpacing(11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_23 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_9.addWidget(self.label_23)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_8.addWidget(self.scrollArea_5)

        self.stackedWidget.addWidget(self.six_page)
        self.third_page = QWidget()
        self.third_page.setObjectName(u"third_page")
        self.horizontalLayout_5 = QHBoxLayout(self.third_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea_3 = QScrollArea(self.third_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(239, 255, 240);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 663, 6001))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setSpacing(11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_7.addWidget(self.label_21)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_5.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.third_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.header_body)


        self.verticalLayout.addWidget(self.header)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_label_name.setText(QCoreApplication.translate("MainWindow", u"Math 27+", None))
        self.first.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.second.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.third.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.forth.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.fifth.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.task_but.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.comboBox_number.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_number.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_number.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_number.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_number.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_number.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_number.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_number.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_number.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_number.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_number.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))

        self.label_image.setText("")
        self.labe_text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.otvet_test.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.label_true.setText("")
        self.new_task.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1. <span style=\" color:#212529;\">\u041f\u0440\u043e\u0441\u0442\u0435\u0439\u0448\u0438\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f. </span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0412 \u0437\u0430\u0434\u0430\u043d\u0438\u0438 \u21161 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430 \u0415\u0413\u042d \u0432\u0430\u043c \u0432\u0441\u0442\u0440\u0435\u0442\u044f\u0442\u0441\u044f \u0432\u0441\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f: \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0435 \u0438</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0441\u0432\u043e\u0434\u044f\u0449\u0438\u0435\u0441\u044f \u043a \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u043c, \u0434\u0440\u043e\u0431\u043d\u043e-\u0440\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435, \u0438\u0440\u0440\u0430"
                        "\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435, \u0441\u0442\u0435\u043f\u0435\u043d\u043d\u044b\u0435,</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0438 \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0438 \u0434\u0430\u0436\u0435 \u0442\u0440\u0438\u0433\u043e\u043d\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435. \u0412\u0438\u0434\u0438\u0442\u0435, \u043a\u0430\u043a \u043c\u043d\u043e\u0433\u043e \u043d\u0443\u0436\u043d\u043e</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0437\u043d\u0430\u0442\u044c, \u0447\u0442\u043e\u0431\u044b \u0441\u043f\u0440\u0430\u0432\u0438\u0442\u044c\u0441\u044f \u0441 \u0437\u0430\u0434\u0430\u043d\u0438\u0435\u043c! \u0418 \u0435\u0449\u0435 \u043b\u043e\u0432\u0443\u0448\u043a\u0438 \u0438 \u00ab\u043f\u043e\u0434\u0432\u043e\u0434\u043d\u044b\u0435 \u043a\u0430"
                        "\u043c\u043d\u0438\u00bb, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0436\u0434\u0443\u0442 \u0432\u0430\u0441</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0432 \u0441\u0430\u043c\u043e\u043c \u043d\u0435\u043e\u0436\u0438\u0434\u0430\u043d\u043d\u043e\u043c \u043c\u0435\u0441\u0442\u0435.</span></p><p><span style=\" color:#212529;\">\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f</span></p><p><span style=\" color:#212529;\">\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u2013 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0432\u0438\u0434\u0430 ax^2+bx+c = 0 \u0433\u0434\u0435 a \u043d\u0435 \u0440\u0430\u0432\u043d\u043e 0.</span></p><p><span style=\" color:#212529;\">\u0427\u0438\u0441\u043b\u0430 a, b, c \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u0430"
                        "\u043c\u0438 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f.</span></p><p><span style=\" color:#212529;\">\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u043c\u043e\u0436\u0435\u0442 \u0438\u043c\u0435\u0442\u044c \u0434\u0432\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043a\u043e\u0440\u043d\u044f, \u043e\u0434\u0438\u043d \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u0440\u0435\u043d\u044c \u0438\u043b\u0438 \u043d\u0438 \u043e\u0434\u043d\u043e\u0433\u043e.</span></p><p><span style=\" color:#212529;\">\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u0440\u043d\u0435\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u0432\u0438\u0441\u0438\u0442 \u043e"
                        "\u0442 \u0437\u043d\u0430\u043a\u0430 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u043d\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0434\u0438\u0441\u043a\u0440\u0438\u043c\u0438\u043d\u0430\u043d\u0442.</span></p><p><span style=\" font-family:'Arial','sans-serif'; font-weight:600; color:#212529;\">\u0414\u0438\u0441\u043a\u0440\u0438\u043c\u0438\u043d\u0430\u043d\u0442 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f:</span><span style=\" color:#212529;\"> D = b^2 \u2013 4ac.</span></p><p><span style=\" color:#212529;\">\u0415\u0441\u043b\u0438 D &gt; 0, \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u0435\u0442 \u0434\u0432\u0430 \u043a\u043e\u0440\u043d\u044f: </span><img src=\":/newPrefix/pict/pict28.jpg\"/><span style=\" color:#212529;\"> \u0438 </span><img src=\":/newPrefix/pict/"
                        "pict29.jpg\"/><span style=\" color:#212529;\"> .</span></p><p><span style=\" color:#212529;\">\u0415\u0441\u043b\u0438 D = 0, \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u0435\u0442 \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043a\u043e\u0440\u0435\u043d\u044c </span><img src=\":/newPrefix/pict/pict30.jpg\"/><span style=\" color:#212529;\"> .</span></p><p><span style=\" color:#212529;\">\u0415\u0441\u043b\u0438 D &lt; 0, \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u043d\u0435 \u0438\u043c\u0435\u0435\u0442 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043a\u043e\u0440\u043d\u0435\u0439.</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0420\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0438\u043c \u043d\u0435\u043f\u043e\u043b\u043d\u044b\u0435 \u043a\u0432\u0430"
                        "\u0434\u0440\u0430\u0442\u043d\u044b\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f. </span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u041d\u0435\u043f\u043e\u043b\u043d\u044b\u043c\u0438 \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 b, \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 c, \u0438\u043b\u0438</span></p><p><span style=\" color:#212529; background-color:#ffffff;\"> \u043e\u0431\u0430 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u0430 \u0440\u0430\u0432\u043d\u044b \u043d\u0443\u043b\u044e.</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">c = 0 </span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0422\u043e\u0433\u0434\u0430 \u0443\u0440"
                        "\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u0435\u0442 \u0432\u0438\u0434: </span></p><p><span style=\" color:#212529; background-color:#ffffff;\">ax^2+bx = 0</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0417\u0430\u043f\u0438\u0448\u0435\u043c \u0435\u0433\u043e \u0432 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c \u0432\u0438\u0434\u0435:</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">x(ax+b) =0 </span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u0434\u0432\u0443\u0445 \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u0435\u0439 \u0440\u0430\u0432\u043d\u043e \u043d\u0443\u043b\u044e \u0442\u043e\u0433\u0434\u0430 \u0438 \u0442\u043e\u043b\u044c\u043a\u043e \u0442\u043e\u0433\u0434\u0430, \u043a\u043e\u0433\u0434\u0430 \u0445\u043e\u0442\u044f \u0431\u044b \u043e\u0434\u0438\u043d \u0438\u0437 \u043d\u0438\u0445</span></p><p><span style"
                        "=\" color:#212529; background-color:#ffffff;\">\u0440\u0430\u0432\u0435\u043d \u043d\u0443\u043b\u044e.</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0417\u043d\u0430\u0447\u0438\u0442 </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"44\" height=\"18\"/><span style=\" color:#212529;\"> , </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png\" width=\"54\" height=\"26\"/></p><p><span style=\" color:#212529; background-color:#ffffff;\">b = 0 </span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0422\u043e\u0433\u0434\u0430 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u0435\u0442 \u0432\u0438\u0434 ax^2 + c = 0</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u041a\u043e\u0440\u043d\u044f\u043c\u0438 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0431\u0443\u0434\u0443\u0442"
                        " </span><img src=\":/newPrefix/pict/pict31.jpg\"/></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u041f\u0440\u0438 \u044d\u0442\u043e\u043c \u043f\u043e\u0434\u043a\u043e\u0440\u0435\u043d\u043d\u043e\u0435 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0443\u043b\u044f, \u043b\u0438\u0431\u043e \u0440\u0430\u0432\u043d\u043e \u043d\u0443\u043b\u044e.</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">b = 0 \u0438 c = 0</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u0422\u043e\u0433\u0434\u0430 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u0435\u0442 \u0432\u0438\u0434 ax^2 = 0</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">\u041e\u0447\u0435\u0432\u0438\u0434\u043d\u043e \u0447\u0442\u043e \u043e\u043d\u043e \u0438\u043c\u0435\u0435\u0442 \u0435\u0434\u0438\u043d\u0441\u0442\u0432"
                        "\u0435\u043d\u043d\u044b\u0439 \u043a\u043e\u0440\u0435\u043d\u044c x = 0</span></p><p>\u0422\u0435\u043e\u0440\u0435\u043c\u0430 \u0412\u0438\u0435\u0442\u0430 </p><p><span style=\" color:#212529;\">\u041f\u043e\u043b\u0435\u0437\u043d\u0430\u044f \u0442\u0435\u043e\u0440\u0435\u043c\u0430 \u0434\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0445 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439 \u2013 \u0442\u0435\u043e\u0440\u0435\u043c\u0430 \u0412\u0438\u0435\u0442\u0430.</span></p><p><span style=\" color:#212529;\">\u0415\u0441\u043b\u0438 </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png\" width=\"17\" height=\"18\"/><span style=\" color:#212529;\"> \u0438 </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png\" width=\"14\" height=\"18\"/><span style=\" color:#212529;\"> \u2013 \u043a\u043e\u0440\u043d\u0438 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438"
                        "\u044f ax^2+bx+c = 0, \u0442\u043e </span></p><p><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image010.png\" width=\"91\" height=\"26\"/><span style=\" color:#212529;\"> \u0438 </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image012.png\" width=\"57\" height=\"25\"/></p><p>\u0420\u0430\u0437\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u0442\u0440\u0435\u0445\u0447\u043b\u0435\u043d\u0430 \u043d\u0430 \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u0438 </p><p><span style=\" color:#212529;\">ax^2+bx+c = a(x-</span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image014.png\" width=\"20\" height=\"18\"/><span style=\" color:#212529;\">)(x-</span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png\" width=\"14\" height=\"18\"/><span style=\" color:#212529;\">)</span></p><p><span style=\" color:#212529;\">\u0417\u0434\u0435\u0441"
                        "\u044c </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png\" width=\"17\" height=\"18\"/><span style=\" color:#212529;\">\u0438 </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png\" width=\"14\" height=\"18\"/><span style=\" color:#212529;\"> \u2013 \u043a\u043e\u0440\u043d\u0438 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f ax^2+bx+c = 0.</span></p><p><span style=\" color:#212529;\">\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u0435 \u044d\u0442\u0443 \u0444\u043e\u0440\u043c\u0443\u043b\u0443. \u041e\u043d\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u0430 \u0434\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0438\u0447\u043d\u044b\u0445 \u0438 \u0434\u0440\u043e\u0431\u043d\u043e-\u0440\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445</span></p><p><span style=\" co"
                        "lor:#212529;\">\u043d\u0435\u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432.</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#212529; background-color:#ffffff;\">\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2. \u0422\u0435\u043e\u0440\u0438\u044f \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0435\u0439. \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043f\u043e\u043d\u044f\u0442\u0438\u044f.</span></p><p><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#212529;\">\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0440\u0430\u0432\u043d\u0430 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044e \u0447\u0438\u0441\u043b\u0430 \u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0445 \u0438\u0441\u0445\u043e\u0434\u043e\u0432 \u043a\u00a0\u043e\u0431\u0449\u0435\u043c\u0443 \u0447\u0438\u0441\u043b\u0443 \u0438\u0441\u0445\u043e\u0434\u043e\u0432.</span></p><p><span style=\" color:#212529;\">\u041e\u0447\u0435\u0432\u0438\u0434\u043d\u043e, \u0447\u0442\u043e \u0432\u0435"
                        "\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043d\u0435\u00a0\u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u0435\u0434\u0438\u043d\u0438\u0446\u044b.</span></p><p><span style=\" color:#212529; background-color:#ffffff;\">p = m/n </span></p><p><span style=\" color:#212529;\">m \u2013 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0445 \u0438\u0441\u0445\u043e\u0434\u043e\u0432 </span></p><p><span style=\" color:#212529;\">n \u2013 \u043e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u0445\u043e\u0434\u043e\u0432 </span></p><p><span style=\" color:#212529;\">p \u2013 \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u044f</span></p><p><span style=\" color:#212529;\"/></p><p><span style=\" color:#212529;\">\u041d\u0430\u0447\u043d\u0435\u043c \u0441\u00a0\u0441\u0430"
                        "\u043c\u043e\u0433\u043e \u043f\u0440\u043e\u0441\u0442\u043e\u0433\u043e \u043f\u0440\u0438\u043c\u0435\u0440\u0430. \u0412\u044b\u00a0\u0431\u0440\u043e\u0441\u0430\u0435\u0442\u0435 \u043c\u043e\u043d\u0435\u0442\u043a\u0443. \u041e\u0440\u0435\u043b \u0438\u043b\u0438 \u0440\u0435\u0448\u043a\u0430?</span></p><p><span style=\" color:#212529;\">\u0422\u0430\u043a\u043e\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u0438\u0432\u0435\u0441\u0442\u0438 \u043a\u00a0\u043e\u0434\u043d\u043e\u043c\u0443 \u0438\u0437\u00a0\u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432, \u0432\u00a0\u0442\u0435\u043e\u0440\u0438\u0438</span></p><p><span style=\" color:#212529;\"> \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0435\u0439 \u043d\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u00a0</span><span style=\" font-family:'Arial','sans-serif"
                        "'; font-style:italic; color:#212529;\">\u0438\u0441\u043f\u044b\u0442\u0430\u043d\u0438\u0435\u043c</span><span style=\" color:#212529;\">.</span></p><p><span style=\" color:#212529;\">\u041e\u0440\u0435\u043b \u0438\u00a0\u0440\u0435\u0448\u043a\u0430\u00a0\u2014 \u0434\u0432\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445\u00a0</span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#212529;\">\u0438\u0441\u0445\u043e\u0434\u0430</span><span style=\" color:#212529;\">\u00a0\u0438\u0441\u043f\u044b\u0442\u0430\u043d\u0438\u044f.</span></p><p><span style=\" color:#212529;\">\u041e\u0440\u0435\u043b \u0432\u044b\u043f\u0430\u0434\u0435\u0442 \u0432\u00a0\u043e\u0434\u043d\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u0438\u0437\u00a0\u0434\u0432\u0443\u0445 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445. \u0413\u043e\u0432\u043e\u0440\u044f\u0442, \u0447\u0442\u043e\u00a0</span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#212529;\">"
                        "\u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c</span><span style=\" color:#212529;\">\u00a0\u0442\u043e\u0433\u043e, \u0447\u0442\u043e</span></p><p><span style=\" color:#212529;\"> \u043c\u043e\u043d\u0435\u0442\u043a\u0430 \u0443\u043f\u0430\u0434\u0435\u0442 \u043e\u0440\u043b\u043e\u043c, \u0440\u0430\u0432\u043d\u0430\u00a0 1/2</span></p><p><span style=\" color:#212529;\">\u0411\u0440\u043e\u0441\u0438\u043c \u0438\u0433\u0440\u0430\u043b\u044c\u043d\u0443\u044e \u043a\u043e\u0441\u0442\u044c. \u0423\u00a0\u043a\u0443\u0431\u0438\u043a\u0430 \u0448\u0435\u0441\u0442\u044c \u0433\u0440\u0430\u043d\u0435\u0439, \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u0438\u0441\u0445\u043e\u0434\u043e\u0432 \u0442\u043e\u0436\u0435 \u0448\u0435\u0441\u0442\u044c.</span></p><p><span style=\" color:#212529;\">\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0432\u044b\u00a0\u0437\u0430\u0433\u0430\u0434\u0430\u043b\u0438, \u0447\u0442\u043e \u0432"
                        "\u044b\u043f\u0430\u0434\u0435\u0442 \u0442\u0440\u0438 \u043e\u0447\u043a\u0430. \u042d\u0442\u043e \u043e\u0434\u0438\u043d \u0438\u0441\u0445\u043e\u0434 \u0438\u0437\u00a0\u0448\u0435\u0441\u0442\u0438 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445. \u0412\u00a0\u0442\u0435\u043e\u0440\u0438\u0438</span></p><p><span style=\" color:#212529;\"> \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0435\u0439 \u043e\u043d\u00a0\u0431\u0443\u0434\u0435\u0442 \u043d\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f\u00a0</span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#212529;\">\u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u043c \u0438\u0441\u0445\u043e\u0434\u043e\u043c</span><span style=\" color:#212529;\">.</span></p><p><span style=\" color:#212529;\">\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u0432\u044b\u043f\u0430\u0434\u0435\u043d\u0438\u044f \u0442\u0440\u043e\u0439\u043a\u0438 \u0440\u0430\u0432\u043d"
                        "\u0430 1/6\u00a0(\u043e\u0434\u0438\u043d \u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439 \u0438\u0441\u0445\u043e\u0434 \u0438\u0437\u00a0\u0448\u0435\u0441\u0442\u0438 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445).</span></p><p><span style=\" color:#212529;\">\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u0447\u0435\u0442\u0432\u0435\u0440\u043a\u0438\u00a0\u2014 \u0442\u043e\u0436\u0435\u00a01/6</span></p><p><span style=\" color:#212529;\">\u0410\u00a0\u0432\u043e\u0442 \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u0435\u043c\u0435\u0440\u043a\u0438 \u0440\u0430\u0432\u043d\u0430 \u043d\u0443\u043b\u044e. \u0412\u0435\u0434\u044c \u0433\u0440\u0430\u043d\u0438 \u0441\u00a0\u0441\u0435\u043c\u044c\u044e \u0442\u043e\u0447\u043a\u0430\u043c\u0438 \u043d\u0430\u00a0\u043a\u0443\u0431\u0438\u043a\u0435 \u043d\u0435\u0442.</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#333333;\">\u0417\u0430\u0434\u0430\u043d\u0438\u0435 4. \u0412\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f \u0438 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f. </span></p><p><span style=\" color:#333333;\">\u0414\u043b\u044f \u0442\u043e\u0433\u043e, \u0447\u0442\u043e\u0431\u044b \u0440\u0435\u0448\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435 \u043d\u0443\u0436\u043d\u043e \u0437\u043d\u0430\u0442\u044c \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u0439.</span></p><p><span style=\" color:#333333;\">\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c\u043e\u0432:</span></p><p><img src=\":/newPrefix/pict/pict 22.jpg\"/></p><p><span style=\" color:#333333;\">\u041e\u0441\u043d\u043e\u0432"
                        "\u043d\u044b\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u0441\u0442\u0435\u043f\u0435\u043d\u0435\u0439:</span></p><p><img src=\":/newPrefix/pict/pict23.jpg\"/></p><p><span style=\" color:#333333;\">\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043a\u043e\u0440\u043d\u0435\u0439:</span></p><p><img src=\":/newPrefix/pict/pict24.jpg\"/></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u0430\u0434\u0430\u043d\u0438\u0435 7. \u0417\u0430\u0434\u0430\u0447\u0438 \u0441 \u043f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u044b\u043c \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435\u043c. </p><p>\u041c\u043e\u0436\u043d\u043e \u0441\u043a\u0430\u0437\u0430\u0442\u044c \u0447\u0442\u043e \u044d\u0442\u043e \u0437\u0430\u0434\u0430\u0447\u0438 \u043f\u043e \u0444\u0438\u0437\u0438\u043a\u0435, \u0430 \u043d\u0435 \u043f\u043e \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0435, \u043d\u043e \u0432\u0441\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0444\u043e\u0440\u043c\u0443\u043b\u044b \u0438 \u0432\u0435\u043b\u0438\u0447\u0438\u043d\u044b \u0434\u0430\u043d\u044b \u0432 \u0443\u0441\u043b\u043e\u0432\u0438\u0438. \u0417\u0430\u0434\u0430\u0447\u0438</p><p>\u0441\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u043a \u0440\u0435\u0448\u0435\u043d\u0438\u044e \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u0438\u043b"
                        "\u0438 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f, \u043b\u0438\u0431\u043e \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u0438\u043b\u0438 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0433\u043e \u043d\u0435\u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432\u0430. \u041f\u043e\u044d\u0442\u043e\u043c\u0443 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e</p><p>\u0443\u043c\u0435\u0442\u044c \u0440\u0435\u0448\u0430\u0442\u044c \u0442\u0430\u043a\u0438\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0438 \u043d\u0435\u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432\u0430, \u0438 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0442\u044c \u043e\u0442\u0432\u0435\u0442. \u041e\u0442\u0432\u0435\u0442 \u0432 \u043b\u044e\u0431\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u0434\u043e\u043b\u0436\u0435\u043d \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c\u0441\u044f \u0432 \u0432\u0438"
                        "\u0434\u0435 \u0446\u0435\u043b\u043e\u0433\u043e</p><p>\u0447\u0438\u0441\u043b\u0430 \u0438\u043b\u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0439 \u0434\u0435\u0441\u044f\u0442\u0438\u0447\u043d\u043e\u0439 \u0434\u0440\u043e\u0431\u0438. </p><p>\u041d\u0430 \u0447\u0442\u043e \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u0435: </p><p>\u0415\u0441\u043b\u0438 \u0432 \u0432\u043e\u043f\u0440\u043e\u0441\u0435 \u043f\u0440\u043e\u0437\u0432\u0443\u0447\u0430\u043b\u043e \u00ab\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043d\u0430\u0438\u0431\u043e\u043b\u044c\u0448\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u00bb, \u00ab\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u043d\u0430\u0438\u043c\u0435\u043d\u044c\u0448\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\u00bb, \u0442\u043e</p><p> \u0437\u0430\u0434\u0430\u0447\u0430 \u0432 \u0431"
                        "\u043e\u043b\u044c\u0448\u0438\u043d\u0441\u0442\u0432\u0435 \u0441\u043b\u0443\u0447\u0430\u0435\u0432 \u0440\u0435\u0448\u0430\u0435\u0442\u0441\u044f \u0447\u0435\u0440\u0435\u0437 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u0435\u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432\u0430. </p><p>\u00a0\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0439\u0442\u0435 \u0437\u043d\u0430\u043a \u043f\u0440\u0438 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u043d\u0435\u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432\u0430. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: b \u043d\u0435 \u043c\u0435\u043d\u0435\u0435 21 \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u043a\u0430\u043a b\u226521 (b \u0440\u0430\u0432\u043d\u043e \u0438\u043b\u0438</p><p>\u0431\u043e\u043b\u044c\u0448\u0435 21). </p><p>\u0415\u0441\u043b\u0438 \u0432 \u0432\u043e\u043f\u0440\u043e\u0441\u0435 \u0437\u0430"
                        "\u0434\u0430\u0447\u0438 \u043f\u0440\u043e\u0437\u0432\u0443\u0447\u0430\u043b\u043e \u00ab\u0441\u043a\u043e\u043b\u044c\u043a\u043e\u00bb, \u0442\u043e \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435. </p><p>\u041d\u0435 \u0437\u0430\u0431\u044b\u0432\u0430\u0439\u0442\u0435 \u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438 \u0435\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f, \u0435\u0441\u043b\u0438 \u044d\u0442\u043e \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e (\u043c\u0435\u0442\u0440\u044b \u0441 \u0441\u0430\u043d\u0442\u0438\u043c\u0435\u0442\u0440\u044b \u0438 \u043f\u0440.) </p><p>\u041d\u0435 \u0443\u043f\u0443\u0441\u043a\u0430\u0439\u0442\u0435 \u0438\u0437 \u0432\u0438\u0434\u0443, \u0432 \u043a\u0430\u043a\u0438\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0442\u0440\u0435\u0431\u0443"
                        "\u0435\u0442\u0441\u044f \u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0440\u0435\u0448\u0438\u0432 \u0437\u0430\u0434\u0430\u0447\u0443, </p><p>\u0432\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u043b\u0438 0,5 \u0447\u0430\u0441\u0430, \u0432 \u0443\u0441\u043b\u043e\u0432\u0438\u0438 \u0441\u043a\u0430\u0437\u0430\u043d\u043e \u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445, \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0441\u044f 30 \u043c\u0438\u043d\u0443\u0442; \u0435\u0441\u043b\u0438 \u0437\u0430\u043f\u0438\u0448\u0438\u0442\u0435</p><p> 0,5 \u2013 \u044d\u0442\u043e \u043e\u0448\u0438\u0431\u043a\u0430 \u0438 \u043f\u043e\u0442\u0435\u0440\u044f\u043d\u043d\u044b\u0439 \u0431\u0430\u043b, \u0445\u043e\u0442\u044f \u0437\u0430\u0434\u0430\u0447\u0430</p><p>\u0440\u0435\u0448\u0435\u043d\u0430, \u0432\u0435\u0440\u043d\u043e). </p></"
                        "body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u0430\u0434\u0430\u043d\u0438\u0435 6. \u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f </p><p>\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u044b\u0445 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0445 \u0444\u0443\u043d\u043a\u0446\u0438\u0439: </p><p><img src=\":/newPrefix/pict/pict25.jpg\"/></p><p>\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0434\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f: </p><p><span style=\" color:#1d1d1b; background-color:#ffffff;\">\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u0441\u0443\u043c\u043c\u044b \u0440\u0430\u0432\u043d\u0430 \u0441\u0443\u043c\u043c\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u044b\u0445: (f(x) + g(x))' = f '(x) + g'(x).</span></p><p><span style=\" color:#1d1d1b;\">\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u044b\u0439 \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b"
                        "\u044c \u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043d\u0435\u0441\u0442\u0438 \u0437\u0430 \u0437\u043d\u0430\u043a \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439:</span></p><p><span style=\" color:#1d1d1b;\">(cf(x))'=c f '(x)</span></p><p><span style=\" color:#1d1d1b; background-color:#ffffff;\">\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0440\u0430\u0432\u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044e \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044f \u043d\u0430 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043b\u044e\u0441 \u043f\u0435\u0440\u0432\u044b\u0439 \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c, \u0443\u043c\u043d\u043e\u0436\u0435\u043d\u043d\u044b\u0439 \u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0443\u044e \u0432\u0442\u043e\u0440\u043e\u0433\u043e. \u00a0\u00a0"
                        "\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0(f(x)\u00b7g(x))' = f ' (x)\u00b7g(x)+f(x)\u00b7g' (x)</span></p><p><span style=\" color:#1d1d1b; background-color:#ffffff;\">\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043d\u043e\u0433\u043e \u0440\u0430\u0432\u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439 \u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044f \u0443\u043c\u043d\u043e\u0436\u0435\u043d\u043d\u043e\u0433\u043e \u043d\u0430 \u0437\u043d\u0430\u043c\u0435\u043d\u0430\u0442\u0435\u043b\u044c \u043c\u0438\u043d\u0443\u0441 \u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c \u0443\u043c\u043d\u043e\u0436\u0435\u043d\u043d\u044b\u0439 \u043d\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0443\u044e \u0437\u043d\u0430\u043c\u0435\u043d\u0430\u0442\u0435\u043b\u044f \u0438 \u0432\u0441\u0435 \u044d\u0442\u043e \u0434\u0435\u043b"
                        "\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043a\u0432\u0430\u0434\u0440\u0430\u0442 \u0437\u043d\u0430\u043c\u0435\u043d\u0430\u0442\u0435\u043b\u044f.</span></p><p/><p><img src=\":/newPrefix/pict/pict26.jpg\"/></p><p><span style=\" color:#1d1d1b;\"/></p><p><span style=\" color:#1d1d1b;\">\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u0441\u043b\u043e\u0436\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043f\u043e \u0444\u043e\u0440\u043c\u0443\u043b\u0435: (f(g(x)))'=f '(g(x))\u00b7g' (x)</span></p><p><span style=\" color:#1d1d1b;\">\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u043c\u044b\u0441\u043b \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439:</span></p><p><span style=\" color:#1d1d1b; background-color:#ffffff;\">\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u0432 \u0442\u043e\u0447\u043a\u0435 x</span><span style=\" color:"
                        "#1d1d1b; background-color:#ffffff; vertical-align:sub;\">0</span><span style=\" color:#1d1d1b; background-color:#ffffff;\">\u00a0\u0440\u0430\u0432\u043d\u0430 \u0443\u0433\u043b\u043e\u0432\u043e\u043c\u0443 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u0443 \u043a\u0430\u0441\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043a \u0433\u0440\u0430\u0444\u0438\u043a\u0443 \u0444\u0443\u043d\u043a\u0446\u0438\u0438\u00a0</span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#1d1d1b; background-color:#ffffff;\">y</span><span style=\" color:#1d1d1b; background-color:#ffffff;\">\u00a0=\u00a0</span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#1d1d1b; background-color:#ffffff;\">f</span><span style=\" color:#1d1d1b; background-color:#ffffff;\">(</span><span style=\" font-family:'Arial','sans-serif'; font-style:italic; color:#1d1d1b; background-color:#ffffff;\">x</span><span style=\" color:#1d1d1b; background-color:#ffffff;\">) \u0432 \u044d"
                        "\u0442\u043e\u0439 \u0442\u043e\u0447\u043a\u0435.</span></p><p><span style=\" color:#1d1d1b;\">\u0424\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u043c\u044b\u0441\u043b \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439:</span></p><p><span style=\" color:#1d1d1b;\">\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u2013 \u044d\u0442\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u043f\u0443\u0442\u0438 \u043f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438.</span></p><p><span style=\" color:#1d1d1b;\">V = s\u2019(t)</span></p><p><span style=\" color:#1d1d1b;\">\u0415\u0441\u043b\u0438 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0443\u043b\u044f, \u0442\u043e \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u0435\u0442.</span></p><p><span style=\" color:#1d1d1b;\">\u0415\u0441\u043b\u0438 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d"
                        "\u0430\u044f \u043c\u0435\u043d\u044c\u0448\u0435 \u043d\u0443\u043b\u044f, \u0442\u043e \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u0443\u0431\u044b\u0432\u0430\u0435\u0442.</span></p><p><span style=\" color:#1d1d1b;\">\u0415\u0441\u043b\u0438 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u0440\u0430\u0432\u043d\u0430 \u043d\u0443\u043b\u044e, \u0442\u043e \u0434\u0430\u043d\u043d\u0430\u044f \u0442\u043e\u0447\u043a\u0430 x \u043d\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0442\u043e\u0447\u043a\u043e\u0439 \u044d\u043a\u0441\u0442\u0440\u0435\u043c\u0443\u043c\u0430.</span></p><p><span style=\" color:#1d1d1b;\">\u042d\u043a\u0441\u0442\u0440\u0435\u043c\u0443\u043c \u2013 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u043b\u0438 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043d\u0430 \u0437\u0430\u0434\u0430\u043d\u043d\u043e"
                        "\u043c \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043a\u0435.</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u0430\u0434\u0430\u043d\u0438\u0435 3. \u041f\u043b\u0430\u043d\u0438\u043c\u0435\u0442\u0440\u0438\u044f. </p><p><span style=\" font-family:'Arial','sans-serif'; color:#212529; background-color:#ffffff;\">\u0424\u043e\u0440\u043c\u0443\u043b\u044b \u043f\u043b\u043e\u0449\u0430\u0434\u0438 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0445 \u0444\u0438\u0433\u0443\u0440</span></p><p>\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>\u0427\u0435\u0440\u0435\u0437 \u0441\u0442\u043e\u0440\u043e\u043d\u0443 \u0438 \u0432\u044b\u0441\u043e\u0442\u0443 </p><p>S = \u00bd ah </p><p>a \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>h \u2013 \u0432\u044b\u0441\u043e\u0442\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430, \u043f\u0440\u043e\u0432\u0435\u0434\u0451\u043d\u043d\u0430\u044f \u043a \u0441\u0442\u043e"
                        "\u0440\u043e\u043d\u0435 a </p><p>?\u041a\u0410\u0420\u0422\u0418\u041d\u041a\u04101? </p><p>\u0427\u0435\u0440\u0435\u0437 \u0434\u0432\u0435 \u0441\u0442\u043e\u0440\u043e\u043d\u044b \u0438 \u0443\u0433\u043e\u043b \u043c\u0435\u0436\u0434\u0443 \u043d\u0438\u043c\u0438 </p><p>S = \u00bd ab sin<img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"10\" height=\"18\"/></p><p>a \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>b \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043aa </p><p><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"10\" height=\"18\"/>\u00a0\u2013 \u0443\u0433\u043e\u043b \u043c\u0435\u0436\u0434\u0443 \u0441\u0442\u043e\u0440\u043e\u043d\u0430\u043c\u0438 a \u0438 b </p><p><img src=\":/newPrefix/pict/pict2.jpg\"/></p><p>\u0424\u043e\u0440\u043c\u0443\u043b\u0430"
                        " \u0413\u0435\u0440\u043e\u043d\u0430 </p><p><img src=\":/newPrefix/pict/pict3.jpg\"/></p><p>a \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>b \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>c \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>p \u2013 \u043f\u043e\u043b\u0443\u043f\u0435\u0440\u0438\u043c\u0435\u0442\u0440 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430, p = \u00bd(a+b+c) </p><p><img src=\":/newPrefix/pict/pict4.jpg\"/></p><p>\u0427\u0435\u0440\u0435\u0437 \u0440\u0430\u0434\u0438\u0443\u0441 \u0432\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0439 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438 </p><p>S = pr </p><p>p \u2013 \u043f\u043e\u043b\u0443\u043f\u0435\u0440\u0438\u043c\u0435\u0442\u0440 \u0442\u0440\u0435\u0443"
                        "\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>r \u2013 \u0440\u0430\u0434\u0438\u0443\u0441 \u0432\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0439 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p><img src=\":/newPrefix/pict/pict5.jpg\"/></p><p>\u0427\u0435\u0440\u0435\u0437 \u0440\u0430\u0434\u0438\u0443\u0441 \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0439 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438 </p><p><img src=\":/newPrefix/pict/pict6.jpg\"/></p><p>R \u2013 \u0440\u0430\u0434\u0438\u0443\u0441 \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0439 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438 </p><p>a \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>b \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>c \u2013"
                        " \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 </p><p>\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430 </p><p>S = ah </p><p>a \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430 </p><p>h \u2013 \u0432\u044b\u0441\u043e\u0442\u0430 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430, \u043f\u0440\u043e\u0432\u0435\u0434\u0451\u043d\u043d\u0430\u044f \u043a \u0441\u0442\u043e\u0440\u043e\u043d\u0435 a </p><p><img src=\":/newPrefix/pict/pict7.jpg\"/></p><p>S = ab sin<img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"10\" height=\"18\"/></p><p>a \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430 </p><p>b"
                        " \u2013 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430 </p><p><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"10\" height=\"18\"/>\u00a0\u2013 \u0443\u0433\u043e\u043b \u043c\u0435\u0436\u0434\u0443 a \u0438 b </p><p><img src=\":/newPrefix/pict/pict8.jpg\"/></p><p><img src=\":/newPrefix/pict/pict9.jpg\"/></p><p><img src=\":/newPrefix/pict/pict10.jpg\"/></p><p>\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438 </p><p>S = \u00bd (a+b)h </p><p><img src=\":/newPrefix/pict/pict11.jpg\"/></p><p>\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043b\u0438\u043d\u0438\u044f \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 \u0438 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438. </p><p><span style=\" font-family:'Arial','sans-serif'; font-weight:600; color:#333333;\">\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043b\u0438\u043d"
                        "\u0438\u044f \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430\u00a0</span><span style=\" color:#333333;\">- \u044d\u0442\u043e \u043e\u0442\u0440\u0435\u0437\u043e\u043a, \u0441\u043e\u0435\u0434\u0438\u043d\u044f\u044e\u0449\u0438\u0439 \u0441\u0435\u0440\u0435\u0434\u0438\u043d\u044b \u0434\u0432\u0443\u0445 \u0435\u0433\u043e \u0441\u0442\u043e\u0440\u043e\u043d.</span></p><p><img src=\":/newPrefix/pict/pict12.jpg\"/></p><p><span style=\" color:#333333;\">\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043b\u0438\u043d\u0438\u044f \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u044c\u043d\u0430 \u0442\u0440\u0435\u0442\u044c\u0435\u0439 \u0441\u0442\u043e\u0440\u043e\u043d\u0435, \u0430 \u0435\u0435 \u0434\u043b\u0438\u043d\u0430 \u0440\u0430\u0432\u043d\u0430 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0435 \u0434\u043b\u0438\u043d\u044b</span></p><p><span style=\" color:#333333;\"> \u044d\u0442\u043e\u0439 \u0441"
                        "\u0442\u043e\u0440\u043e\u043d\u044b.</span></p><p><span style=\" font-family:'Arial','sans-serif'; font-weight:600; color:#333333;\">\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043b\u0438\u043d\u0438\u044f \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438\u00a0</span><span style=\" color:#333333;\">- \u044d\u0442\u043e \u043e\u0442\u0440\u0435\u0437\u043e\u043a, \u0441\u043e\u0435\u0434\u0438\u043d\u044f\u044e\u0449\u0438\u0439 \u0441\u0435\u0440\u0435\u0434\u0438\u043d\u044b \u0435\u0451 \u0431\u043e\u043a\u043e\u0432\u044b\u0445 \u0441\u0442\u043e\u0440\u043e\u043d.</span></p><p><img src=\":/newPrefix/pict/pict13.jpg\"/></p><p><span style=\" color:#333333;\">\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043b\u0438\u043d\u0438\u044f \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438 \u0440\u0430\u0432\u043d\u0430 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0435 \u0441\u0443\u043c\u043c\u044b \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0439.</span></p><p><span style=\" color:#333333;\">m = </span>\u00bd(a+"
                        "b) </p><p><span style=\" color:#333333;\">m \u2013 \u0441\u0440\u0435\u0434\u043d\u044f\u044f \u043b\u0438\u043d\u0438\u044f \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438</span></p><p><span style=\" color:#333333;\">a \u0438 b \u2013 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438</span></p><p><span style=\" color:#333333;\">\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043b\u0438\u043d\u0438\u044f \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438 \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u044c\u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f\u043c \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0438.</span></p><p><span style=\" color:#333333;\">\u0422\u0435\u043e\u0440\u0435\u043c\u0430 \u0441\u0438\u043d\u0443\u0441\u043e\u0432. </span></p><p><img src=\":/newPrefix/pict/pict14.png\"/></p><p><span style=\" color:#333333;\">\u0422\u0435\u043e\u0440\u0435\u043c\u0430 \u043a\u043e\u0441\u0438\u043d\u0443\u0441\u043e\u0432. </span></p><"
                        "p><img src=\":/newPrefix/pict/pict15.jpg\"/></p><p><img src=\":/newPrefix/pict/pict16.jpg\"/></p><p><span style=\" color:#333333;\">\u0412\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0435 \u0438 \u0446\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0443\u0433\u043b\u044b.</span></p><p><img src=\":/newPrefix/pict/pict17.jpg\"/></p><p><span style=\" color:#333333;\">\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0443\u0433\u043e\u043b \u2013 \u0443\u0433\u043e\u043b \u0441 \u0432\u0435\u0440\u0448\u0438\u043d\u043e\u0439 \u0432 \u0446\u0435\u043d\u0442\u0440\u0435 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438, \u0441\u0442\u043e\u0440\u043e\u043d\u044b \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0440\u043e\u0445\u043e\u0434\u044f\u0442 \u0447\u0435\u0440\u0435\u0437</span></p><p><span style=\" color:#333333;\"> \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c.</span></p><p><span style=\" color:#333333;\">\u0412\u043f\u0438\u0441\u0430\u043d"
                        "\u043d\u044b\u0439 \u0443\u0433\u043e\u043b \u2013 \u0443\u0433\u043e\u043b, \u0432\u0435\u0440\u0448\u0438\u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043b\u0435\u0436\u0438\u0442 \u043d\u0430 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438, \u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u044b \u043f\u0435\u0440\u0435\u0441\u0435\u043a\u0430\u044e\u0442 \u0434\u0430\u043d\u043d\u0443\u044e</span></p><p><span style=\" color:#333333;\"> \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c.</span></p><p><span style=\" color:#333333;\">\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0443\u0433\u043e\u043b \u0440\u0430\u0432\u0435\u043d \u0433\u0440\u0430\u0434\u0443\u0441\u043d\u043e\u0439 \u043c\u0435\u0440\u0435 \u0434\u0443\u0433\u0438 \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043e\u043f\u0438\u0440\u0430\u0435\u0442\u0441\u044f. </span></p><p><span style=\" color:#333333;\">\u0412\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0439 \u0443\u0433"
                        "\u043e\u043b \u0440\u0430\u0432\u0435\u043d \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0435 \u0433\u0440\u0430\u0434\u0443\u0441\u043d\u043e\u0439 \u043c\u0435\u0440\u044b \u0434\u0443\u0433\u0438, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043e\u043f\u0438\u0440\u0430\u0435\u0442\u0441\u044f. </span></p><p><span style=\" color:#333333;\">\u0412\u0441\u0435 \u0432\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b, \u043e\u043f\u0438\u0440\u0430\u044e\u0449\u0438\u0435\u0441\u044f \u043d\u0430 \u043e\u0434\u043d\u0443 \u0434\u0443\u0433\u0443, \u0440\u0430\u0432\u043d\u044b.</span></p><p><span style=\" color:#333333;\">\u0412\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0439 \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a. \u041f\u0440\u0438\u0437\u043d\u0430\u043a\u0438 \u0438 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430.</span></p><p><span style=\" color:#333333;\">\u0412\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0439 \u0447\u0435"
                        "\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a \u2013 \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a \u0432\u0435\u0440\u0448\u0438\u043d\u044b \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043b\u0435\u0436\u0430\u0442 \u043d\u0430 \u043e\u0434\u043d\u043e\u0439 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438. </span></p><p><span style=\" color:#333333;\">\u0415\u0441\u043b\u0438 \u0441\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u043f\u043e\u043b\u043e\u0436\u043d\u044b\u0445 \u0443\u0433\u043b\u043e\u0432 \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 \u0440\u0430\u0432\u043d\u0430 180 \u0433\u0440\u0430\u0434\u0443\u0441\u0430\u043c, \u0442\u043e \u0434\u0430\u043d\u043d\u044b\u0439</span></p><p><span style=\" color:#333333;\"> \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a \u0432\u043f\u0438\u0441\u0430"
                        "\u043d\u043d\u044b\u0439. \u0423\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u0432\u0435\u0440\u043d\u043e \u0438 \u0432 \u043e\u0431\u0440\u0430\u0442\u043d\u0443\u044e \u0441\u0442\u043e\u0440\u043e\u043d\u0443.</span></p><p><img src=\":/newPrefix/pict/pict18.jpg\"/></p><p><img src=\":/newPrefix/pict/pict19.jpg\"/></p><p><span style=\" color:#333333;\">\u0415\u0441\u043b\u0438 \u0443\u0433\u043e\u043b </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png\" width=\"10\" height=\"18\"/><span style=\" color:#333333;\">\u00a0\u0440\u0430\u0432\u0435\u043d \u0443\u0433\u043b\u0443 </span><img src=\"file:///C:/Users/Asus/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png\" width=\"10\" height=\"18\"/><span style=\" color:#333333;\">\u00a0\u0442\u043e \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a \u0432\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0439. \u0423\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435"
                        " \u0432\u0435\u0440\u043d\u043e \u0438 \u0432 \u043e\u0431\u0440\u0430\u0442\u043d\u0443\u044e</span></p><p><span style=\" color:#333333;\"> \u0441\u0442\u043e\u0440\u043e\u043d\u0443. </span></p><p><span style=\" color:#333333;\">\u041e\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0439 \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a. </span></p><p><span style=\" color:#333333;\">\u041e\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0439 \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a \u2013 \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043c\u043e\u0436\u043d\u043e \u0432\u043f\u0438\u0441\u0430\u0442\u044c \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c. </span></p><p><img src=\":/newPrefix/pict/pict20.jpg\"/></p><p><span style=\" color:#333333;\">\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u0441\u0432\u043e\u0439\u0441\u0442"
                        "\u0432\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0433\u043e \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430: \u0441\u0443\u043c\u043c\u044b \u0434\u043b\u0438\u043d \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u043f\u043e\u043b\u043e\u0436\u043d\u044b\u0445 \u0441\u0442\u043e\u0440\u043e\u043d \u0440\u0430\u0432\u043d\u044b. </span></p><p><span style=\" color:#333333;\">a + c = b + d </span></p><p><img src=\":/newPrefix/pict/pict21.jpg\"/></p><p><span style=\" color:#333333;\">\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0433\u043e \u0447\u0435\u0442\u044b\u0440\u0451\u0445\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043a\u0430\u043a \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0443\u043f\u0435\u0440\u0438\u043c\u0435\u0442\u0440\u0430 \u043d\u0430 \u0440\u0430\u0434\u0438\u0443\u0441</span"
                        "></p><p><span style=\" color:#333333;\"> \u0432\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0439 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438.</span></p></body></html>", None))
    # retranslateUi

