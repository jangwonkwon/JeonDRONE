
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import RPi.GPIO as GPIO
import time
import bmpsensor

from gui import Ui_Dialog
from BMP180_class import BMP180_data

import bmpsensor

class module_work(QThread):
    def run(self):
        while True:
            self.temp, self.pressure, self.altitude = bmpsensor.readBmp180()
            ui.Height_LCD.display(self.altitude)
            print(self.altitude)
#            time.sleep(1)



class Main_Dialog(Ui_Dialog):
    def __init__(self, Diaglog):
        self.drone_set()
        self.drone(Dialog)
#        self.hovering()
        self.display()
#        self.module_work()
        self.worker = module_work()
        self.worker.start()

    def drone_set(self):
        ui.Motor_FR = 18   # pin Number
        ui.Motor_FL = 23
        ui.Motor_BR = 24
        ui.Motor_BL = 25

        ui.frequency = 300  # default Frequency
        ui.duty_FR = 35        # default duty
        ui.duty_FL = 35
        ui.duty_BR = 35
        ui.duty_BL = 35

        GPIO.setmode(GPIO.BCM)

        #add for multiple motor
        GPIO.setup(ui.Motor_FR, GPIO.OUT)
        GPIO.setup(ui.Motor_FL, GPIO.OUT)
        GPIO.setup(ui.Motor_BR, GPIO.OUT)
        GPIO.setup(ui.Motor_BL, GPIO.OUT)

        ui.pwm_FR = GPIO.PWM(ui.Motor_FR,ui.frequency)
        ui.pwm_FL = GPIO.PWM(ui.Motor_FL,ui.frequency)
        ui.pwm_BR = GPIO.PWM(ui.Motor_BR,ui.frequency)
        ui.pwm_BL = GPIO.PWM(ui.Motor_BL,ui.frequency)

        ui.pwm_FR.start(ui.duty_FR)
        ui.pwm_FL.start(ui.duty_FL)
        ui.pwm_BR.start(ui.duty_BR)
        ui.pwm_BL.start(ui.duty_BL)

    def display(self):
        ui.Duty_FR_LCD.display(ui.duty_FR)
        ui.Duty_FL_LCD.display(ui.duty_FL)
        ui.Duty_BR_LCD.display(ui.duty_BR)
        ui.Duty_BL_LCD.display(ui.duty_BL)

        ui.Frequency_LCD.display(ui.frequency)
        ui.Duty_LCD.display(ui.duty_FR)

    def drone(self, Dialog):
        ui.Set_button.clicked.connect(self.Set_btn_clicked)
        ui.Fre_high.clicked.connect(self.frequency_high)
        ui.Fre_low.clicked.connect(self.frequency_low)
        ui.Duty_high.clicked.connect(self.duty_high)
        ui.Duty_low.clicked.connect(self.duty_low)

        ui.Single_FWD.clicked.connect(self.Set_btn_Single_FWD)
        ui.Single_BWD.clicked.connect(self.Set_btn_single_BWD)
        ui.Single_L.clicked.connect(self.Set_btn_Single_R)
        ui.Single_R.clicked.connect(self.Set_btn_Single_L)
        ui.Single_TR.clicked.connect(self.Set_btn_Single_TR)
        ui.Single_TL.clicked.connect(self.Set_btn_Single_TL)

    def Set_btn_clicked(self):
        print("Set button clicked")
        ui.frequency = float(ui.Frequency_text.text())
        self.Frequency_set()
        ui.duty_FR = float(ui.Duty_text.text())
        ui.duty_FL = float(ui.Duty_text.text())
        ui.duty_BR = float(ui.Duty_text.text())
        ui.duty_BL = float(ui.Duty_text.text())
        self.duty_set()

    def frequency_high(self):
         ui.frequency += float(ui.Fre_Step_text.text())
         self.Frequency_set()
    def frequency_low(self):
        if ui.frequency - 10 >0:
            ui.frequency = ui.frequency - float(ui.Fre_Step_text.text())
        self.Frequency_set()

    def duty_high(self):
#        if ui.duty+float(ui.Duty_Step_text.text()) < 100:
        ui.duty_FR = ui.duty_FR + float(ui.Duty_Step_text.text())
        ui.duty_FL = ui.duty_FL + float(ui.Duty_Step_text.text())
        ui.duty_BR = ui.duty_BR + float(ui.Duty_Step_text.text())
        ui.duty_BL = ui.duty_BL + float(ui.Duty_Step_text.text())
        self.duty_set()
    def duty_low(self):
