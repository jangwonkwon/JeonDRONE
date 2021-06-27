from gpiozero import LED,Button
from time import sleep

led = LED(17)
button = Button(18)


while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)

	if button.is_pressed:
		print("Pressed")
	else:
		print("Released")


print('A !')
