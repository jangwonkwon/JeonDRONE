import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

print('GPIO test')

try:
	while True:
		if GPIO.input(23)==0:
			print('DANGER')
#		elif GPIO.input(23)==1:
#			print('safe')

		time.sleep(0.1)


except KeyboardInterrupt:
	GPIO.cleanup()
	print("bye")


