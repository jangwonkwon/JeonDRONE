# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui211014.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(951, 701)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(480, 240, 113, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 280, 113, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.webView = QtWebKitWidgets.QWebView(Dialog)
        self.webView.setGeometry(QtCore.QRect(10, 10, 441, 341))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 280, 113, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 280, 113, 28))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 320, 56, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 320, 56, 18))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 370, 41, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 400, 41, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 400, 41, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 400, 41, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(600, 240, 56, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(600, 190, 81, 18))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(480, 190, 113, 28))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(480, 150, 113, 28))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(600, 150, 81, 18))
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 400, 41, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 400, 41, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 370, 41, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 400, 41, 31))
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(_translate("Dialog", "20"))
        self.lineEdit_2.setText(_translate("Dialog", "20"))
        self.lineEdit_3.setText(_translate("Dialog", "20"))
        self.lineEdit_4.setText(_translate("Dialog", "20"))
        self.label.setText(_translate("Dialog", "Height"))
        self.label_2.setText(_translate("Dialog", "velocity"))
        self.pushButton.setText(_translate("Dialog", "up"))
        self.pushButton_2.setText(_translate("Dialog", "down"))
        self.pushButton_3.setText(_translate("Dialog", "right"))
        self.pushButton_4.setText(_translate("Dialog", "left"))
        self.label_3.setText(_translate("Dialog", "degree"))
        self.label_4.setText(_translate("Dialog", "acceleration"))
        self.lineEdit_5.setText(_translate("Dialog", "20"))
        self.lineEdit_6.setText(_translate("Dialog", "1"))
        self.label_5.setText(_translate("Dialog", "Height step"))
        self.pushButton_5.setText(_translate("Dialog", "a"))
        self.pushButton_6.setText(_translate("Dialog", "d"))
        self.pushButton_7.setText(_translate("Dialog", "w"))
        self.pushButton_8.setText(_translate("Dialog", "s"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

