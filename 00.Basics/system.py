# This File Will Loop execute.
from machine import Pin
import time
# Python and WebDAV cross, which leads to the Python sequence is not stable.
# So You Can Switch Python and WebDAV through external Button to stable execute.
Button = Pin(27, Pin.IN)
while 0 == Button.value():
	pass