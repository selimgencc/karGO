# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main 11meUrbh.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QListWidget, QListWidgetItem,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QTextEdit, QVBoxLayout, QWidget, QTextBrowser)

from Backend.informations import all_shipments,customers_list,Customer
from datetime import datetime
from Backend.informations import ShipmentSorter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QSize(800, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font = QFont()
        font.setFamilies([u"Segoe UI Light"])
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset 53.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/max.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/closeAsset 43.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(80, 55))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/homeAsset 46.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_home.setIcon(icon4)
        self.bn_home.setIconSize(QSize(22, 22))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_cloud = QFrame(self.frame_bottom_west)
        self.frame_cloud.setObjectName(u"frame_cloud")
        self.frame_cloud.setMinimumSize(QSize(80, 55))
        self.frame_cloud.setMaximumSize(QSize(160, 55))
        self.frame_cloud.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_cloud.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_cloud = QPushButton(self.frame_cloud)
        self.bn_cloud.setObjectName(u"bn_cloud")
        self.bn_cloud.setMinimumSize(QSize(80, 55))
        self.bn_cloud.setMaximumSize(QSize(160, 55))
        self.bn_cloud.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/cloudAsset 48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_cloud.setIcon(icon5)
        self.bn_cloud.setIconSize(QSize(22, 12))
        self.bn_cloud.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_cloud)


        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_android = QFrame(self.frame_bottom_west)
        self.frame_android.setObjectName(u"frame_android")
        self.frame_android.setMinimumSize(QSize(80, 55))
        self.frame_android.setMaximumSize(QSize(160, 55))
        self.frame_android.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_android.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_android = QPushButton(self.frame_android)
        self.bn_android.setObjectName(u"bn_android")
        self.bn_android.setMinimumSize(QSize(80, 55))
        self.bn_android.setMaximumSize(QSize(160, 55))
        self.bn_android.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/androidAsset 49.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_android.setIcon(icon6)
        self.bn_android.setIconSize(QSize(20, 22))
        self.bn_android.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_android)


        self.verticalLayout_3.addWidget(self.frame_android)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_home)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_home_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.lab_home_main_hed = QLabel(self.frame_home_main)
        self.lab_home_main_hed.setObjectName(u"lab_home_main_hed")
        self.lab_home_main_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_main_hed.setMaximumSize(QSize(16777215, 55))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semilight"])
        font1.setPointSize(24)
        self.lab_home_main_hed.setFont(font1)
        self.lab_home_main_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_main_hed.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout_5.addWidget(self.lab_home_main_hed)

        self.listWidget_2 = QListWidget(self.frame_home_main)
        self.listWidget_2.setObjectName(u"listWidget_2")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 217))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(91, 90, 90, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.listWidget_2.setPalette(palette)

        self.verticalLayout_5.addWidget(self.listWidget_2)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFrameShape(QFrame.Shape.VLine)
        self.vert_divide.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_home)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        self.frame_home_stat.setMinimumSize(QSize(400, 0))
        self.frame_home_stat.setMaximumSize(QSize(220, 16777215))
        self.frame_home_stat.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_home_stat)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.lab_home_stat_hed = QLabel(self.frame_home_stat)
        self.lab_home_stat_hed.setObjectName(u"lab_home_stat_hed")
        self.lab_home_stat_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_stat_hed.setMaximumSize(QSize(16777215, 55))
        self.lab_home_stat_hed.setFont(font1)
        self.lab_home_stat_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_stat_hed.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lab_home_stat_hed)

        self.listWidget_3 = QListWidget(self.frame_home_stat)
        self.listWidget_3.setObjectName(u"listWidget_3")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.listWidget_3.setPalette(palette1)

        self.verticalLayout_6.addWidget(self.listWidget_3)


        self.horizontalLayout_19.addWidget(self.frame_home_stat)

        self.stackedWidget.addWidget(self.page_home)
        self.page_about_home = QWidget()
        self.page_about_home.setObjectName(u"page_about_home")
        self.page_about_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_13 = QVBoxLayout(self.page_about_home)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_about_home)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(24)
        self.lab_about_home.setFont(font2)
        self.lab_about_home.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_home = QFrame(self.page_about_home)
        self.frame_about_home.setObjectName(u"frame_about_home")
        self.frame_about_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_about_home.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_home)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_about_home = QTextBrowser(self.frame_about_home)
        self.text_about_home.setObjectName(u"text_about_home")
        self.text_about_home.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.text_about_home.setFont(font3)
        self.text_about_home.setStyleSheet(u"color:rgb(255,255,255);")
        self.text_about_home.setFrameShape(QFrame.Shape.NoFrame)
        self.text_about_home.setFrameShadow(QFrame.Shadow.Plain)
        self.text_about_home.setReadOnly(True)
        self.text_about_home.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_about_home)


        self.verticalLayout_13.addWidget(self.frame_about_home)

        self.stackedWidget.addWidget(self.page_about_home)
        self.page_about_cloud = QWidget()
        self.page_about_cloud.setObjectName(u"page_about_cloud")
        self.page_about_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cloud)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.stackedWidget.addWidget(self.page_about_cloud)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName(u"page_about_android")
        self.page_about_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName(u"page_about_bug")
        self.page_about_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_bug)
        self.page_cloud = QWidget()
        self.page_cloud.setObjectName(u"page_cloud")
        self.page_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cloud)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.lab_cloud_main = QLabel(self.page_cloud)
        self.lab_cloud_main.setObjectName(u"lab_cloud_main")
        self.lab_cloud_main.setMinimumSize(QSize(0, 55))
        self.lab_cloud_main.setMaximumSize(QSize(16777215, 55))
        self.lab_cloud_main.setFont(font2)
        self.lab_cloud_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.lab_cloud_main)

        self.frame_2 = QFrame(self.page_cloud)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 300))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        self.frame_2.setFont(font4)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(14)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.bn_cloud_clear = QPushButton(self.frame_2)
        self.bn_cloud_clear.setObjectName(u"bn_cloud_clear")
        self.bn_cloud_clear.setEnabled(True)
        self.bn_cloud_clear.clicked.connect(self.load_button_click_3)
        self.bn_cloud_clear.setMinimumSize(QSize(69, 25))
        self.bn_cloud_clear.setMaximumSize(QSize(69, 25))
        self.bn_cloud_clear.setFont(font4)
        self.bn_cloud_clear.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_cloud_clear, 0, 4, 1, 1)

        self.line_cloud_id = QLineEdit(self.frame_2)
        self.line_cloud_id.setObjectName(u"line_cloud_id")
        self.line_cloud_id.setEnabled(True)
        self.line_cloud_id.setMinimumSize(QSize(400, 25))
        self.line_cloud_id.setMaximumSize(QSize(500, 25))
        self.line_cloud_id.setFont(font4)
        self.line_cloud_id.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_cloud_id, 0, 1, 1, 3)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.listWidget = QListWidget(self.page_cloud)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 300))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.listWidget.setPalette(palette2)

        self.verticalLayout_8.addWidget(self.listWidget)

        self.stackedWidget.addWidget(self.page_cloud)
        self.page_android = QWidget()
        self.page_android.setObjectName(u"page_android")
        self.page_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_android)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_android_menu = QFrame(self.page_android)
        self.frame_android_menu.setObjectName(u"frame_android_menu")
        self.frame_android_menu.setMinimumSize(QSize(0, 30))
        self.frame_android_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_android_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_android_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_android_menu.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_android_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_android_contact = QFrame(self.frame_android_menu)
        self.frame_android_contact.setObjectName(u"frame_android_contact")
        self.frame_android_contact.setMinimumSize(QSize(80, 30))
        self.frame_android_contact.setMaximumSize(QSize(80, 30))
        self.frame_android_contact.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_android_contact.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_android_contact)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bn_android_contact = QPushButton(self.frame_android_contact)
        self.bn_android_contact.setObjectName(u"bn_android_contact")
        self.bn_android_contact.setMinimumSize(QSize(80, 30))
        self.bn_android_contact.setMaximumSize(QSize(80, 30))
        self.bn_android_contact.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/bookAsset 57.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_android_contact.setIcon(icon7)
        self.bn_android_contact.setIconSize(QSize(13, 16))
        self.bn_android_contact.setFlat(True)

        self.horizontalLayout_21.addWidget(self.bn_android_contact)


        self.horizontalLayout_20.addWidget(self.frame_android_contact)

        self.frame_android_game = QFrame(self.frame_android_menu)
        self.frame_android_game.setObjectName(u"frame_android_game")
        self.frame_android_game.setMinimumSize(QSize(80, 30))
        self.frame_android_game.setMaximumSize(QSize(80, 30))
        self.frame_android_game.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_android_game.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_android_game)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bn_android_game = QPushButton(self.frame_android_game)
        self.bn_android_game.setObjectName(u"bn_android_game")
        self.bn_android_game.setMinimumSize(QSize(80, 30))
        self.bn_android_game.setMaximumSize(QSize(80, 30))
        self.bn_android_game.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/1x/gameAsset 61.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bn_android_game.setIcon(icon8)
        self.bn_android_game.setIconSize(QSize(20, 13))
        self.bn_android_game.setFlat(True)

        self.horizontalLayout_22.addWidget(self.bn_android_game)


        self.horizontalLayout_20.addWidget(self.frame_android_game)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_android_menu)

        self.stackedWidget_android = QStackedWidget(self.page_android)
        self.stackedWidget_android.setObjectName(u"stackedWidget_android")
        self.stackedWidget_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_android_contact = QWidget()
        self.page_android_contact.setObjectName(u"page_android_contact")
        self.page_android_contact.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_android_contact)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.lab_android_contact = QLabel(self.page_android_contact)
        self.lab_android_contact.setObjectName(u"lab_android_contact")
        self.lab_android_contact.setMinimumSize(QSize(0, 55))
        self.lab_android_contact.setMaximumSize(QSize(16777215, 55))
        self.lab_android_contact.setFont(font2)
        self.lab_android_contact.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.lab_android_contact)

        self.frame_android_bottom = QFrame(self.page_android_contact)
        self.frame_android_bottom.setObjectName(u"frame_android_bottom")
        self.frame_android_bottom.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_android_bottom.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_android_bottom)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_android_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.line_android_name = QLineEdit(self.frame_android_field)
        self.line_android_name.setObjectName(u"line_android_name")#İSİMSOYİSİM
        self.line_android_name.setEnabled(True)
        self.line_android_name.setMinimumSize(QSize(300, 25))
        self.line_android_name.setMaximumSize(QSize(400, 25))
        self.line_android_name.setFont(font4)
        self.line_android_name.setStyleSheet(u"QLineEdit {\n"
                                      "	color:rgb(255,255,255);\n"
                                      "	border:2px solid rgb(51,51,51);\n"
                                      "	border-radius:4px;\n"
                                      "	background:rgb(51,51,51);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled {\n"
                                      "	color:rgb(255,255,255);\n"
                                      "	border:2px solid rgb(112,112,112);\n"
                                      "	border-radius:4px;\n"
                                      "	background:rgb(112,112,112);\n"
                                      "}")

        self.gridLayout_4.addWidget(self.line_android_name, 1, 2, 1, 1)

        self.line_android_adress = QLineEdit(self.frame_android_field)#ADRES
        self.line_android_adress.setObjectName(u"line_android_adress")
        self.line_android_adress.setEnabled(True)
        self.line_android_adress.setMinimumSize(QSize(300, 25))
        self.line_android_adress.setMaximumSize(QSize(400, 25))
        self.line_android_adress.setFont(font4)
        self.line_android_adress.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_adress, 4, 2, 1, 1)

        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 2)

        self.label = QLabel(self.frame_android_field)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 2)

        self.bn_android_contact_save = QPushButton(self.frame_android_field)#müşteri ekleme butonu
        self.bn_android_contact_save.setObjectName(u"bn_android_contact_save")
        self.bn_android_contact_save.setEnabled(True)
        self.bn_android_contact_save.setMaximumSize(QSize(250, 25))
        self.bn_android_contact_save.setFont(font4)
        self.bn_android_contact_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(90,90,90);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.bn_android_contact_save.clicked.connect(self.load_button_click_1)

        self.gridLayout_4.addWidget(self.bn_android_contact_save, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame_android_field)
        self.label_4.setObjectName(u"label_4")
        palette3 = QPalette()
        brush2 = QBrush(QColor(251, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_4.setPalette(palette3)

        self.gridLayout_4.addWidget(self.label_4, 5, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_android_field)#müşteri id
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(400, 25))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
                                               "	color:rgb(255,255,255);\n"
                                               "	border:2px solid rgb(51,51,51);\n"
                                               "	border-radius:4px;\n"
                                               "	background:rgb(51,51,51);\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:disabled {\n"
                                               "	color:rgb(255,255,255);\n"
                                               "	border:2px solid rgb(112,112,112);\n"
                                               "	border-radius:4px;\n"
                                               "	background:rgb(112,112,112);\n"
                                               "}")
        palette4 = QPalette()
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(51, 51, 51, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush5 = QBrush(QColor(76, 76, 76, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(63, 63, 63, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(25, 25, 25, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush7)
        brush8 = QBrush(QColor(34, 34, 34, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush9)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush10 = QBrush(QColor(255, 255, 220, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush9)
        brush11 = QBrush(QColor(255, 255, 255, 127))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush9)
        brush12 = QBrush(QColor(25, 25, 25, 127))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        brush13 = QBrush(QColor(36, 36, 36, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush13)
        self.lineEdit_2.setPalette(palette4)

        self.gridLayout_4.addWidget(self.lineEdit_2, 5, 2, 1, 1)

        self.pushButton = QPushButton(self.frame_android_field)
        self.pushButton.setObjectName(u"pushButton")#kargo yükleme butonu
        self.pushButton.setMaximumSize(QSize(250, 25))

        self.pushButton.setStyleSheet("""
            QPushButton {
                border: 2px solid rgb(51, 51, 51);
                border-radius: 5px;
                color: rgb(255, 255, 255);
                background-color: rgb(51, 51, 51);
            }
            QPushButton:hover {
                border: 2px solid rgb(0, 143, 150);
                background-color: rgb(0, 143, 150);
            }
            QPushButton:pressed {
                border: 2px solid rgb(0, 143, 150);
                background-color: rgb(90, 90, 90);
            }
            QPushButton:disabled {
                border-radius: 5px;
                border: 2px solid rgb(112, 112, 112);
                background-color: rgb(112, 112, 112);
            }
        """)

        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush14 = QBrush(QColor(112, 112, 112, 217))
        brush14.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButton.setPalette(palette5)

        self.pushButton.clicked.connect(self.load_button_click_2)
        self.gridLayout_4.addWidget(self.pushButton, 6, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_android_field, 0, 1, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_android.addWidget(self.page_android_contact)
        self.page_android_game = QWidget()
        self.page_android_game.setObjectName(u"page_android_game")
        self.page_android_game.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_game)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.lab_gamepad = QLabel(self.page_android_game)
        self.lab_gamepad.setObjectName(u"lab_gamepad")
        self.lab_gamepad.setMinimumSize(QSize(0, 55))
        self.lab_gamepad.setMaximumSize(QSize(16777215, 55))
        self.lab_gamepad.setFont(font2)
        self.lab_gamepad.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_11.addWidget(self.lab_gamepad)

        self.frame_textbar = QFrame(self.page_android_game)
        self.frame_textbar.setObjectName(u"frame_textbar")
        self.frame_textbar.setMaximumSize(QSize(16777215, 400))
        self.frame_textbar.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_textbar)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.label_3 = QLabel(self.frame_textbar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(75, 300))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_3.setPalette(palette6)

        self.horizontalLayout_26.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.frame_textbar)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(400, 25))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
                                      "	color:rgb(255,255,255);\n"
                                      "	border:2px solid rgb(51,51,51);\n"
                                      "	border-radius:4px;\n"
                                      "	background:rgb(51,51,51);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:disabled {\n"
                                      "	color:rgb(255,255,255);\n"
                                      "	border:2px solid rgb(112,112,112);\n"
                                      "	border-radius:4px;\n"
                                      "	background:rgb(112,112,112);\n"
                                      "}")

        self.horizontalLayout_26.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.frame_textbar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(100, 16777215))
        self.pushButton_2.setStyleSheet("""
                    QPushButton {
                        border: 2px solid rgb(51, 51, 51);
                        border-radius: 5px;
                        color: rgb(255, 255, 255);
                        background-color: rgb(51, 51, 51);
                    }
                    QPushButton:hover {
                        border: 2px solid rgb(0, 143, 150);
                        background-color: rgb(0, 143, 150);
                    }
                    QPushButton:pressed {
                        border: 2px solid rgb(0, 143, 150);
                        background-color: rgb(90, 90, 90);
                    }
                    QPushButton:disabled {
                        border-radius: 5px;
                        border: 2px solid rgb(112, 112, 112);
                        background-color: rgb(112, 112, 112);
                    }
                """)
        self.pushButton_2.clicked.connect(self.handle_button_click)

        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButton_2.setPalette(palette7)

        self.horizontalLayout_26.addWidget(self.pushButton_2)


        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.listWidget_4 = QListWidget(self.page_android_game)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setMaximumSize(QSize(1000, 250))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.listWidget_4.setPalette(palette8)

        self.verticalLayout_11.addWidget(self.listWidget_4)

        self.stackedWidget_android.addWidget(self.page_android_game)

        self.verticalLayout_9.addWidget(self.stackedWidget_android)

        self.stackedWidget.addWidget(self.page_android)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        self.frame_tab.setFont(font6)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Light"])
        font7.setPointSize(10)
        self.lab_tab.setFont(font7)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_android.setCurrentIndex(1)

        self.listWidget_2.itemClicked.connect(self.on_item_clicked)
        self.listCustomersUI()
        self.listAllShipmentsUI()



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def load_button_click_3(self):
        try:
                # Kullanıcı girişini sayıya dönüştürmeyi dene
                shipment_id = int(self.line_cloud_id.text())
        except ValueError:
                # Eğer boş veya geçersiz bir giriş varsa
                shipment_id = None

        if shipment_id is None:
                # shipment_id boşsa, tüm gönderileri listele
                self.listAllShipmentsUI()
        else:
                # shipment_id geçerliyse, işlem yap
                ShipmentSorter.sort_shipments_by_id()
                result = ShipmentSorter.binary_search_by_id(shipment_id)

                self.listWidget.clear()
                if result:
                        self.listWidget.addItem(f"Cargo ID: {result.shipment_id}")
                        self.listWidget.addItem(f"Shipment date: {result.shipment_date}")
                        self.listWidget.addItem(f"Target city: {result.target_city}")
                        self.listWidget.addItem(f"Delivery status: {result.delivery_status}")
                        self.listWidget.addItem(f"Estimated delivery duration: {result.delivery_duration} days")
                else:
                        self.listWidget.addItem("Kargo bulunamadı!")  # Sonuç yoksa kullanıcıya bilgi ver

    def load_button_click_2(self):
            try:
                    customer_id = int(self.lineEdit_2.text())  # Müşteri ID'sini integer olarak alıyoruz
                    current_date = datetime.now().date()  # Yıl, ay, gün bilgisini alıyoruz (sadece tarih)
                    customer_address = str(self.line_android_adress.text())  # Adresi alıyoruz

                    # customers_list içinde müşteri ID'sini arıyoruz
                    customer = next((c for c in customers_list if c.customerID == customer_id), None)

                    if customer:
                            customer.addShipment(current_date, "Not Delivered", customer_address)
                            print(f"Müşteri {customer_id} için gönderim başarıyla eklendi.")
                    else:
                            print(f"Müşteri ID'si {customer_id} bulunamadı.")
            except ValueError:
                    print("Hata: Lütfen geçerli bir müşteri ID'si giriniz.")

    def load_button_click_1(self):
            try:
                    print("Button clicked")  # Butona tıklandığında log yazdır
                    full_name = str(self.line_android_name.text())
                    name_parts = full_name.split(maxsplit=1)

                    customer_name = name_parts[0]
                    customer_surname = name_parts[1] if len(name_parts) > 1 else ""

                    Customer.addCustomer(customer_name, customer_surname)
            except Exception as e:
                    print(f"An error occurred: {e}")

    def handle_button_click(self):
            try:
                    customer_id = int(self.lineEdit.text())  # lineEdit'den alınan metni int'e çevir
                    self.print_shipments_by_customer_id(customer_id)  # Fonksiyona gönder
            except ValueError:
                    print("Error: Please enter a valid integer for Customer ID.")

    def print_shipments_by_customer_id(self, customer_id):
            """
            Belirli bir müşteri ID'sine ait gönderi geçmişini listWidget_4'e ekler.
            :param customer_id: Müşteri ID
            :param list_widget: PyQt listWidget nesnesi
            """
            # Müşteri ID'sine göre müşteriyi arama
            customer = next((c for c in customers_list if c.customerID == customer_id), None)

            # Müşteri bulunduysa gönderilerini listWidget'e ekle
            if customer:
                    self.listWidget_4.clear()  # Önce listeyi temizle
                    current = customer.shipment_history_list.head
                    while current:
                            shipment_str = str(current.shipment)
                            self.listWidget_4.addItem(shipment_str)  # Gönderi bilgisini listWidget'e ekle
                            current = current.next
            else:
                    self.listWidget_4.clear()
                    self.listWidget_4.addItem(f"No customer found with ID={customer_id}.")

    def on_item_clicked(self, item):
            # Tıklanan item'ın metnini al ve kontrol et
            item_text = item.text()
            print(f"Tıklanan item metni: {item_text}")

            # 'ID: ' kısmını ayıklayıp, sadece sayıyı almak için düzenleme yap
            try:
                    # 'ID: ' kısmını temizle ve sonra sayıyı al
                    customer_id = int(item_text.split("ID: ")[1].split(",")[0].strip())
                    print(f"Bulunan Müşteri ID'si: {customer_id}")
            except ValueError as e:
                    print(f"ID alınırken hata oluştu: {e}")
                    return  # Eğer hata oluşursa işlem yapma

            # Müşteri ID'sine göre müşteriyi bul
            selected_customer = self.get_customer_by_id(customer_id)

            if selected_customer:
                    # Müşterinin stack'inden son 5 gönderiyi al
                    last_shipments = selected_customer.shipment_history_stack.get_last_shipments()

                    # listWidget_3'ü güncelle
                    self.update_listWidget_3_from_shipments(last_shipments)
            else:
                    print("Müşteri bulunamadı!")

    def get_customer_by_id(self, customer_id):
            # Müşteri listesinde, verilen ID'ye sahip müşteriyi bul
            for customer in customers_list:
                    if customer.customerID == customer_id:
                            return customer
            return None

    def update_listWidget_3_from_shipments(self, shipments):
            # İlk olarak listWidget'ı temizle
            self.listWidget_3.clear()

            # Eğer gönderiler yoksa, "Kullanıcının kargosu bulunamadı" mesajını ekle
            if shipments is None or len(shipments) == 0:
                    self.listWidget_3.addItem("Kullanıcının kargosu bulunamadı")
            else:
                    # Eğer gönderiler varsa, her bir gönderiyi listeye ekle
                    for shipment in shipments:
                            self.listWidget_3.addItem(str(shipment))

    def listCustomersUI(self):
            self.listWidget_2.clear()
            if not customers_list:
                    print("nocustoemr")
            else:
                    for custoemr in customers_list:
                            self.listWidget_2.addItem(str(custoemr))

    def listAllShipmentsUI(self):
            for shipment in all_shipments:
                    if shipment.delivery_status == "Delivered":
                            shipment.delivery_duration = 0  # Teslim edilenlerin süresi 0 yapılır
            all_shipments.sort(key=lambda x: (x.delivery_duration == 0, x.delivery_duration))

            self.listWidget.clear()
            if not all_shipments:
                    print("No shipments found.")
            else:
                    for shipment in all_shipments:
                            # Konsola yazdırıyoruz
                            self.listWidget.addItem(str(shipment))



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">KarGO Management Systems</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip(QCoreApplication.translate("MainWindow", u"", None))
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_cloud.setToolTip(QCoreApplication.translate("MainWindow", u"", None))
#endif // QT_CONFIG(tooltip)
        self.bn_cloud.setProperty(u"M\u00fc\u015fteriler", "")
#if QT_CONFIG(tooltip)
        self.bn_android.setToolTip(QCoreApplication.translate("MainWindow", u"", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android.setText("")
        self.lab_home_main_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Aktif Kargolar</p><p><br/></p></body></html>", None))
        self.lab_home_stat_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Rotalar</p><p><br/></p></body></html>", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"Kargolarla \u0130lgili", None))
        self.text_about_home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'-webkit-standard'; font-size:18pt; color:#ffffff;\">Bu aray\u00fcz, kargo i\u015flemlerini y\u00f6netmek i\u00e7in kullan\u0131c\u0131 dostu bir tasar\u0131ma sahip olup, kargolar\u0131n rota ve adres bilgilerini net bir \u015fekilde g\u00f6sterirken, ayn\u0131 zamanda ilgili ki\u015filerin ileti\u015fim bilgilerini d\u00fczenli bir bi\u00e7imde sunar. Kullan\u0131c\u0131l"
                        "ar, her kargonun gidece\u011fi adresi ve g\u00fczergah\u0131 rahat\u00e7a g\u00f6rebilirken, her g\u00f6nderi i\u00e7in al\u0131c\u0131 ve g\u00f6nderici bilgilerini h\u0131zl\u0131ca eri\u015febilir. Kargo takip numaras\u0131, teslimat durumu gibi detaylar da kolayca g\u00f6r\u00fcnt\u00fclenebilir. Aray\u00fcz, t\u00fcm bu bilgileri g\u00f6rsel olarak ayr\u0131\u015ft\u0131rarak kullan\u0131c\u0131n\u0131n rahat\u00e7a i\u015flem yapmas\u0131n\u0131 sa\u011flar.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'-webkit-standard'; font-size:18pt; color:#ffffff;\"><br /></p></body></html>", None))
        self.lab_cloud_main.setText(QCoreApplication.translate("MainWindow", u"Kargo Sorgulama", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Kargo Takip Numaras\u0131:", None))
        self.bn_cloud_clear.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
#if QT_CONFIG(tooltip)
        self.bn_android_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Contact", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_contact.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_game.setToolTip(QCoreApplication.translate("MainWindow", u"GamePad", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_game.setText("")
        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u"M\u00fc\u015fteri Kaydetme ve Kargo Ekleme", None))
        self.line_android_name.setText("")
        self.line_android_adress.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Adres: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0130sim Soyisim: ", None))
        self.bn_android_contact_save.setText(QCoreApplication.translate("MainWindow", u"Y\u00fckle", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Kargo g\u00f6ndermek i\u00e7in m\u00fc\u015fteri no giriniz: ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Y\u00fckle", None))
        self.lab_gamepad.setText(QCoreApplication.translate("MainWindow", u"M\u00fc\u015fteri Ge\u00e7mi\u015fi Sorgulama", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M\u00fc\u015fteri ID : ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


