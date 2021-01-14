# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainiAtyhc.ui'
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
        MainWindow.resize(950, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QFrame(self.centralwidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setStyleSheet(u"background-color: rgb(237, 237, 237);")
        self.main_layout.setFrameShape(QFrame.NoFrame)
        self.main_layout.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.main_layout)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.right_side_frame = QFrame(self.main_layout)
        self.right_side_frame.setObjectName(u"right_side_frame")
        self.right_side_frame.setMinimumSize(QSize(500, 0))
        self.right_side_frame.setFrameShape(QFrame.NoFrame)
        self.right_side_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.right_side_frame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 5, 9)
        self.frame_7 = QFrame(self.right_side_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_title = QPushButton(self.frame_7)
        self.header_title.setStyleSheet('border: none; color: rgb(255,0,0);text-align: left')
        self.header_title.setCursor(QCursor(Qt.PointingHandCursor))
        self.header_title.setObjectName(u"header_title")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header_title.setFont(font)
        #self.header_title.setIndent(10)

        self.horizontalLayout_2.addWidget(self.header_title, 0, Qt.AlignLeft)

        self.countries_select = QComboBox(self.frame_7)
        self.countries_select.setObjectName(u"countries_select")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countries_select.sizePolicy().hasHeightForWidth())
        self.countries_select.setSizePolicy(sizePolicy)
        self.countries_select.setMinimumSize(QSize(120, 0))
        self.countries_select.setMaximumSize(QSize(16777215, 40))
        self.countries_select.setStyleSheet(u"border: 1px solid;border-radius: 4px;color: rgb(1,1,1);QComboBox::down-arrow {image: url('./style/rc/arrow_down_disabled.png');height: 8px;width: 8px;}")

        self.horizontalLayout_2.addWidget(self.countries_select)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.info_boxes_frame = QFrame(self.right_side_frame)
        self.info_boxes_frame.setObjectName(u"info_boxes_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_boxes_frame.sizePolicy().hasHeightForWidth())
        self.info_boxes_frame.setSizePolicy(sizePolicy1)
        self.info_boxes_frame.setMinimumSize(QSize(0, 0))
        self.info_boxes_frame.setMaximumSize(QSize(16777215, 130))
        self.info_boxes_frame.setFrameShape(QFrame.NoFrame)
        self.info_boxes_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.info_boxes_frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.frame_3 = QFrame(self.info_boxes_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"\n"
"QFrame{\n"
"	border: 3px solid;\n"
"	border-radius: 13px;\n"
"	border-color: rgb(255, 0,0);\n"
"	background-color: rgb(248, 248, 246);\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.covid_cases = QLabel(self.frame_3)
        self.covid_cases.setObjectName(u"covid_cases")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.covid_cases.setFont(font1)
        self.covid_cases.setStyleSheet(u"color: rgb(254, 0, 0);")
        self.covid_cases.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.covid_cases)

        self.covid_cases_inc = QLabel(self.frame_3)
        self.covid_cases_inc.setObjectName(u"covid_cases_inc")
        font2 = QFont()
        font2.setFamily(u"Ubuntu Light")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.covid_cases_inc.setFont(font2)
        self.covid_cases_inc.setStyleSheet(u"color: rgb(164, 0, 0);")
        self.covid_cases_inc.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.covid_cases_inc)

        self.covid_cases_tot = QLabel(self.frame_3)
        self.covid_cases_tot.setObjectName(u"covid_cases_tot")
        font3 = QFont()
        font3.setFamily(u"Ubuntu")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setKerning(True)
        self.covid_cases_tot.setFont(font3)
        self.covid_cases_tot.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.covid_cases_tot)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.info_boxes_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"\n"
