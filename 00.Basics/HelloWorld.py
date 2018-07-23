from machine import Pin
import time
LED = Pin(18, Pin.OUT)
while Thread[0]:
	LED.value(1) # Let the LED on.