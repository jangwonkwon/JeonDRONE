#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
from time import sleep
import curses

# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWORD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 26  #37 pin
ENB = 0   #27 pin

#GPIO PIN
IN1 = 19  #37 pin
IN2 = 13  #35 pin
IN3 = 6   #31 pin
IN4 = 5   #29 pin

# 핀 설정 함수
def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100khz 로 PWM 동작 시킴
    pwm = GPIO.PWM(EN, 1)
    # 우선 PWM 멈춤.
    pwm.start(0)
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):

    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)

    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)

    #뒤로
    elif stat == BACKWORD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)


# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

def main_key_everytime(window):
        while True:
                key = window.getch()
                curses.halfdelay(1)
                print(key)
                if key == 49:
                        print('1')
                        setMotor(CH1, 10, FORWARD)
                        setMotor(CH2, 10, FORWARD)
                elif key ==50:
                        print('2')
                        setMotor(CH1, 20, FORWARD)
                        setMotor(CH2, 20, FORWARD)
                elif key == 51:
                        print('3')
                        setMotor(CH1, 30, FORWARD)
                        setMotor(CH2, 30, FORWARD)
                elif key == 52:
                        print('4')
                        setMotor(CH2, 40, FORWARD)
                        setMotor(CH2, 40, FORWARD)
                elif key ==53:
                        print('5')
                        setMotor(CH1, 50, FORWARD)
                        setMotor(CH2, 50, FORWARD)

                elif key ==54:
                        print('6')
                        setMotor(CH1, 12.4, FORWARD)
                        setMotor(CH2, 12.4, FORWARD)

                elif key ==55:
                        print('7')
                        setMotor(CH1, 22, FORWARD)
                        setMotor(CH2, 22, FORWARD)

                elif key ==56:
                        print('8')
                        setMotor(CH1, 24, FORWARD)
                        setMotor(CH2, 24, FORWARD)

                elif key ==57:
                        print('9')
                        setMotor(CH1, 26, FORWARD)
                        setMotor(CH2, 26, FORWARD)

                elif key == 48:
			#curses.halfdelay(1)
                        setMotor(CH1, 6, STOP)
                        setMotor(CH2, 6, STOP)



#curses.wrapper(main2)
curses.wrapper(main_key_everytime)


# 종료
GPIO.cleanup()
