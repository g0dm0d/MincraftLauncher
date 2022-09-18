# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool
from tools.accounts.auth import addAccount


from tools.mods.installFabric import installFabric
from tools.versions.downloadMinecraft import downloadMinecraft
from tools.versions.getMinecraft import getVersion
from tools.versions.minecraftConf import versionList


class settingsUI(object):
    def __init__(self):
        self.threadpool = QThreadPool()
    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 690)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.Minecraft = QtWidgets.QWidget()
        self.Minecraft.setObjectName("Minecraft")
        self.version = QtWidgets.QComboBox(self.Minecraft)
        self.version.setGeometry(QtCore.QRect(160, 0, 111, 34))
        self.version.setObjectName("version")
        self.download = QtWidgets.QPushButton(self.Minecraft)
        self.download.setGeometry(QtCore.QRect(280, 0, 111, 36))
        self.download.setObjectName("download")
        self.name = QtWidgets.QLineEdit(self.Minecraft)
        self.name.setGeometry(QtCore.QRect(0, 0, 151, 32))
        self.name.setObjectName("name")
        self.tabWidget.addTab(self.Minecraft, "")
        self.Account = QtWidgets.QWidget()
        self.Account.setObjectName("Account")
        self.login = QtWidgets.QPushButton(self.Account)
        self.login.setGeometry(QtCore.QRect(0, 0, 90, 36))
        self.login.setObjectName("login")
        self.tabWidget.addTab(self.Account, "")
        self.Fabric = QtWidgets.QWidget()
        self.Fabric.setObjectName("Fabric")
        self.profile = QtWidgets.QComboBox(self.Fabric)
        self.profile.setGeometry(QtCore.QRect(0, 0, 111, 34))
        self.profile.setObjectName("profile")
        self.install = QtWidgets.QPushButton(self.Fabric)
        self.install.setGeometry(QtCore.QRect(130, 0, 90, 36))
        self.install.setObjectName("install")
        self.tabWidget.addTab(self.Fabric, "")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 660, 591, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.download.setText(_translate("Form", "Install Minecraft"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Minecraft), _translate("Form", "Minecraft"))
        self.login.setText(_translate("Form", "Login"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Account), _translate("Form", "Account"))
        self.install.setText(_translate("Form", "Install Fabric"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Fabric), _translate("Form", "Fabric"))

        self.install.clicked.connect(lambda: self.fabricInstall())
        self.download.clicked.connect(lambda: self.minecraftInstall())
        self.login.clicked.connect(lambda: self.loginin())


    def getVersion(self):
        for version in getVersion():
            self.version.addItem(version)


    def getProfile(self):
        for profile in versionList():
            self.profile.addItem(profile)


    def progress(self, procent):
        self.progressBar.setValue(procent)


    def loginin(self):
        self.threadpool.globalInstance().start(lambda: addAccount())


    def fabricInstall(self):
        self.threadpool.globalInstance().start(lambda: installFabric(self.profile.currentText(), callback = self.progress))


    def minecraftInstall(self):
        self.threadpool.globalInstance().start(lambda: downloadMinecraft(self.version.currentText(), self.name.text(), '/usr/bin/java', callback = self.progress))
