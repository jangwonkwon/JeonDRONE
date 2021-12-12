
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 636)
        self.buttonBox_Cancel_OK = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox_Cancel_OK.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox_Cancel_OK.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Cancel_OK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Cancel_OK.setObjectName("buttonBox_Cancel_OK")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 70, 105, 31))
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_1.setGeometry(QtCore.QRect(50, 150, 64, 23))
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(50, 180, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalSlider_j = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_j.setGeometry(QtCore.QRect(50, 210, 160, 26))
        self.horizontalSlider_j.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_j.setObjectName("horizontalSlider_j")
        self.dial_knob = QtWidgets.QDial(Dialog)
        self.dial_knob.setGeometry(QtCore.QRect(290, 73, 81, 131))
        self.dial_knob.setObjectName("dial_knob")
        self.Duty_high = QtWidgets.QPushButton(Dialog)
        self.Duty_high.setGeometry(QtCore.QRect(240, 380, 105, 31))
        self.Duty_high.setObjectName("Duty_high")
        self.Fre_high = QtWidgets.QPushButton(Dialog)
        self.Fre_high.setGeometry(QtCore.QRect(120, 380, 105, 31))
        self.Fre_high.setObjectName("Fre_high")
        self.Fre_low = QtWidgets.QPushButton(Dialog)
        self.Fre_low.setGeometry(QtCore.QRect(120, 420, 105, 31))
        self.Fre_low.setObjectName("Fre_low")
        self.Duty_low = QtWidgets.QPushButton(Dialog)
        self.Duty_low.setGeometry(QtCore.QRect(240, 420, 105, 31))
        self.Duty_low.setObjectName("Duty_low")
        self.Frequency_text = QtWidgets.QLineEdit(Dialog)
        self.Frequency_text.setGeometry(QtCore.QRect(390, 380, 113, 32))
        self.Frequency_text.setObjectName("Frequency_text")
        self.Duty_text = QtWidgets.QLineEdit(Dialog)
        self.Duty_text.setGeometry(QtCore.QRect(390, 440, 113, 32))
        self.Duty_text.setObjectName("Duty_text")
        self.Fre_label = QtWidgets.QLabel(Dialog)
        self.Fre_label.setGeometry(QtCore.QRect(390, 360, 131, 22))
        self.Fre_label.setObjectName("Fre_label")
        self.Duty_label = QtWidgets.QLabel(Dialog)
        self.Duty_label.setGeometry(QtCore.QRect(390, 420, 68, 22))
        self.Duty_label.setObjectName("Duty_label")
        self.buttonBox_Cancel_OK.raise_()
        self.pushButton.raise_()
        self.lcdNumber_1.raise_()
        self.lcdNumber_2.raise_()
        self.dial_knob.raise_()
        self.horizontalSlider_j.raise_()
        self.Duty_high.raise_()
        self.Fre_high.raise_()
        self.Fre_low.raise_()
        self.Duty_low.raise_()
        self.Frequency_text.raise_()
        self.Duty_text.raise_()
        self.Fre_label.raise_()
        self.Duty_label.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox_Cancel_OK.accepted.connect(Dialog.accept)
        self.buttonBox_Cancel_OK.rejected.connect(Dialog.reject)
        self.buttonBox_Cancel_OK.accepted.connect(self.buttonBox_Cancel_OK.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.Motor_pin1 = 18   # pin Number
        self.Motor_pin2 = 23
        self.Motor_pin3 = 24
        self.Motor_pin4 = 25



        self.frequency = 300  # default Frequency
        self.duty = 35        # default duty

        GPIO.setmode(GPIO.BCM)

        #add for multiple motor 
        GPIO.setup(self.Motor_pin1, GPIO.OUT)
        GPIO.setup(self.Motor_pin2, GPIO.OUT)
        GPIO.setup(self.Motor_pin3, GPIO.OUT)
        GPIO.setup(self.Motor_pin4, GPIO.OUT)

        self.pwm_led1 = GPIO.PWM(self.Motor_pin1,self.frequency)
        self.pwm_led2 = GPIO.PWM(self.Motor_pin2,self.frequency)
        self.pwm_led3 = GPIO.PWM(self.Motor_pin3,self.frequency)
        self.pwm_led4 = GPIO.PWM(self.Motor_pin4,self.frequency)


        self.pwm_led1.start(self.duty)
        self.pwm_led2.start(self.duty)
        self.pwm_led3.start(self.duty)
        self.pwm_led4.start(self.duty)

        self.drone(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "click_here"))
        self.horizontalSlider_j.setWhatsThis(_translate("Dialog", "<html><head/><body><p>change_1</p></body></html>"))
        self.Duty_high.setText(_translate("Dialog", "Duty_up"))
        self.Fre_high.setText(_translate("Dialog", "Fre_up"))
        self.Fre_low.setText(_translate("Dialog", "Fre_down"))
        self.Duty_low.setText(_translate("Dialog", "Duty_down"))
        self.Fre_label.setText(_translate("Dialog", "Frequency [MHz]"))
        self.Duty_label.setText(_translate("Dialog", "Duty [%]"))


    def drone(self, Dialog):
#        self.Frequency_text.returnPressed.connect(self.frequency_enter)    # not yet
#        self.Duty_text.returnPressed.connect(self.duty_enter)    # not yet
        self.pushButton.clicked.connect(self.btn_clicked)
        self.Fre_high.clicked.connect(self.frequency_high)
        self.Fre_low.clicked.connect(self.frequency_low)
        self.Duty_high.clicked.connect(self.duty_high)
        self.Duty_low.clicked.connect(self.duty_low)


    def btn_clicked(self):
        print("button clicked")
        self.frequency = float(self.Frequency_text.text())
        self.Frequency_set()
        self.duty = float(self.Duty_text.text())
        self.duty_set()


    def frequency_enter(self):
         self.frequency = float(self.Frequency_text.text())
         self.Frequency_set()

    def frequency_high(self):
         self.frequency += 10
#         print(self.frequency)
         self.Frequency_set()
    def frequency_low(self):
        if self.frequency - 10 >0:
            self.frequency = self.frequency -10
#        print(self.frequency)
        self.Frequency_set()

    def duty_enter(self):
        self.duty = float(self.Duty_text.text())
        self.duty_set()

    def duty_high(self):
        if self.duty+1 < 100:
            self.duty = self.duty + 0.1
#        print(self.duty)
        self.duty_set()

    def duty_low(self):
        if self.duty-1 >=0:
            self.duty = self.duty - 0.1
#        print(self.duty)
        self.duty_set()

    def Frequency_set(self):
        print("frequency = "+str(self.frequency))
        self.pwm_led1.ChangeFrequency(self.frequency)
        self.pwm_led2.ChangeFrequency(self.frequency)
        self.pwm_led3.ChangeFrequency(self.frequency)
        self.pwm_led4.ChangeFrequency(self.frequency)



    def duty_set(self):
        print("duty = "+str(self.duty))
        self.pwm_led1.ChangeDutyCycle(self.duty)
        self.pwm_led2.ChangeDutyCycle(self.duty)
        self.pwm_led3.ChangeDutyCycle(self.duty)
        self.pwm_led4.ChangeDutyCycle(self.duty)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
#    GPIO.cleanup()
#    print("program exit")

