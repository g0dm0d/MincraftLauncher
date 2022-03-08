from os import access
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from authAPI import loginmine
from UUID import uuidfinder

con = sqlite3.connect('enelix.db')
cursor = con.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 572)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/main/svg.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(1070, 490, 95, 31))
        self.play.setObjectName("play")
        self.version = QtWidgets.QComboBox(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(850, 490, 171, 31))
        self.version.setObjectName("version")
        self.selectacc = QtWidgets.QComboBox(self.centralwidget)
        self.selectacc.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.selectacc.setObjectName("selectacc")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(210, 20, 95, 31))
        self.login.setObjectName("login")
        self.Nickname = QtWidgets.QLineEdit(self.centralwidget)
        self.Nickname.setGeometry(QtCore.QRect(340, 20, 113, 31))
        self.Nickname.setStyleSheet("")
        self.Nickname.setObjectName("Nickname")
        self.reg = QtWidgets.QPushButton(self.centralwidget)
        self.reg.setGeometry(QtCore.QRect(490, 20, 95, 31))
        self.reg.setObjectName("reg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.reg.clicked.connect(self.pressedreg)
        self.play.clicked.connect(self.pressedplay)
        self.version.addItem("1.18.1")
        self.version.addItem("1.17.1")
        cursor.execute("SELECT username FROM accounts")
        rows = cursor.fetchall()
        for row in rows:
            self.selectacc.addItem(row[0])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enelix"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.login.setText(_translate("MainWindow", "login"))
        self.Nickname.setPlaceholderText(_translate("MainWindow", "Nickname"))
        self.reg.setText(_translate("MainWindow", "reg"))

    def pressedreg(self):
        nick = self.Nickname.text()
        access_token = loginmine()
        uuid = uuidfinder(nick)
        cursor.execute(f"INSERT INTO accounts (username, uuid, accessToken) VALUES ('{nick}', '{uuid}', '{access_token}')")
        con.commit()


    def pressedplay(self):
        username=self.selectacc.currentText()
        cursor.execute(f"SELECT * FROM accounts WHERE username = '{username}'")
        rows = cursor.fetchall()
        for row in rows:
            sys.argv = [self.version.currentText(), row[0], row[1], row[2]]
            execfile('game.py')

import launcher_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())