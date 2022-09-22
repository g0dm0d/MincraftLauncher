# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/mods.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QLabel


from tools.mods.modManager import listMod, toogleMod, modStatus


class ModsManagerUI(object):
    def __init__(self, profile: str) -> None:
        self.profile = profile


    def on_click(self, mod):
        toogleMod(mod, self.profile)


    def setupUi(self, Form):
        Form.setObjectName("Mod manager")
        Form.resize(877, 731)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 260, 811, 441))
        self.listWidget.setObjectName("listWidget")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def add_card(self, name):
        itemN = QtWidgets.QListWidgetItem() 
        widget = QtWidgets.QWidget()
        widgetText =  QtWidgets.QLabel(name)
        widgetButton =  QtWidgets.QCheckBox()
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addWidget(widgetText)
        widgetLayout.addStretch()
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)  
        itemN.setSizeHint(widget.sizeHint())
        widgetButton.setChecked(modStatus(name, self.profile))
        widgetButton.stateChanged.connect(lambda: self.on_click(name))
        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, widget)
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(f'setup mod for {self.profile}')
        for mod in listMod(self.profile):
            self.add_card(mod[:-4])
