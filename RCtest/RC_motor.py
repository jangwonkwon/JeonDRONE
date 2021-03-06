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
    pwm = GPIO.PWM(EN, 100)
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


def main(window):
	next_key = None
	while True:
		curses.halfdelay(1)
		if next_key is None:
			key = window.getch()
		else:
			key = next_key
			next_key = None

		if key != -1:
			curses.halfdelay(3)
			next_key = key

			if key == 259:
				print('up')
				setMotor(CH1, 80, FORWARD)
				setMotor(CH2, 80, FORWARD)
			elif key ==258:
				print('down')
				setMotor(CH1, 40, BACKWORD)
				setMotor(CH2, 40, BACKWORD)
			elif key == 260:
				print('left')
				setMotor(CH1, 60, FORWARD)
				setMotor(Ch2, 80, STOP)
			elif key == 261:
				print('right')
				setMotor(Ch1, 60, FORWARD)
				setMotor(CH2, 60, FORWARD)

			while next_key == key:
				next_key = window.getch()
			#KEY UP #정지
			setMotor(CH1, 80, STOP)
			setMotor(CH2, 80, STOP)

def main2(window):
	next_key = None

	while True:
		key = window.getch()
		print(key)
		print(next_key)
#		if key != -1:
#		curses.halfdelay(1)
		next_key = key
		if key == 259:
			print('up')
			setMotor(CH1, 80, FORWARD)
			setMotor(CH2, 80, FORWARD)
		elif key ==258:
			print('down')
			setMotor(CH1, 40, BACKWORD)
			setMotor(CH2, 40, BACKWORD)
		elif key == 260:
			print('left')
			setMotor(CH1, 60, FORWARD)
		elif key == 261:
			print('right')
			setMotor(CH2, 60, FORWARD)

		while next_key == key:
			next_key = window.getch()
		#else:
		#KEY UP #정지
		curses.halfdelay(1)
		setMotor(CH1, 80, STOP)
		setMotor(CH2, 80, STOP)



def main3(window):
        next_key = None
	key = window.getch()
        while True:

		curses.halfdelay(1)
                print(key)
                print(next_key)
                if key == 259:
                        print('up')
                        setMotor(CH1, 80, FORWARD)
                        setMotor(CH2, 80, FORWARD)
                elif key ==258:
                        print('down')
                        setMotor(CH1, 40, BACKWORD)
                        setMotor(CH2, 40, BACKWORD)
                elif key == 260:
                        print('left')
                        setMotor(CH1, 60, FORWARD)
                elif key == 261:
                        print('right')
                        setMotor(CH2, 60, FORWARD)

                while next_key == key:
                        next_key = window.getch()
		key = next_key
                #KEY UP #정지
                curses.halfdelay(1)
                setMotor(CH1, 80, STOP)
                setMotor(CH2, 80, STOP)


def main_key_everytime(window):
        while True:
                key = window.getch()
		curses.halfdelay(1)
                print(key)
                if key == 259:
                        print('up')
                        setMotor(CH1, 80, FORWARD)
                        setMotor(CH2, 80, FORWARD)
                elif key ==258:
                        print('down')
                        setMotor(CH1, 40, BACKWORD)
                        setMotor(CH2, 40, BACKWORD)
                elif key == 260:
                        print('left')
                        setMotor(CH1, 60, FORWARD)
                elif key == 261:
                        print('right')
                        setMotor(CH2, 60, FORWARD)
                elif key == -1:
			#curses.halfdelay(1)
			setMotor(CH1, 80, STOP)
			setMotor(CH2, 80, STOP)



curses.wrapper(main2)
#curses.wrapper(main_key_everytime)


# 종료
GPIO.cleanup()
