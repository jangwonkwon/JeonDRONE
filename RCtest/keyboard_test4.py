import curses 
from gpiozero import Robot,LED,Button


R = LED(20)
Y = LED(21)
G = LED(17)

actions = {259:print('UP'),curses.KEY_DOWN:print('DOWN'),curses.KEY_LEFT:R.on(),curses.KEY_RIGHT:Y.on()}

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
			elif key ==258:
				print('down')
			elif key == 260:
				print('left')
				Y.on()
			elif key == 261:
				print('right')
				R.on()

			while next_key == key:
				next_key = window.getch()
			#KEY UP
 			Y.off()
			R.off()
			G.off()

			G.on()


curses.wrapper(main)
