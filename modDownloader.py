from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QPushButton
from tools.mods.modManager import searchMod


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(918, 715)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(120, 60, 641, 651))
        self.listWidget.setObjectName("listWidget")


        self.textbox = QLineEdit(Form)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.returnPressed.connect(self.searchMod)
        
        # connect button to function on_click


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def on_click(self, mod='test'):
        print(mod)

    def add_card(self, name, modid):
        itemN = QtWidgets.QListWidgetItem() 
        #Create widget
        widget = QtWidgets.QWidget()
        widgetText =  QtWidgets.QLabel(name)
        widgetButton =  QtWidgets.QPushButton("Download")
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(widgetText)
        widgetLayout.addWidget(widgetButton)
        widgetLayout.addStretch()
        
        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)  
        itemN.setSizeHint(widget.sizeHint())    
        
        #Add widget to QListWidget funList
        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, widget)

        widgetButton.clicked.connect(lambda:self.on_click(modid))

    def searchMod(self):
        textboxValue = self.textbox.text()
        modsList = searchMod(textboxValue)
        for i in modsList:
            self.add_card(i[0],i[1])

import mods_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
