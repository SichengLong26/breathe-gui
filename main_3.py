# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv
import random
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import model
import pyqtgraph
from pyqtgraph import PlotWidget
from PyQt5.QtCore import *  # 导入线程相关模块
import re

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 789)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 30, 471, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 420, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 110, 631, 321))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        """
    ------呼吸音实时监测曲线图绘图------
        """
        self.widget = PlotWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 28, 607, 271))
        self.widget.setObjectName("widget")

        """
    ------------至此结束------------
        """

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 460, 361, 211))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(140, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(260, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.feature1 = QtWidgets.QLabel(self.groupBox_2)
        self.feature1.setGeometry(QtCore.QRect(20, 80, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.feature1.setFont(font)
        self.feature1.setText("")
        self.feature1.setAlignment(QtCore.Qt.AlignCenter)
        self.feature1.setObjectName("feature1")
        self.feature2 = QtWidgets.QLabel(self.groupBox_2)
        self.feature2.setGeometry(QtCore.QRect(140, 90, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.feature2.setFont(font)
        self.feature2.setAlignment(QtCore.Qt.AlignCenter)
        self.feature2.setObjectName("feature2")
        self.feature3 = QtWidgets.QLabel(self.groupBox_2)
        self.feature3.setGeometry(QtCore.QRect(260, 90, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.feature3.setFont(font)
        self.feature3.setAlignment(QtCore.Qt.AlignCenter)
        self.feature3.setObjectName("feature3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 50, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/用户.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 120, 341, 241))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(60, 30, 51, 31))
        self.label_8.setObjectName("label_8")
        self.name = QtWidgets.QLabel(self.groupBox_3)
        self.name.setGeometry(QtCore.QRect(110, 30, 111, 31))
        self.name.setText("")
        self.name.setObjectName("name")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(60, 70, 51, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(60, 110, 51, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(40, 190, 71, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 150, 91, 31))
        self.label_13.setObjectName("label_13")
        self.sex = QtWidgets.QLabel(self.groupBox_3)
        self.sex.setGeometry(QtCore.QRect(110, 70, 111, 31))
        self.sex.setText("")
        self.sex.setObjectName("sex")
        self.year = QtWidgets.QLabel(self.groupBox_3)
        self.year.setGeometry(QtCore.QRect(110, 110, 111, 31))
        self.year.setText("")
        self.year.setObjectName("year")
        self.weight = QtWidgets.QLabel(self.groupBox_3)
        self.weight.setGeometry(QtCore.QRect(110, 150, 111, 31))
        self.weight.setText("")
        self.weight.setObjectName("weight")
        self.illness = QtWidgets.QLabel(self.groupBox_3)
        self.illness.setGeometry(QtCore.QRect(120, 190, 111, 31))
        self.illness.setText("")
        self.illness.setObjectName("illness")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton.setGeometry(QtCore.QRect(280, 20, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(810, 470, 221, 201))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(50, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.result = QtWidgets.QLabel(self.groupBox_4)
        self.result.setGeometry(QtCore.QRect(30, 80, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 560, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 630, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 490, 161, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionasd = QtWidgets.QAction(MainWindow)
        self.actionasd.setObjectName("actionasd")
        self.actionlanyayanlie = QtWidgets.QAction(MainWindow)
        self.actionlanyayanlie.setObjectName("actionlanyayanlie")
        self.menu.addAction(self.actionasd)
        self.menu.addAction(self.actionlanyayanlie)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.showpatientinfo)
        self.pushButton_3.clicked.connect(self.showclasscification)
        self.pushButton_4.clicked.connect(self.savedata)
        self.pushButton_5.clicked.connect(self.datastop)
        self.toolButton.clicked.connect(self.DisplayPatient)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #  多线程
        self.f = Data1()  # 创建实时显示特征值线程对象
        self.f.data_signal.connect(self.feature_show)
        self.pushButton.clicked.connect(self.start)

    def start(self):  # 启动线程
        self.f.start()

    def feature_show(self, str):
        a = re.findall('-?\d+.\d+', str)
        self.x_array = [float(x) for x in a]
        print(self.x_array)
        self.curve = self.widget.plot(self.x_array, name="mode1")

        self.curve.setData(self.x_array)

        text = round(float(a[-1]), 2)
        text = "{}".format(text)
        self.feature1.setText(text)

    def datastop(self):
        self.f.quit()

    def showclasscification(self):
        list = ["正常音","湿罗音","干啰音"]
        i = random.randint(0,2)
        ill = list[i]
        self.result.setText(ill)

    def savedata(self):

        self.data = self.x_array

        if len(self.data) >= 10:
            for i in range(int(len(self.data)/10)):

                with open('beathe.csv', 'a') as wcsv:
                    w = csv.writer(wcsv)
                    w.writerow(self.data[i:i+9])


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "虚拟呼吸音数据模拟器"))
        self.pushButton.setText(_translate("MainWindow", "生成模拟呼吸音数据"))
        self.groupBox.setTitle(_translate("MainWindow", "呼吸音实时监测曲线图"))
        self.groupBox_2.setTitle(_translate("MainWindow", "实时监测数据"))
        self.label_2.setText(_translate("MainWindow", "特征值1"))
        self.label_3.setText(_translate("MainWindow", "特征值2"))
        self.label_4.setText(_translate("MainWindow", "特征值3"))
        self.feature2.setText(_translate("MainWindow", "待定"))
        self.feature3.setText(_translate("MainWindow", "待定"))
        self.pushButton_2.setText(_translate("MainWindow", "输入患者信息"))
        self.groupBox_3.setTitle(_translate("MainWindow", "患者基本信息"))
        self.label_8.setText(_translate("MainWindow", "姓名："))
        self.label_10.setText(_translate("MainWindow", "性别："))
        self.label_11.setText(_translate("MainWindow", "年龄："))
        self.label_12.setText(_translate("MainWindow", "患病史："))
        self.label_13.setText(_translate("MainWindow", "身高/体重："))
        self.toolButton.setText(_translate("MainWindow", "刷新"))
        self.groupBox_4.setTitle(_translate("MainWindow", "识别结果"))
        self.label_14.setText(_translate("MainWindow", "疾病类型"))
        self.pushButton_3.setText(_translate("MainWindow", "呼吸音类型识别"))
        self.pushButton_4.setText(_translate("MainWindow", "数据保存"))
        self.pushButton_5.setText(_translate("MainWindow", "停止生成数据"))
        self.menu.setTitle(_translate("MainWindow", "选择连接方式"))
        self.actionasd.setText(_translate("MainWindow", "接入云域网"))
        self.actionlanyayanlie.setText(_translate("MainWindow", "蓝牙连接"))

    def showpatientinfo(self):
        import patientinfo
        self.m = patientinfo.Ui_MainWindow()
        self.m.show()


    def DisplayPatient(self):
        result = model.Database().SearchInfo('select * from patientinfo')[-1]
        self.name.setText(result[1])
        self.sex.setText(result[2])
        self.year.setText(result[3])
        self.weight.setText(result[4])
        self.illness.setText(result[5])


class Data1(QThread):   # 线程1 实时特征值
    data_signal = pyqtSignal(str)
    def __init__(self):
        super(Data1, self).__init__()
        self.x_array = []
    def run(self):
        import numpy as np
        while True:
            random_data = np.random.normal()
            if len(self.x_array) < 1000000:
                self.x_array.append(random_data)
            elif len(self.x_array) >= 1000000:
                for i in range(len(self.x_array) - 1):
                    self.x_array[i] = self.x_array[i + 1]
                self.x_array[-1] = random_data
            self.data_signal.emit(str(self.x_array))
            QThread.msleep(200)

