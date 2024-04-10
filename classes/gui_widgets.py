# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1402, 1014)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font-size: 12pt; font: Arial;")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 850, 1041, 131))
        self.plainTextEdit.setMouseTracking(True)
        self.plainTextEdit.setStyleSheet("font-size: 15pt; font: Arial;")
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.VideoFeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoFeedLabel.setGeometry(QtCore.QRect(10, 5, 1041, 801))
        self.VideoFeedLabel.setMouseTracking(True)
        self.VideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.VideoFeedLabel.setText("")
        self.VideoFeedLabel.setObjectName("VideoFeedLabel")
        self.frameslider = QtWidgets.QProgressBar(self.centralwidget)
        self.frameslider.setGeometry(QtCore.QRect(10, 812, 1041, 31))
        self.frameslider.setStyleSheet("    QProgressBar {\n"
"        border: 2px solid rgba(33, 37, 43, 180);\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        background-color: rgba(33, 37, 43, 180);\n"
"        color: black;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #FFD700;\n"
"    }")
        self.frameslider.setMinimum(0)
        self.frameslider.setMaximum(100)
        self.frameslider.setProperty("value", 0)
        self.frameslider.setObjectName("frameslider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(329, 987))
        self.dockWidget.setStyleSheet("")
        self.dockWidget.setFloating(False)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.frame_3 = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 311, 231))
        self.frame_3.setStyleSheet(" color: rgb(0, 0, 0);\n"
" background-color: rgb(255, 255, 255);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.choosevideobutton = QtWidgets.QPushButton(self.frame_3)
        self.choosevideobutton.setGeometry(QtCore.QRect(30, 50, 101, 31))
        self.choosevideobutton.setStyleSheet("     QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"            \n"
"            \n"
"            }")
        self.choosevideobutton.setObjectName("choosevideobutton")
        self.pausebutton = QtWidgets.QPushButton(self.frame_3)
        self.pausebutton.setGeometry(QtCore.QRect(170, 50, 121, 30))
        self.pausebutton.setMaximumSize(QtCore.QSize(300, 30))
        self.pausebutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(150, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(150, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 150);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 255);\n"
"                font: bold 12px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(255, 0, 0);\n"
"                padding-left: 2px;\n"
"                padding-top: 2px;\n"
"            }")
        self.pausebutton.setCheckable(True)
        self.pausebutton.setObjectName("pausebutton")
        self.savedatabutton = QtWidgets.QPushButton(self.frame_3)
        self.savedatabutton.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.savedatabutton.setStyleSheet("QPushButton {\n"
"                color: rgb(0, 0, 0);\n"
"                background-color: rgb(255, 255, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 255, 100);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(255, 255, 200);\n"
"                color: rgb(0, 0, 0);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: red;\n"
"                border: 2px solid red;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"                border-style: inset;\n"
"                }")
        self.savedatabutton.setCheckable(True)
        self.savedatabutton.setObjectName("savedatabutton")
        self.recordbutton = QtWidgets.QPushButton(self.frame_3)
        self.recordbutton.setGeometry(QtCore.QRect(170, 120, 131, 31))
        self.recordbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.recordbutton.setCheckable(True)
        self.recordbutton.setObjectName("recordbutton")
        self.framelabel = QtWidgets.QLabel(self.frame_3)
        self.framelabel.setGeometry(QtCore.QRect(30, 90, 121, 21))
        self.framelabel.setMaximumSize(QtCore.QSize(300, 25))
        self.framelabel.setObjectName("framelabel")
        self.leftbutton = QtWidgets.QToolButton(self.frame_3)
        self.leftbutton.setGeometry(QtCore.QRect(170, 90, 51, 21))
        self.leftbutton.setStyleSheet("QToolButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: px;\n"
"                border-radius: 10px;\n"
"                border: 2px solid rgb(0, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border: 2px solid rgb(0, 255, 0);\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: rgb(100, 100, 100);\n"
"                border: 2px solid rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.leftbutton.setAutoRepeat(False)
        self.leftbutton.setAutoRepeatDelay(0)
        self.leftbutton.setAutoRepeatInterval(1)
        self.leftbutton.setArrowType(QtCore.Qt.LeftArrow)
        self.leftbutton.setObjectName("leftbutton")
        self.trackbutton = QtWidgets.QPushButton(self.frame_3)
        self.trackbutton.setGeometry(QtCore.QRect(10, 5, 281, 41))
        self.trackbutton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.trackbutton.setStyleSheet("\n"
"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 255);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"              font: bold 25px;\n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 0);\n"
"                font: bold 25px;\n"
"                min-width: 1em;\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(0, 255, 0);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.trackbutton.setCheckable(True)
        self.trackbutton.setObjectName("trackbutton")
        self.rightbutton = QtWidgets.QToolButton(self.frame_3)
        self.rightbutton.setGeometry(QtCore.QRect(240, 90, 50, 21))
        self.rightbutton.setStyleSheet("QToolButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: px;\n"
"                border-radius: 10px;\n"
"                border: 2px solid rgb(0, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border: 2px solid rgb(0, 255, 0);\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: rgb(100, 100, 100);\n"
"                border: 2px solid rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.rightbutton.setAutoRepeat(False)
        self.rightbutton.setAutoRepeatInterval(1)
        self.rightbutton.setArrowType(QtCore.Qt.RightArrow)
        self.rightbutton.setObjectName("rightbutton")
        self.exposurelabel = QtWidgets.QLabel(self.frame_3)
        self.exposurelabel.setGeometry(QtCore.QRect(20, 170, 111, 25))
        self.exposurelabel.setMaximumSize(QtCore.QSize(150, 25))
        self.exposurelabel.setObjectName("exposurelabel")
        self.exposurebox = QtWidgets.QSpinBox(self.frame_3)
        self.exposurebox.setGeometry(QtCore.QRect(20, 190, 111, 35))
        self.exposurebox.setMinimum(100)
        self.exposurebox.setMaximum(30000)
        self.exposurebox.setSingleStep(100)
        self.exposurebox.setProperty("value", 5000)
        self.exposurebox.setDisplayIntegerBase(10)
        self.exposurebox.setObjectName("exposurebox")
        self.objectivelabel = QtWidgets.QLabel(self.frame_3)
        self.objectivelabel.setGeometry(QtCore.QRect(180, 170, 111, 25))
        self.objectivelabel.setMaximumSize(QtCore.QSize(150, 25))
        self.objectivelabel.setObjectName("objectivelabel")
        self.objectivebox = QtWidgets.QSpinBox(self.frame_3)
        self.objectivebox.setGeometry(QtCore.QRect(180, 190, 111, 35))
        self.objectivebox.setMinimum(1)
        self.objectivebox.setMaximum(50)
        self.objectivebox.setSingleStep(5)
        self.objectivebox.setProperty("value", 10)
        self.objectivebox.setDisplayIntegerBase(10)
        self.objectivebox.setObjectName("objectivebox")
        self.trackerparamsframe = QtWidgets.QFrame(self.dockWidgetContents)
        self.trackerparamsframe.setGeometry(QtCore.QRect(10, 250, 311, 281))
        self.trackerparamsframe.setStyleSheet(" color: rgb(0, 0, 0);\n"
" background-color: rgb(255, 255, 255);\n"
"")
        self.trackerparamsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trackerparamsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trackerparamsframe.setObjectName("trackerparamsframe")
        self.robotmasklowerbox = QtWidgets.QSpinBox(self.trackerparamsframe)
        self.robotmasklowerbox.setGeometry(QtCore.QRect(110, 160, 141, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.robotmasklowerbox.setFont(font)
        self.robotmasklowerbox.setStyleSheet("")
        self.robotmasklowerbox.setMaximum(255)
        self.robotmasklowerbox.setSingleStep(1)
        self.robotmasklowerbox.setProperty("value", 0)
        self.robotmasklowerbox.setObjectName("robotmasklowerbox")
        self.maskthreshlabel = QtWidgets.QLabel(self.trackerparamsframe)
        self.maskthreshlabel.setGeometry(QtCore.QRect(10, 170, 81, 25))
        self.maskthreshlabel.setMaximumSize(QtCore.QSize(150, 25))
        self.maskthreshlabel.setObjectName("maskthreshlabel")
        self.robotmaskdilationbox = QtWidgets.QSpinBox(self.trackerparamsframe)
        self.robotmaskdilationbox.setGeometry(QtCore.QRect(110, 240, 141, 35))
        self.robotmaskdilationbox.setMaximum(40)
        self.robotmaskdilationbox.setObjectName("robotmaskdilationbox")
        self.maskdilationlabel = QtWidgets.QLabel(self.trackerparamsframe)
        self.maskdilationlabel.setGeometry(QtCore.QRect(10, 250, 81, 25))
        self.maskdilationlabel.setMaximumSize(QtCore.QSize(150, 25))
        self.maskdilationlabel.setObjectName("maskdilationlabel")
        self.robotcroplengthbox = QtWidgets.QSpinBox(self.trackerparamsframe)
        self.robotcroplengthbox.setGeometry(QtCore.QRect(110, 80, 141, 35))
        self.robotcroplengthbox.setMinimum(5)
        self.robotcroplengthbox.setMaximum(400)
        self.robotcroplengthbox.setSingleStep(1)
        self.robotcroplengthbox.setProperty("value", 40)
        self.robotcroplengthbox.setDisplayIntegerBase(10)
        self.robotcroplengthbox.setObjectName("robotcroplengthbox")
        self.croplengthlabel = QtWidgets.QLabel(self.trackerparamsframe)
        self.croplengthlabel.setGeometry(QtCore.QRect(10, 90, 81, 25))
        self.croplengthlabel.setMaximumSize(QtCore.QSize(150, 25))
        self.croplengthlabel.setObjectName("croplengthlabel")
        self.robotmaskblurbox = QtWidgets.QSpinBox(self.trackerparamsframe)
        self.robotmaskblurbox.setGeometry(QtCore.QRect(110, 120, 141, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.robotmaskblurbox.setFont(font)
        self.robotmaskblurbox.setStyleSheet("")
        self.robotmaskblurbox.setMaximum(40)
        self.robotmaskblurbox.setSingleStep(1)
        self.robotmaskblurbox.setProperty("value", 0)
        self.robotmaskblurbox.setObjectName("robotmaskblurbox")
        self.maskblurlabel = QtWidgets.QLabel(self.trackerparamsframe)
        self.maskblurlabel.setGeometry(QtCore.QRect(10, 130, 61, 25))
        self.maskblurlabel.setMaximumSize(QtCore.QSize(150, 25))
        self.maskblurlabel.setObjectName("maskblurlabel")
        self.maskbutton = QtWidgets.QPushButton(self.trackerparamsframe)
        self.maskbutton.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.maskbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-style: inset;\n"
"              border-color: rgb(0, 255, 0);\n"
"            }")
        self.maskbutton.setCheckable(True)
        self.maskbutton.setChecked(False)
        self.maskbutton.setObjectName("maskbutton")
        self.maskinvert_checkBox = QtWidgets.QCheckBox(self.trackerparamsframe)
        self.maskinvert_checkBox.setGeometry(QtCore.QRect(140, 10, 131, 30))
        self.maskinvert_checkBox.setChecked(False)
        self.maskinvert_checkBox.setObjectName("maskinvert_checkBox")
        self.robotmaskupperbox = QtWidgets.QSpinBox(self.trackerparamsframe)
        self.robotmaskupperbox.setGeometry(QtCore.QRect(110, 200, 141, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.robotmaskupperbox.setFont(font)
        self.robotmaskupperbox.setStyleSheet("")
        self.robotmaskupperbox.setMinimum(0)
        self.robotmaskupperbox.setMaximum(255)
        self.robotmaskupperbox.setSingleStep(1)
        self.robotmaskupperbox.setProperty("value", 128)
        self.robotmaskupperbox.setObjectName("robotmaskupperbox")
        self.maskthreshlabel_2 = QtWidgets.QLabel(self.trackerparamsframe)
        self.maskthreshlabel_2.setGeometry(QtCore.QRect(10, 210, 81, 25))
        self.maskthreshlabel_2.setMaximumSize(QtCore.QSize(150, 25))
        self.maskthreshlabel_2.setObjectName("maskthreshlabel_2")
        self.robotparamsframe = QtWidgets.QFrame(self.dockWidgetContents)
        self.robotparamsframe.setGeometry(QtCore.QRect(10, 549, 311, 61))
        self.robotparamsframe.setStyleSheet(" color: rgb(255, 255, 255);\n"
" background-color: rgb(0, 0, 0);\n"
"font-size: 14pt; font: Arial;")
        self.robotparamsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.robotparamsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.robotparamsframe.setObjectName("robotparamsframe")
        self.robotsizelabel = QtWidgets.QLabel(self.robotparamsframe)
        self.robotsizelabel.setGeometry(QtCore.QRect(30, 0, 51, 20))
        self.robotsizelabel.setMaximumSize(QtCore.QSize(300, 50))
        self.robotsizelabel.setObjectName("robotsizelabel")
        self.robotvelocitylabel = QtWidgets.QLabel(self.robotparamsframe)
        self.robotvelocitylabel.setGeometry(QtCore.QRect(110, 0, 81, 21))
        self.robotvelocitylabel.setMaximumSize(QtCore.QSize(300, 50))
        self.robotvelocitylabel.setObjectName("robotvelocitylabel")
        self.robotblurlabel = QtWidgets.QLabel(self.robotparamsframe)
        self.robotblurlabel.setGeometry(QtCore.QRect(220, 0, 51, 20))
        self.robotblurlabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.robotblurlabel.setStyleSheet("")
        self.robotblurlabel.setObjectName("robotblurlabel")
        self.blurlcdnum = QtWidgets.QLCDNumber(self.robotparamsframe)
        self.blurlcdnum.setGeometry(QtCore.QRect(200, 20, 61, 30))
        self.blurlcdnum.setStyleSheet("background-color: rgb(0,0,0); \n"
"color: rgb(0,255,0);")
        self.blurlcdnum.setLineWidth(0)
        self.blurlcdnum.setMidLineWidth(0)
        self.blurlcdnum.setSmallDecimalPoint(False)
        self.blurlcdnum.setDigitCount(3)
        self.blurlcdnum.setMode(QtWidgets.QLCDNumber.Dec)
        self.blurlcdnum.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
        self.blurlcdnum.setProperty("value", 137.0)
        self.blurlcdnum.setObjectName("blurlcdnum")
        self.robotvelocityunitslabel = QtWidgets.QLabel(self.robotparamsframe)
        self.robotvelocityunitslabel.setGeometry(QtCore.QRect(160, 30, 41, 20))
        self.robotvelocityunitslabel.setMaximumSize(QtCore.QSize(300, 50))
        self.robotvelocityunitslabel.setObjectName("robotvelocityunitslabel")
        self.robotblurunitslabe = QtWidgets.QLabel(self.robotparamsframe)
        self.robotblurunitslabe.setGeometry(QtCore.QRect(260, 30, 41, 20))
        self.robotblurunitslabe.setMaximumSize(QtCore.QSize(300, 50))
        self.robotblurunitslabe.setObjectName("robotblurunitslabe")
        self.sizelcdnum = QtWidgets.QLCDNumber(self.robotparamsframe)
        self.sizelcdnum.setGeometry(QtCore.QRect(0, 20, 61, 30))
        self.sizelcdnum.setStyleSheet("background-color: rgb(0,0,0); \n"
"color: rgb(0,255,0);")
        self.sizelcdnum.setLineWidth(0)
        self.sizelcdnum.setMidLineWidth(0)
        self.sizelcdnum.setSmallDecimalPoint(False)
        self.sizelcdnum.setDigitCount(3)
        self.sizelcdnum.setMode(QtWidgets.QLCDNumber.Dec)
        self.sizelcdnum.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
        self.sizelcdnum.setProperty("value", 20.0)
        self.sizelcdnum.setObjectName("sizelcdnum")
        self.vellcdnum = QtWidgets.QLCDNumber(self.robotparamsframe)
        self.vellcdnum.setGeometry(QtCore.QRect(90, 20, 71, 30))
        self.vellcdnum.setStyleSheet("background-color: rgb(0,0,0); \n"
"color: rgb(0,255,0);")
        self.vellcdnum.setLineWidth(0)
        self.vellcdnum.setMidLineWidth(0)
        self.vellcdnum.setSmallDecimalPoint(False)
        self.vellcdnum.setDigitCount(3)
        self.vellcdnum.setMode(QtWidgets.QLCDNumber.Dec)
        self.vellcdnum.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
        self.vellcdnum.setProperty("value", 17.1)
        self.vellcdnum.setObjectName("vellcdnum")
        self.robotsizeunitslabel = QtWidgets.QLabel(self.robotparamsframe)
        self.robotsizeunitslabel.setGeometry(QtCore.QRect(60, 30, 31, 20))
        self.robotsizeunitslabel.setMaximumSize(QtCore.QSize(300, 50))
        self.robotsizeunitslabel.setObjectName("robotsizeunitslabel")
        self.CroppedVideoFeedLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.CroppedVideoFeedLabel.setGeometry(QtCore.QRect(10, 615, 310, 310))
        self.CroppedVideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.CroppedVideoFeedLabel.setText("")
        self.CroppedVideoFeedLabel.setObjectName("CroppedVideoFeedLabel")
        self.resetdefaultbutton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.resetdefaultbutton.setGeometry(QtCore.QRect(20, 935, 71, 25))
        self.resetdefaultbutton.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.resetdefaultbutton.setFont(font)
        self.resetdefaultbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(100, 100, 100);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(100, 100, 100);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(200, 200, 200);\n"
"                color: rgb(0, 0, 0);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(200, 200, 200);\n"
"         \n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"                border-style: inset;\n"
"                }")
        self.resetdefaultbutton.setObjectName("resetdefaultbutton")
        self.croppedmasktoggle = QtWidgets.QPushButton(self.dockWidgetContents)
        self.croppedmasktoggle.setGeometry(QtCore.QRect(125, 935, 71, 25))
        self.croppedmasktoggle.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.croppedmasktoggle.setFont(font)
        self.croppedmasktoggle.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-style: inset;\n"
"              border-color: rgb(0, 255, 0);\n"
"            }")
        self.croppedmasktoggle.setCheckable(True)
        self.croppedmasktoggle.setObjectName("croppedmasktoggle")
        self.croppedrecordbutton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.croppedrecordbutton.setGeometry(QtCore.QRect(230, 935, 71, 25))
        self.croppedrecordbutton.setMinimumSize(QtCore.QSize(21, 0))
        self.croppedrecordbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"      \n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.croppedrecordbutton.setCheckable(True)
        self.croppedrecordbutton.setObjectName("croppedrecordbutton")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actiondock = QtWidgets.QAction(MainWindow)
        self.actiondock.setMenuRole(QtWidgets.QAction.NoRole)
        self.actiondock.setObjectName("actiondock")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frameslider.setFormat(_translate("MainWindow", "Frame %v"))
        self.choosevideobutton.setText(_translate("MainWindow", "Choose Video"))
        self.pausebutton.setText(_translate("MainWindow", "Pause"))
        self.savedatabutton.setText(_translate("MainWindow", "Save Data"))
        self.recordbutton.setText(_translate("MainWindow", "Record"))
        self.framelabel.setText(_translate("MainWindow", "Frame: "))
        self.leftbutton.setText(_translate("MainWindow", "..."))
        self.trackbutton.setText(_translate("MainWindow", "Track"))
        self.rightbutton.setText(_translate("MainWindow", "..."))
        self.exposurelabel.setText(_translate("MainWindow", "Exposure"))
        self.objectivelabel.setText(_translate("MainWindow", "Objective"))
        self.maskthreshlabel.setText(_translate("MainWindow", "Lower Thresh"))
        self.maskdilationlabel.setText(_translate("MainWindow", "Dilation"))
        self.croplengthlabel.setText(_translate("MainWindow", "Crop Length"))
        self.maskblurlabel.setText(_translate("MainWindow", "Blur"))
        self.maskbutton.setText(_translate("MainWindow", "Mask"))
        self.maskinvert_checkBox.setText(_translate("MainWindow", "Invert Mask: True"))
        self.maskthreshlabel_2.setText(_translate("MainWindow", "Upper Thresh"))
        self.robotsizelabel.setText(_translate("MainWindow", "Size:   "))
        self.robotvelocitylabel.setText(_translate("MainWindow", "Velocity: "))
        self.robotblurlabel.setText(_translate("MainWindow", "Blur:"))
        self.robotvelocityunitslabel.setText(_translate("MainWindow", "um/s"))
        self.robotblurunitslabe.setText(_translate("MainWindow", "units"))
        self.robotsizeunitslabel.setText(_translate("MainWindow", "um  "))
        self.resetdefaultbutton.setText(_translate("MainWindow", "Defaults"))
        self.croppedmasktoggle.setText(_translate("MainWindow", "Original"))
        self.croppedrecordbutton.setText(_translate("MainWindow", "Record"))
        self.actiondock.setText(_translate("MainWindow", "dock"))
