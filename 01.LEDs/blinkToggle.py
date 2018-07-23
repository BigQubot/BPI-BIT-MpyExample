from machine import Pin
import time
LED = Pin(18, Pin.OUT)
def toggle(LED):
	LED.value(not LED.value())
while Thread[0]:
	time.sleep(0.2) # Set 0.1s Python execute time.
	toggle(LED)