#        if ui.duty-float(ui.Duty_Step_text.text()) >=0:
        ui.duty_FR = ui.duty_FR - float(ui.Duty_Step_text.text())
       	ui.duty_FL = ui.duty_FL - float(ui.Duty_Step_text.text())
        ui.duty_BR = ui.duty_BR - float(ui.Duty_Step_text.text())
        ui.duty_BL = ui.duty_BL - float(ui.Duty_Step_text.text())
        self.duty_set()

    def Frequency_set(self):
        print("frequency = "+str(ui.frequency))
        ui.pwm_FR.ChangeFrequency(ui.frequency)
        ui.pwm_FL.ChangeFrequency(ui.frequency)
        ui.pwm_BR.ChangeFrequency(ui.frequency)
        ui.pwm_BL.ChangeFrequency(ui.frequency)
        self.display()

    def duty_set(self):
        print("duty = "+str(ui.duty_FR))
        ui.pwm_FR.ChangeDutyCycle(ui.duty_FR)
        ui.pwm_FL.ChangeDutyCycle(ui.duty_FL)
        ui.pwm_BR.ChangeDutyCycle(ui.duty_BR)
        ui.pwm_BL.ChangeDutyCycle(ui.duty_BL)
        self.display()

    def Set_btn_Single_FWD(self):
        ui.duty_FR = ui.duty_FR - float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL - float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR + float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL + float(ui.Gap_Duty_text.text())
        self.duty_set()

        time.sleep(float(ui.Single_Time_text.text())/1000)

        ui.duty_FR = ui.duty_FR + float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL + float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR - float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL - float(ui.Gap_Duty_text.text())
        self.duty_set()

    def Set_btn_single_BWD(self):
        ui.duty_FR = ui.duty_FR + float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL + float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR - float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL - float(ui.Gap_Duty_text.text())
        self.duty_set()

        time.sleep(float(ui.Single_Time_text.text())/1000)

        ui.duty_FR = ui.duty_FR - float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL - float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR + float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL + float(ui.Gap_Duty_text.text())
        self.duty_set()

    def Set_btn_Single_R(self):
        ui.duty_FR = ui.duty_FR - float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL + float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR - float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL + float(ui.Gap_Duty_text.text())
        self.duty_set()

        time.sleep(float(ui.Single_Time_text.text())/1000)

        ui.duty_FR = ui.duty_FR + float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL - float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR + float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL - float(ui.Gap_Duty_text.text())
        self.duty_set()

    def Set_btn_Single_L(self):
        ui.duty_FR = ui.duty_FR + float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL - float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR + float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL - float(ui.Gap_Duty_text.text())
        self.duty_set()

        time.sleep(float(ui.Single_Time_text.text())/1000)

        ui.duty_FR = ui.duty_FR - float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL + float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR - float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL + float(ui.Gap_Duty_text.text())
        self.duty_set()

    def Set_btn_Single_TR(self):
        ui.duty_FR = ui.duty_FR - float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL + float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR + float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL - float(ui.Gap_Duty_text.text())
        self.duty_set()

        time.sleep(float(ui.Single_Time_text.text())/1000)

        ui.duty_FR = ui.duty_FR + float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL - float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR - float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL + float(ui.Gap_Duty_text.text())
        self.duty_set()


    def Set_btn_Single_TL(self):
        ui.duty_FR = ui.duty_FR + float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL - float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR - float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL + float(ui.Gap_Duty_text.text())
        self.duty_set()

        time.sleep(float(ui.Single_Time_text.text())/1000)

        ui.duty_FR = ui.duty_FR - float(ui.Gap_Duty_text.text())
        ui.duty_FL = ui.duty_FL + float(ui.Gap_Duty_text.text())
        ui.duty_BR = ui.duty_BR + float(ui.Gap_Duty_text.text())
        ui.duty_BL = ui.duty_BL - float(ui.Gap_Duty_text.text())
        self.duty_set()

    def module_work(self):
        ui.Height_LCD.display(bmp.altitude)


def main():
    print("yes")
    while True:
        function_work.module_work()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
#    bmp = BMP180_data()
#    bmp.startBMP()
    function_work = Main_Dialog(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    main()

