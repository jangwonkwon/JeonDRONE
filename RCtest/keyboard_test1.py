from pynput import keyboard

def on_press(key):
	try:
		print('alpha :{0}'.format(key.char))
	except AttributeError:
		print('nono : {0}'.format(key))

def on_release(key):
	print('key released :{0}'.format(key))
	if key == keyboard.key.esc:
		return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()



