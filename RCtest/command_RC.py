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
	if Command == 'S':
		R.off()
		L.off()
	if Command == 'R':
		R.off()
		L.on()
	if Command == 'L':
		R.on()
		L.off()




