from PyQt5 import QtCore, QtGui, QtWidgets
from authAPI import loginmine
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(1029, 568)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/Downloads/White_Candle_Cake_(lit)_JE3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("#comboBox{\n"
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
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.Play = QtWidgets.QPushButton(Dialog)
        self.Play.setGeometry(QtCore.QRect(420, 470, 180, 60))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(False)
        self.Play.setFont(font)
        self.Play.setStyleSheet("background-color: rgb(0, 139, 68);\n"
"border-radius: 13px; \n"
"border-width: 3px;\n"
"border-style: solid;\n"
"\n"
"")
        self.Play.setObjectName("Play")
        self.Mods = QtWidgets.QToolButton(Dialog)
        self.Mods.setGeometry(QtCore.QRect(340, 120, 81, 36))
        self.Mods.setObjectName("Mods")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1051, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.widget.setFont(font)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color:  #1e1e1e;")
        self.widget.setObjectName("widget")
        self.Planet = QtWidgets.QLabel(self.widget)
        self.Planet.setGeometry(QtCore.QRect(10, 10, 19, 19))
        self.Planet.setText("")
        self.Planet.setPixmap(QtGui.QPixmap("res/Earth.png"))
        self.Planet.setScaledContents(True)
        self.Planet.setObjectName("Planet")
        self.Language = QtWidgets.QComboBox(self.widget)
        self.Language.setGeometry(QtCore.QRect(29, 5, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Thaana")
        font.setBold(True)
        self.Language.setFont(font)
        self.Language.setStyleSheet("#Language{\n"
"    border: 0px     solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding-left:  10px;\n"
"}\n"
"\n"
"#Language::drop-down{\n"
"    border:0px;\n"
"}\n"
"\n"
"#Language::down-arrow{\n"
"    image: url(:/newPrefix/arrow-down-sign-to-navigate.png);\n"
"    width: 12px;\n"
"     height: 12px;\n"
"    margin-right:  15px;\n"
"}\n"
"\n"
"#Language:on {\n"
"    border: 0px solid #c2dbfe;\n"
"}")
        self.Language.setObjectName("Language")
        self.Language.addItem("")
        self.Language.addItem("")
        self.Language.addItem("")
        self.Login = QtWidgets.QComboBox(self.widget)
        self.Login.setGeometry(QtCore.QRect(900, 5, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Thaana")
        font.setBold(True)
        self.Login.setFont(font)
        self.Login.setStyleSheet("#Login{\n"
"    border: 0px     solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding-left:  10px;\n"
"}\n"
"\n"
"#Login::drop-down{\n"
"    border:0px;\n"
"}\n"
"\n"
"#Login::down-arrow{\n"
"    image: url(:/newPrefix/arrow-down-sign-to-navigate.png);\n"
"    width: 12px;\n"
"     height: 12px;\n"
"    margin-right:  15px;\n"
"}\n"
"\n"
"#Login:on {\n"
"    border: 0px solid #c2dbfe;\n"
"}")
        self.Login.setObjectName("Login")
        self.Login.addItem("")
        self.Settings = QtWidgets.QToolButton(Dialog)
        self.Settings.setGeometry(QtCore.QRect(470, 120, 81, 36))
        self.Settings.setObjectName("Settings")
        self.Skin = QtWidgets.QToolButton(Dialog)
        self.Skin.setGeometry(QtCore.QRect(600, 120, 81, 36))
        self.Skin.setObjectName("Skin")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(-20, 490, 1051, 80))
        self.widget_2.setStyleSheet("background-color:  #1e1e1e;")
        self.widget_2.setObjectName("widget_2")
        self.Launchver = QtWidgets.QLabel(self.widget_2)
        self.Launchver.setGeometry(QtCore.QRect(30, 50, 161, 20))
        self.Launchver.setObjectName("Launchver")
        self.logo = QtWidgets.QLabel(self.widget_2)
        self.logo.setGeometry(QtCore.QRect(920, 46, 61, 21))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("res/Null.png"))
        self.logo.setScaledContents(False)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.null_2 = QtWidgets.QLabel(self.widget_2)
        self.null_2.setGeometry(QtCore.QRect(990, 50, 59, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        self.null_2.setFont(font)
        self.null_2.setObjectName("null_2")
        self.Version = QtWidgets.QComboBox(Dialog)
        self.Version.setGeometry(QtCore.QRect(820, 170, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Version.sizePolicy().hasHeightForWidth())
        self.Version.setSizePolicy(sizePolicy)
        self.Version.setStyleSheet("#Version{\n"
"    border: 0px     solid #ced4da;\n"
"    border-radius: 4px;\n"
"    padding-left:  10px;\n"
"}\n"
"\n"
"#Version::drop-down{\n"
"    border:0px;\n"
"}\n"
"\n"
"#Version::down-arrow{\n"
"    image: url(:/newPrefix/arrow-down-sign-to-navigate.png);\n"
"    width: 12px;\n"
"     height: 12px;\n"
"    margin-right:  15px;\n"
"}\n"
"\n"
"#Version:on {\n"
"    border: 0px solid #c2dbfe;\n"
"}")
        self.Version.setObjectName("Version")
        self.widget_2.raise_()
        self.widget.raise_()
        self.Mods.raise_()
        self.Settings.raise_()
        self.Skin.raise_()
        self.Play.raise_()
        self.Version.raise_()

        self.Play.clicked.connect(self.loginin)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Minecraft Launcher"))
        self.Play.setText(_translate("Dialog", "PLAY"))
        self.Mods.setText(_translate("Dialog", "Mods"))
        self.Language.setItemText(0, _translate("Dialog", "English - US"))
        self.Language.setItemText(1, _translate("Dialog", "11"))
        self.Language.setItemText(2, _translate("Dialog", "1"))
        self.Login.setItemText(0, _translate("Dialog", "Login"))
        self.Settings.setText(_translate("Dialog", "Settings"))
        self.Skin.setText(_translate("Dialog", "Skins"))
        self.Launchver.setText(_translate("Dialog", "\"Launcher version"))
        self.null_2.setText(_translate("Dialog", "Null"))

    def loginin(self):
        self.threadpool = QThreadPool()
        self.threadpool.start(loginmine)


import launcher_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
