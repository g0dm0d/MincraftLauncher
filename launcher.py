import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication



# from PyQt5 import QtCore, QtGui, QtWidgets


from authAPI import loginmine
from UUID import uuidfinder


class Launcher(QDialog):
    def __init__(self):
        super(Launcher, self).__init__()
        loadUi("launcher.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    ui = Launcher()
    #ui.setupUi.Play.clicked.connect(print("hello"))
    widget.addWidget(ui)
    widget.setFixedSize(500, 500)
    widget.show
    sys.exit(app.exec_())




    con = sqlite3.connect('enelix.db')
    cursor = con.cursor()
