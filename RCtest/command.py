from gpiozero import LED,Button
from time import sleep

Red = LED(20)
Yellow = LED(21)

R= 1
Y = 1
C = 0

while True:


	sleep(0.5)
	R = input("Red On/Off: ")
	Y = input("Yellow On/Off: ")
	C = input("script On/off: ")

	if R == 1:
		Red.on()
	else:
		Red.off()

	if Y == 1:
		Yellow.on()
	else:
		Yellow.off()

	if C == 1:
		break

print('A !')