"QFrame{\n"
"	border: 3px solid;\n"
"	border-radius: 13px;\n"
"	border-color: rgb(0, 255,0);\n"
"	background-color: rgb(248, 248, 246);\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.recovered = QLabel(self.frame_4)
        self.recovered.setObjectName(u"recovered")
        self.recovered.setFont(font1)
        self.recovered.setStyleSheet(u"color: rgb(0,250, 0);")
        self.recovered.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.recovered)

        self.recovered_cases_inc = QLabel(self.frame_4)
        self.recovered_cases_inc.setObjectName(u"recovered_cases_inc")
        self.recovered_cases_inc.setFont(font2)
        self.recovered_cases_inc.setStyleSheet(u"color: rgb(0, 230, 0);")
        self.recovered_cases_inc.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_3.addWidget(self.recovered_cases_inc)

        self.recovered_cases_tot = QLabel(self.frame_4)
        self.recovered_cases_tot.setObjectName(u"recovered_cases_tot")
        font4 = QFont()
        font4.setFamily(u"Ubuntu")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.recovered_cases_tot.setFont(font4)
        self.recovered_cases_tot.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_3.addWidget(self.recovered_cases_tot)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.info_boxes_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(100, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	border: 3px solid;\n"
"	border-radius: 13px;\n"
"	border-color: rgb(255, 0,0);\n"
"	background-color: rgb(248, 248, 246);\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.deaths = QLabel(self.frame_5)
        self.deaths.setObjectName(u"deaths")
        self.deaths.setFont(font1)
        self.deaths.setStyleSheet(u"color: rgb(254, 0, 0);")
        self.deaths.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.deaths)

        self.death_cases_inc = QLabel(self.frame_5)
        self.death_cases_inc.setObjectName(u"death_cases_inc")
        self.death_cases_inc.setFont(font2)
        self.death_cases_inc.setStyleSheet(u"color: rgb(164, 0, 0);")
        self.death_cases_inc.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.death_cases_inc)

        self.death_cases_tot = QLabel(self.frame_5)
        self.death_cases_tot.setObjectName(u"death_cases_tot")
        self.death_cases_tot.setFont(font4)
        self.death_cases_tot.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.death_cases_tot)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.info_boxes_frame)

        self.frame_6 = QFrame(self.right_side_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"\n"
"QFrame{\n"
"	border: 10px solid;\n"
"	border-radius: 13px;\n"
"	border-color: rgb(255, 255,255)\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0,0,0,0)
        # self.map_placeholder = QLabel(self.frame_6)
        # self.map_placeholder.setObjectName(u"map_placeholder")
        # self.map_placeholder.setAlignment(Qt.AlignCenter)

        # self.verticalLayout_5.addWidget(self.map_placeholder)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.right_side_frame)

        self.left_side_frame = QFrame(self.main_layout)
        self.left_side_frame.setObjectName(u"left_side_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_side_frame.sizePolicy().hasHeightForWidth())
        self.left_side_frame.setSizePolicy(sizePolicy2)
        self.left_side_frame.setMinimumSize(QSize(300, 0))
        self.left_side_frame.setMaximumSize(QSize(500, 16777215))
        self.left_side_frame.setFrameShape(QFrame.NoFrame)
        self.left_side_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.left_side_frame)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.countries_table_frame = QFrame(self.left_side_frame)
        self.countries_table_frame.setObjectName(u"countries_table_frame")
        self.countries_table_frame.setMinimumSize(QSize(0, 260))
        self.countries_table_frame.setStyleSheet(u"\n"
"QFrame{\n"
"	border: 8px solid;\n"
"	border-radius: 13px;\n"
"	border-color: rgb(255, 255,255)\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.countries_table_frame.setFrameShape(QFrame.NoFrame)
        self.countries_table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.countries_table_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.countries_table_title = QLabel(self.countries_table_frame)
        self.countries_table_title.setObjectName(u"countries_table_title")
        self.countries_table_title.setMinimumSize(QSize(0, 30))
        self.countries_table_title.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setWeight(50)
        self.countries_table_title.setFont(font5)
        self.countries_table_title.setIndent(10)

        self.verticalLayout_9.addWidget(self.countries_table_title)

        self.countries_cases_table = QTableWidget(self.countries_table_frame)
        self.countries_cases_table.setObjectName(u"countries_cases_table")
        self.countries_cases_table.setStyleSheet(u"border: none;")

        self.verticalLayout_9.addWidget(self.countries_cases_table)


        self.verticalLayout_7.addWidget(self.countries_table_frame)

        self.frame_2 = QFrame(self.left_side_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 240))
        self.frame_2.setMaximumSize(QSize(16777215, 300))
        self.frame_2.setStyleSheet(u"\n"
"QFrame{\n"
"	border: 8px solid;\n"
"	border-radius: 13px;\n"
"	border-color: rgb(255, 255,255)\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.graph_title = QLabel(self.frame_2)
        self.graph_title.setObjectName(u"graph_title")
        self.graph_title.setMinimumSize(QSize(0, 30))
        self.graph_title.setMaximumSize(QSize(16777215, 30))
        self.graph_title.setFont(font5)
        self.graph_title.setIndent(10)

        self.verticalLayout_8.addWidget(self.graph_title)

        # self.graph_placeholder = QLabel(self.frame_2)
        # self.graph_placeholder.setObjectName(u"graph_placeholder")
        # self.graph_placeholder.setAlignment(Qt.AlignCenter)

        # self.verticalLayout_8.addWidget(self.graph_placeholder)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_side_frame)


        self.verticalLayout.addWidget(self.main_layout)

        with open('./style/table_style.qss', 'r') as f:
            MainWindow.setStyleSheet(f.read())

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"COVID-19 TRACKER", None))
        self.header_title.setText(QCoreApplication.translate("MainWindow", u"COVID-19 TRACKER", None))
        self.covid_cases.setText(QCoreApplication.translate("MainWindow", u"COVID CASES", None))
        self.covid_cases_inc.setText(QCoreApplication.translate("MainWindow", u"+105.6k", None))
        self.covid_cases_tot.setText(QCoreApplication.translate("MainWindow", u"14.3M Total", None))
        self.recovered.setText(QCoreApplication.translate("MainWindow", u"RECOVERED", None))
        self.recovered_cases_inc.setText(QCoreApplication.translate("MainWindow", u"+1.2k", None))
        self.recovered_cases_tot.setText(QCoreApplication.translate("MainWindow", u"+1.3M Total", None))
        self.deaths.setText(QCoreApplication.translate("MainWindow", u"DEATHES", None))
        self.death_cases_inc.setText(QCoreApplication.translate("MainWindow", u"+2.2k", None))
        self.death_cases_tot.setText(QCoreApplication.translate("MainWindow", u"+1.6M Total", None))
        # self.map_placeholder.setText(QCoreApplication.translate("MainWindow", u"MAP", None))
        self.countries_table_title.setText(QCoreApplication.translate("MainWindow", u"Live Cases by Country", None))
        self.graph_title.setText(QCoreApplication.translate("MainWindow", u"Worldwide New Cases", None))
        # self.graph_placeholder.setText(QCoreApplication.translate("MainWindow", u"GRAPH", None))
    # retranslateUi

