from machine import Pin
import time
LED = Pin(18, Pin.OUT)
Button = Pin(35, Pin.IN)
def toggle(LED):
	LED.value(not LED.value())
while Thread[0]:
	while 0 == Button.value():
		toggle(LED)
		time.sleep(0.2)