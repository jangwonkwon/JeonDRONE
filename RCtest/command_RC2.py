
from gpiozero import LED,Button
from time import sleep

R = LED(20)
L = LED(21)

G = LED(17)
Command = 0


while True:
	sleep(0.1)
	G.on()
	Command = input("Command :  ")

	if Command == 'F':  # Forward
		R.on()
		L.on()
	elif Command == 'S':
		R.off()
		L.off()
	elif Command == 'R':
		R.off()
		L.on()
	elif Command == 'L':
		R.on()
		L.off()




