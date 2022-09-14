# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/mods.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel
import requests


from tools.mods.modManager import searchMod
from tools.versions.minecraftConf import versionList
from tools.mods.modManager import downloadMod
from modsManager import ModsManagerUI


class ModsSearchUI(object):
    def __init__(self):
        self.threadpool = QThreadPool()
    def setupUi(self, Form):
        Form.setObjectName("Mod installer")
        Form.resize(877, 731)
        Form.setStyleSheet("")
        self.Searcbar = QtWidgets.QLineEdit(Form)
        self.Searcbar.setGeometry(QtCore.QRect(210, 160, 171, 34))
        self.Searcbar.setAutoFillBackground(False)
        self.Searcbar.setStyleSheet("QLineEdit\n"
            "{\n"
            "    border: 2px solid  rgb(62, 67, 75);\n"
            "    border-radius: 5%;\n"
            "    color: white;\n"
            "    padding-left:25px;\n"
            "    padding-right:25px;\n"
            "    backgroud-color:rgb(255, 255, 255);\n"
            "}\n"
            "")
        self.Searcbar.setObjectName("lineEdit")
        self.Searcbar.returnPressed.connect(self.searchMod)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(560, 160, 87, 34))
        self.comboBox.setStyleSheet("#comboBox{\n"
            "    border: 0px     solid #ced4da;\n"
            "    border-radius: 4px;\n"
            "    padding-left:  10px;\n"
            "}\n"
            "\n"
            "#comboBox::drop-down{\n"
            "    border:0px;\n"
            "}\n"
            "\n"
            "#comboBox::down-arrow{\n"
            "    image: url(:/newPrefix/arrow-down-sign-to-navigate.png);\n"
            "    width: 12px;\n"
            "     height: 12px;\n"
            "    margin-right:  15px;\n"
            "}\n"
            "\n"
            "#comboBox:on {\n"
            "    border: 0px solid #c2dbfe;\n"
            "}")
        self.comboBox.setObjectName("comboBox")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 260, 811, 441))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 163, 51, 34))
        self.pushButton.setStyleSheet("QPushButton\n"
            "{\n"
            "    border: -0;\n"
            "\n"
            "    color: white;\n"
            "    padding-left:20px;\n"
            "    padding-right:20px;\n"
            "    backgroud-color:rgb(255, 255, 255);\n"
            "}\n"
            "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 391, 20))
        self.label.setObjectName("label")

        self.modsManager = QtWidgets.QToolButton(Form)
        self.modsManager.setGeometry(QtCore.QRect(460, 160, 87, 34))
        self.modsManager.setStyleSheet("#comboBox{\n"
            "    border: 0px     solid #ced4da;\n"
            "    border-radius: 4px;\n"
            "    padding-left:  10px;\n"
            "}\n"
            "\n"
            "#comboBox::drop-down{\n"
            "    border:0px;\n"
            "}\n"
            "\n"
            "#comboBox::down-arrow{\n"
            "    image: url(:/newPrefix/arrow-down-sign-to-navigate.png);\n"
            "    width: 12px;\n"
            "     height: 12px;\n"
            "    margin-right:  15px;\n"
            "}\n"
            "\n"
            "#comboBox:on {\n"
            "    border: 0px solid #c2dbfe;\n"
            "}")
        self.modsManager.setObjectName("modsManager")
        self.modsManager.clicked.connect(lambda: self.modsmanagerUI())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.modsManager.setText(_translate("Dialog", "Mods manager"))
        self.Searcbar.setPlaceholderText(_translate("Form", "Search.."))
        self.comboBox.setPlaceholderText(_translate("Form", "Version"))
        self.pushButton.setText(_translate("Form", "🔍"))
        self.label.setText(_translate("Form", "Mod manager design will be better in the future"))

    def on_click(self, mod):
        self.threadpool = QThreadPool()
        self.threadpool.globalInstance().start(lambda: downloadMod(mod, self.comboBox.currentText()))

    def add_card(self, name, modid, url):
        itemN = QtWidgets.QListWidgetItem() 
        widget = QtWidgets.QWidget()
        image = QImage()
        if len(url) != 0:
            image.loadFromData(requests.get(url).content)
        image = image
        image_label = QLabel()
        image_label.setPixmap(QPixmap(image).scaled(48, 48))

        widgetText =  QtWidgets.QLabel(name)
        widgetButton =  QtWidgets.QPushButton("Download")
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(image_label)
        widgetLayout.addWidget(widgetText)
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()
        
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)  
        itemN.setSizeHint(widget.sizeHint())    
        
        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, widget)
        
        widgetButton.clicked.connect(lambda: self.on_click(modid))

    def searchMod(self):
        self.listWidget.clear()
        version = self.comboBox.currentText()
        textboxValue = self.Searcbar.text()
        modsList = searchMod(textboxValue, version)
        for i in modsList:
            self.add_card(i[0],i[1],i[2])

    def scanVer(self):
        for version in versionList():
            self.comboBox.addItem(version)
            self.comboBox.setCurrentText(version)

    def modsmanagerUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ModsManagerUI()
        self.ui.profile = self.comboBox.currentText()
        self.ui.setupUi(self.window)
        self.window.show()
