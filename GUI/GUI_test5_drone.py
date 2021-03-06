# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 622)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.Set_button = QtWidgets.QPushButton(Dialog)
        self.Set_button.setGeometry(QtCore.QRect(293, 520, 105, 31))
        self.Set_button.setObjectName("Set_button")
        self.Duty_high = QtWidgets.QPushButton(Dialog)
        self.Duty_high.setGeometry(QtCore.QRect(173, 420, 105, 31))
        self.Duty_high.setObjectName("Duty_high")
        self.Fre_high = QtWidgets.QPushButton(Dialog)
        self.Fre_high.setGeometry(QtCore.QRect(53, 420, 105, 31))
        self.Fre_high.setObjectName("Fre_high")
        self.Fre_low = QtWidgets.QPushButton(Dialog)
        self.Fre_low.setGeometry(QtCore.QRect(53, 460, 105, 31))
        self.Fre_low.setObjectName("Fre_low")
        self.Duty_low = QtWidgets.QPushButton(Dialog)
        self.Duty_low.setGeometry(QtCore.QRect(173, 460, 105, 31))
        self.Duty_low.setObjectName("Duty_low")
        self.Frequency_text = QtWidgets.QLineEdit(Dialog)
        self.Frequency_text.setGeometry(QtCore.QRect(293, 410, 113, 32))
        self.Frequency_text.setObjectName("Frequency_text")
        self.Duty_text = QtWidgets.QLineEdit(Dialog)
        self.Duty_text.setGeometry(QtCore.QRect(293, 470, 113, 32))
        self.Duty_text.setObjectName("Duty_text")
        self.Fre_label = QtWidgets.QLabel(Dialog)
        self.Fre_label.setGeometry(QtCore.QRect(293, 390, 131, 22))
        self.Fre_label.setObjectName("Fre_label")
        self.Duty_label = QtWidgets.QLabel(Dialog)
        self.Duty_label.setGeometry(QtCore.QRect(293, 450, 68, 22))
        self.Duty_label.setObjectName("Duty_label")
        self.Height_split = QtWidgets.QSplitter(Dialog)
        self.Height_split.setGeometry(QtCore.QRect(100, 200, 281, 23))
        self.Height_split.setOrientation(QtCore.Qt.Horizontal)
        self.Height_split.setObjectName("Height_split")
        self.Height_LCD = QtWidgets.QLCDNumber(self.Height_split)
        self.Height_LCD.setObjectName("Height_LCD")
        self.Height_v_LCD = QtWidgets.QLCDNumber(self.Height_split)
        self.Height_v_LCD.setObjectName("Height_v_LCD")
        self.Height_a_LCD = QtWidgets.QLCDNumber(self.Height_split)
        self.Height_a_LCD.setObjectName("Height_a_LCD")
        self.Pos_split = QtWidgets.QSplitter(Dialog)
        self.Pos_split.setGeometry(QtCore.QRect(100, 270, 281, 23))
        self.Pos_split.setOrientation(QtCore.Qt.Horizontal)
        self.Pos_split.setObjectName("Pos_split")
        self.Pos_LCD = QtWidgets.QLCDNumber(self.Pos_split)
        self.Pos_LCD.setObjectName("Pos_LCD")
        self.Pos_v_LCD = QtWidgets.QLCDNumber(self.Pos_split)
        self.Pos_v_LCD.setObjectName("Pos_v_LCD")
        self.Pos_a_LCD = QtWidgets.QLCDNumber(self.Pos_split)
        self.Pos_a_LCD.setObjectName("Pos_a_LCD")
        self.Single_R = QtWidgets.QPushButton(Dialog)
        self.Single_R.setGeometry(QtCore.QRect(920, 410, 105, 31))
        self.Single_R.setObjectName("Single_R")
        self.Single_L = QtWidgets.QPushButton(Dialog)
        self.Single_L.setGeometry(QtCore.QRect(680, 420, 105, 31))
        self.Single_L.setObjectName("Single_L")
        self.Single_BWD = QtWidgets.QPushButton(Dialog)
        self.Single_BWD.setGeometry(QtCore.QRect(800, 470, 105, 31))
        self.Single_BWD.setObjectName("Single_BWD")
        self.Single_FWD = QtWidgets.QPushButton(Dialog)
        self.Single_FWD.setGeometry(QtCore.QRect(800, 360, 105, 31))
        self.Single_FWD.setObjectName("Single_FWD")
        self.F_button = QtWidgets.QRadioButton(Dialog)
        self.F_button.setGeometry(QtCore.QRect(520, 380, 71, 27))
        self.F_button.setObjectName("F_button")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(570, 130, 446, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Rotation_layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Rotation_layout.setContentsMargins(0, 0, 0, 0)
        self.Rotation_layout.setObjectName("Rotation_layout")
        self.GHP = QtWidgets.QLineEdit(self.layoutWidget)
        self.GHP.setObjectName("GHP")
        self.Rotation_layout.addWidget(self.GHP)
        self.GHI = QtWidgets.QLineEdit(self.layoutWidget)
        self.GHI.setObjectName("GHI")
        self.Rotation_layout.addWidget(self.GHI)
        self.GHD = QtWidgets.QLineEdit(self.layoutWidget)
        self.GHD.setObjectName("GHD")
        self.Rotation_layout.addWidget(self.GHD)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(570, 190, 446, 34))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.Height_layout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.Height_layout.setContentsMargins(0, 0, 0, 0)
        self.Height_layout.setObjectName("Height_layout")
        self.GLP = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.GLP.setObjectName("GLP")
        self.Height_layout.addWidget(self.GLP)
        self.GLI = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.GLI.setObjectName("GLI")
        self.Height_layout.addWidget(self.GLI)
        self.GLD = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.GLD.setObjectName("GLD")
        self.Height_layout.addWidget(self.GLD)
        self.P_label = QtWidgets.QLabel(Dialog)
        self.P_label.setGeometry(QtCore.QRect(640, 100, 31, 22))
        self.P_label.setObjectName("P_label")
        self.I_label = QtWidgets.QLabel(Dialog)
        self.I_label.setGeometry(QtCore.QRect(790, 100, 31, 22))
        self.I_label.setObjectName("I_label")
        self.D_label = QtWidgets.QLabel(Dialog)
        self.D_label.setGeometry(QtCore.QRect(940, 100, 31, 22))
        self.D_label.setObjectName("D_label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(460, 90, 571, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(1020, 100, 20, 221))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Gain_Rotation_label = QtWidgets.QLabel(Dialog)
        self.Gain_Rotation_label.setGeometry(QtCore.QRect(480, 140, 81, 22))
        self.Gain_Rotation_label.setObjectName("Gain_Rotation_label")
        self.Gain_Height_label = QtWidgets.QLabel(Dialog)
        self.Gain_Height_label.setGeometry(QtCore.QRect(490, 200, 51, 22))
        self.Gain_Height_label.setObjectName("Gain_Height_label")
        self.Gain_Position_label = QtWidgets.QLabel(Dialog)
        self.Gain_Position_label.setGeometry(QtCore.QRect(480, 270, 61, 22))
        self.Gain_Position_label.setObjectName("Gain_Position_label")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(460, 310, 571, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(450, 100, 20, 221))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Duty_FL_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_FL_LCD.setGeometry(QtCore.QRect(700, 360, 64, 23))
        self.Duty_FL_LCD.setObjectName("Duty_FL_LCD")
        self.Duty_FR_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_FR_LCD.setGeometry(QtCore.QRect(950, 360, 64, 23))
        self.Duty_FR_LCD.setObjectName("Duty_FR_LCD")
        self.Duty_BL_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_BL_LCD.setGeometry(QtCore.QRect(710, 510, 64, 23))
        self.Duty_BL_LCD.setObjectName("Duty_BL_LCD")
        self.Duty_BR_LCD = QtWidgets.QLCDNumber(Dialog)
        self.Duty_BR_LCD.setGeometry(QtCore.QRect(950, 500, 64, 23))
        self.Duty_BR_LCD.setObjectName("Duty_BR_LCD")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(40, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.R_button = QtWidgets.QRadioButton(Dialog)
        self.R_button.setGeometry(QtCore.QRect(580, 420, 71, 27))
        self.R_button.setObjectName("R_button")
        self.B_button = QtWidgets.QRadioButton(Dialog)
        self.B_button.setGeometry(QtCore.QRect(520, 460, 71, 27))
        self.B_button.setObjectName("B_button")
        self.L_button = QtWidgets.QRadioButton(Dialog)
        self.L_button.setGeometry(QtCore.QRect(460, 420, 71, 27))
        self.L_button.setObjectName("L_button")
        self.Fre_Step_text = QtWidgets.QLineEdit(Dialog)
        self.Fre_Step_text.setGeometry(QtCore.QRect(43, 520, 113, 32))
        self.Fre_Step_text.setObjectName("Fre_Step_text")
        self.Duty_Step_text = QtWidgets.QLineEdit(Dialog)
        self.Duty_Step_text.setGeometry(QtCore.QRect(173, 520, 113, 32))
        self.Duty_Step_text.setObjectName("Duty_Step_text")
        self.Move_Step_text = QtWidgets.QLineEdit(Dialog)
        self.Move_Step_text.setGeometry(QtCore.QRect(480, 530, 113, 32))
        self.Move_Step_text.setObjectName("Move_Step_text")
        self.Step_Fre = QtWidgets.QLabel(Dialog)
        self.Step_Fre.setGeometry(QtCore.QRect(73, 500, 68, 22))
        self.Step_Fre.setObjectName("Step_Fre")
        self.Step_Duty = QtWidgets.QLabel(Dialog)
        self.Step_Duty.setGeometry(QtCore.QRect(190, 500, 81, 22))
        self.Step_Duty.setObjectName("Step_Duty")
        self.Step_Move = QtWidgets.QLabel(Dialog)
        self.Step_Move.setGeometry(QtCore.QRect(487, 510, 91, 22))
        self.Step_Move.setObjectName("Step_Move")
        self.Height_label = QtWidgets.QLabel(Dialog)
        self.Height_label.setGeometry(QtCore.QRect(120, 180, 51, 22))
        self.Height_label.setObjectName("Height_label")
        self.Angle_label = QtWidgets.QLabel(Dialog)
        self.Angle_label.setGeometry(QtCore.QRect(130, 120, 81, 22))
        self.Angle_label.setObjectName("Angle_label")
        self.Position_label = QtWidgets.QLabel(Dialog)
        self.Position_label.setGeometry(QtCore.QRect(110, 250, 61, 22))
        self.Position_label.setObjectName("Position_label")
        self.Angle_v_label = QtWidgets.QLabel(Dialog)
        self.Angle_v_label.setGeometry(QtCore.QRect(220, 120, 81, 22))
        self.Angle_v_label.setObjectName("Angle_v_label")
        self.Angle_a_label = QtWidgets.QLabel(Dialog)
        self.Angle_a_label.setGeometry(QtCore.QRect(310, 120, 81, 22))
        self.Angle_a_label.setObjectName("Angle_a_label")
        self.Height_v_label = QtWidgets.QLabel(Dialog)
        self.Height_v_label.setGeometry(QtCore.QRect(210, 180, 71, 22))
        self.Height_v_label.setObjectName("Height_v_label")
        self.Height_a_label = QtWidgets.QLabel(Dialog)
        self.Height_a_label.setGeometry(QtCore.QRect(300, 180, 71, 22))
        self.Height_a_label.setObjectName("Height_a_label")
        self.Position_v_label = QtWidgets.QLabel(Dialog)
        self.Position_v_label.setGeometry(QtCore.QRect(210, 250, 81, 22))
        self.Position_v_label.setObjectName("Position_v_label")
        self.Position_a_label = QtWidgets.QLabel(Dialog)
        self.Position_a_label.setGeometry(QtCore.QRect(300, 250, 71, 22))
        self.Position_a_label.setObjectName("Position_a_label")
        self.Angle_split = QtWidgets.QSplitter(Dialog)
        self.Angle_split.setGeometry(QtCore.QRect(100, 140, 281, 23))
        self.Angle_split.setOrientation(QtCore.Qt.Horizontal)
        self.Angle_split.setObjectName("Angle_split")
        self.Angle_LCD = QtWidgets.QLCDNumber(self.Angle_split)
        self.Angle_LCD.setObjectName("Angle_LCD")
        self.Angle_v_LCD = QtWidgets.QLCDNumber(self.Angle_split)
        self.Angle_v_LCD.setObjectName("Angle_v_LCD")
        self.Angle_a_LCD = QtWidgets.QLCDNumber(self.Angle_split)
        self.Angle_a_LCD.setObjectName("Angle_a_LCD")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(570, 260, 446, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Pos_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.Pos_layout.setContentsMargins(0, 0, 0, 0)
        self.Pos_layout.setObjectName("Pos_layout")
        self.GVP = QtWidgets.QLineEdit(self.layoutWidget1)
        self.GVP.setObjectName("GVP")
        self.Pos_layout.addWidget(self.GVP)
        self.GVI = QtWidgets.QLineEdit(self.layoutWidget1)
        self.GVI.setObjectName("GVI")
        self.Pos_layout.addWidget(self.GVI)
        self.GVD = QtWidgets.QLineEdit(self.layoutWidget1)
        self.GVD.setObjectName("GVD")
        self.Pos_layout.addWidget(self.GVD)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.drone_set()
        self.drone(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Set_button.setText(_translate("Dialog", "Set"))
        self.Duty_high.setText(_translate("Dialog", "Duty_up"))
        self.Fre_high.setText(_translate("Dialog", "Fre_up"))
        self.Fre_low.setText(_translate("Dialog", "Fre_down"))
        self.Duty_low.setText(_translate("Dialog", "Duty_down"))
        self.Frequency_text.setText(_translate("Dialog", "300"))
        self.Duty_text.setText(_translate("Dialog", "30"))
        self.Fre_label.setText(_translate("Dialog", "Frequency [MHz]"))
        self.Duty_label.setText(_translate("Dialog", "Duty [%]"))
        self.Single_R.setText(_translate("Dialog", "Duty_down"))
        self.Single_L.setText(_translate("Dialog", "Duty_down"))
        self.Single_BWD.setText(_translate("Dialog", "Duty_down"))
        self.Single_FWD.setText(_translate("Dialog", "Duty_down"))
        self.F_button.setText(_translate("Dialog", "F"))
        self.GHP.setText(_translate("Dialog", "1"))
        self.GHI.setText(_translate("Dialog", "0"))
        self.GHD.setText(_translate("Dialog", "0"))
        self.GLP.setText(_translate("Dialog", "1"))
        self.GLI.setText(_translate("Dialog", "0"))
        self.GLD.setText(_translate("Dialog", "0"))
        self.P_label.setText(_translate("Dialog", "P"))
        self.I_label.setText(_translate("Dialog", "I"))
        self.D_label.setText(_translate("Dialog", "D"))
        self.Gain_Rotation_label.setText(_translate("Dialog", "Rotataion"))
        self.Gain_Height_label.setText(_translate("Dialog", "Height"))
        self.Gain_Position_label.setText(_translate("Dialog", "Position"))
        self.Title.setText(_translate("Dialog", "JeonDRONE"))
        self.R_button.setText(_translate("Dialog", "R"))
        self.B_button.setText(_translate("Dialog", "B"))
        self.L_button.setText(_translate("Dialog", "L"))
        self.Fre_Step_text.setText(_translate("Dialog", "10"))
        self.Duty_Step_text.setText(_translate("Dialog", "1"))
        self.Move_Step_text.setText(_translate("Dialog", "3"))
        self.Step_Fre.setText(_translate("Dialog", "Step_Fre"))
        self.Step_Duty.setText(_translate("Dialog", "Step_Duty"))
        self.Step_Move.setText(_translate("Dialog", "Step_move"))
        self.Height_label.setText(_translate("Dialog", "Height"))
        self.Angle_label.setText(_translate("Dialog", "Angle"))
        self.Position_label.setText(_translate("Dialog", "Position"))
        self.Angle_v_label.setText(_translate("Dialog", "Angle_v"))
        self.Angle_a_label.setText(_translate("Dialog", "Anlge_a"))
        self.Height_v_label.setText(_translate("Dialog", "Height_v"))
        self.Height_a_label.setText(_translate("Dialog", "Height_a"))
        self.Position_v_label.setText(_translate("Dialog", "Position_v"))
        self.Position_a_label.setText(_translate("Dialog", "Position_a"))
        self.GVP.setText(_translate("Dialog", "1"))
        self.GVI.setText(_translate("Dialog", "0"))
        self.GVD.setText(_translate("Dialog", "0"))


    def drone_set(self):
        self.Motor_FR = 18   # pin Number
        self.Motor_FL = 23
        self.Motor_BR = 24
        self.Motor_BL = 25

        self.frequency = 300  # default Frequency
        self.duty_FR = 30        # default duty
        self.duty_FL = 30
        self.duty_BR = 30
        self.duty_BL = 30

        GPIO.setmode(GPIO.BCM)

        #add for multiple motor 
        GPIO.setup(self.Motor_FR, GPIO.OUT)
        GPIO.setup(self.Motor_FL, GPIO.OUT)
        GPIO.setup(self.Motor_BR, GPIO.OUT)
        GPIO.setup(self.Motor_BL, GPIO.OUT)

        self.pwm_FR = GPIO.PWM(self.Motor_FR,self.frequency)
        self.pwm_FL = GPIO.PWM(self.Motor_FL,self.frequency)
        self.pwm_BR = GPIO.PWM(self.Motor_BR,self.frequency)
        self.pwm_BL = GPIO.PWM(self.Motor_BL,self.frequency)

        self.pwm_FR.start(self.duty_FR)
        self.pwm_FL.start(self.duty_FL)
        self.pwm_BR.start(self.duty_BR)
        self.pwm_BL.start(self.duty_BL)


    def drone(self, Dialog):
#        self.Frequency_text.returnPressed.connect(self.frequency_enter)    # not yet
#        self.Duty_text.returnPressed.connect(self.duty_enter)    # not yet
        self.Set_button.clicked.connect(self.Set_btn_clicked)
        self.Fre_high.clicked.connect(self.frequency_high)
        self.Fre_low.clicked.connect(self.frequency_low)
        self.Duty_high.clicked.connect(self.duty_high)
        self.Duty_low.clicked.connect(self.duty_low)


    def Set_btn_clicked(self):
        print("Set button clicked")
        self.frequency = float(self.Frequency_text.text())
        self.Frequency_set()
        self.duty_FR = float(self.Duty_text.text())
        self.duty_FL = float(self.Duty_text.text())
        self.duty_BR = float(self.Duty_text.text())
        self.duty_BL = float(self.Duty_text.text())


        self.duty_set()


    def frequency_enter(self):
         self.frequency = float(self.Frequency_text.text())
         self.Frequency_set()

    def frequency_high(self):
         self.frequency += float(self.Fre_Step_text.text())
#         print(self.frequency)
         self.Frequency_set()
    def frequency_low(self):
        if self.frequency - 10 >0:
            self.frequency = self.frequency - float(self.Fre_Step_text.text())
#        print(self.frequency)
        self.Frequency_set()

    def duty_enter(self):
        self.duty = float(self.Duty_text.text())
        self.duty_set()

    def duty_high(self):
#        if self.duty+float(self.Duty_Step_text.text()) < 100:
        self.duty_FR = self.duty_FR + float(self.Duty_Step_text.text())
        self.duty_FL = self.duty_FL + float(self.Duty_Step_text.text())
        self.duty_BR = self.duty_BR + float(self.Duty_Step_text.text())
        self.duty_BL = self.duty_BL + float(self.Duty_Step_text.text())
#        print(self.duty)
        self.duty_set()

    def duty_low(self):
#        if self.duty-float(self.Duty_Step_text.text()) >=0:
        self.duty_FR = self.duty_FR - float(self.Duty_Step_text.text())
        self.duty_FL = self.duty_FL - float(self.Duty_Step_text.text())
        self.duty_BR = self.duty_BR - float(self.Duty_Step_text.text())
        self.duty_BL = self.duty_BL - float(self.Duty_Step_text.text())

#        print(self.duty)
        self.duty_set()

    def Frequency_set(self):
        print("frequency = "+str(self.frequency))
        self.pwm_FR.ChangeFrequency(self.frequency)
        self.pwm_FL.ChangeFrequency(self.frequency)
        self.pwm_BR.ChangeFrequency(self.frequency)
        self.pwm_BL.ChangeFrequency(self.frequency)



    def duty_set(self):
        print("duty = "+str(self.duty_FR))
        self.pwm_FR.ChangeDutyCycle(self.duty_FR)
        self.pwm_FL.ChangeDutyCycle(self.duty_FL)
        self.pwm_BR.ChangeDutyCycle(self.duty_BR)
        self.pwm_BL.ChangeDutyCycle(self.duty_BL)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

