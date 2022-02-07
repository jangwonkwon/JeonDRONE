
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


#            AngleX_target, AngleY_target, AngleZ_target, PosX_target, PosY_target, Height_target

#            AngleX_const, AngleX_v_const, AngleX_a_const
#            AngleY_const, AngleY_v_const, AngleY_a_const
#            AngleZ_const, AngleZ_v_const, AngleZ_a_const

#            PosX_const, PosX_v_const, PosX_a_const
#            PosY_const, PosY_v_const, PosY_a_const

#            Height_const, Height_v_const, Height_a_const


#            A, B, C = 6050.read(targetAX, targetAY, targetAZ, targetPX, targetPY, targetH)

#            AngleX_P, AngleX_I, AngleX_D
#            AngleY_P, AngleY_I, AngleY_D
#            AngleZ_P, AngleZ_I, AngleZ_D

#            PosX_P, PosX_I, PosX_D
#            PosY_P, PosY_I, PosY_D

#            Height_P, Height_I, Height_D


            if ui.Gain_RotationX_check.isChecked() == True:
               delta = ui.GLXP * AngleX_P + ui.GLXI * AngleX_I  + ui.GLXD * AngleX_D

               ui.duty_FR = ui.duty_FR +- delta
               ui.duty_FL = ui.duty_FL +- delta
               ui.duty_BR = ui.duty_BR +- delta
               ui.duty_BL = ui.duty_BL +- delta

            if ui.Gain_RotationY_check.isChecked() == True:
               delta = ui.GLYP * AngleY_P + ui.GLYI * AngleY_I  + ui.GLYD * AngleY_D

               ui.duty_FR = ui.duty_FR +- delta
               ui.duty_FL = ui.duty_FL +- delta
               ui.duty_BR = ui.duty_BR +- delta
               ui.duty_BL = ui.duty_BL +- delta

            if ui.Gain_RotationZ_check.isChecked() == True:
               delta = ui.GLZP * AngleZ_P + ui.GLZI * AngleZ_I  + ui.GLZD * AngleZ_D

               ui.duty_FR = ui.duty_FR +- delta
               ui.duty_FL = ui.duty_FL +- delta
               ui.duty_BR = ui.duty_BR +- delta
               ui.duty_BL = ui.duty_BL +- delta

            if ui.Gain_PosX_check.isChecked() == True:
               delta = ui.GVXP * PosX_P + ui.GVXI * PosX_I  + ui.GVXD * PosX_D

               ui.duty_FR = ui.duty_FR +- delta
               ui.duty_FL = ui.duty_FL +- delta
               ui.duty_BR = ui.duty_BR +- delta
               ui.duty_BL = ui.duty_BL +- delta


            if ui.Gain_PosY_check.isChecked() == True:
               delta = ui.GVYP * PosY_P + ui.GVYI * PosY_I  + ui.GVYD * PosY_D

               ui.duty_FR = ui.duty_FR +- delta
               ui.duty_FL = ui.duty_FL +- delta
               ui.duty_BR = ui.duty_BR +- delta
               ui.duty_BL = ui.duty_BL +- delta

            if ui.Gain_Height_check.isChecked() == True:
               delta = ui.GHP * Height_P + ui.GHI * Height_I  + ui.GHD * Height_D

               ui.duty_FR = ui.duty_FR +- delta
               ui.duty_FL = ui.duty_FL +- delta
               ui.duty_BR = ui.duty_BR +- delta
               ui.duty_BL = ui.duty_BL +- delta

            function_work.duty_set()


            ui.Height_LCD.display(self.altitude)
#            print(self.altitude)
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


    def drone_off(self):
        ui.duty_FR=0
        ui.duty_FL=0
        ui.duty_BR=0
        ui.duty_BL=0

        self.duty_set()

        ui.pwm_FR.stop()
        ui.pwm_FL.stop()
        ui.pwm_BR.stop()
        ui.pwm_BL.stop()
        GPIO.cleanup()

        print()
        print("Drone OFF !")
        print()

        QCoreApplication.instance().quit()

        self.display()


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

        ui.Exit_button.clicked.connect(self.drone_off)
#        ui.Exit_button.clicked.connect(QCoreApplication.instance().quit)


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
#        print("frequency = "+str(ui.frequency))
        ui.pwm_FR.ChangeFrequency(ui.frequency)
        ui.pwm_FL.ChangeFrequency(ui.frequency)
        ui.pwm_BR.ChangeFrequency(ui.frequency)
        ui.pwm_BL.ChangeFrequency(ui.frequency)
        self.display()

    def duty_set(self):
#        print("duty = "+str(ui.duty_FR))
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

