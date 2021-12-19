# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

from gui import Ui_Dialog

#class Mainclass(QtWidgets.QMainWindow):

class Main_Dialog(Ui_Dialog):
    def func(self):
        ui.Single_FWD.clicked.connect(self.test1)
    def test1(self):
        print("yes")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    functest = Main_Dialog()
    functest.func()

    Dialog.show()
    sys.exit(app.exec_())
