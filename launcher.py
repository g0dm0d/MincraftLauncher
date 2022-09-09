import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


from authAPI import loginmine
from UUID import uuidfinder
from launcherbg import Ui_Dialog


async def test():
    await loginmine()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


    ui.Play.clicked.connect(asyncio.run(test()))


    con = sqlite3.connect('enelix.db')
    cursor = con.cursor()
