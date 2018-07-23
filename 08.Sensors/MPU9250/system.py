# This File Will Loop execute.

from machine import Pin
import time

LED = Pin(18, Pin.OUT) # Set Running Led

# Python and WebDAV cross, which leads to the Python sequence is not stable.
# So You Can Switch Python and WebDAV through external Button to stable execute.
Button = Pin(27, Pin.IN)
while 0 == Button.value():
	time.sleep(0.2) # Set 0.1s Python execute time.
	LED.value(1)
	time.sleep(0.2) # Set 0.1s Python execute time.
	LED.value(0)
