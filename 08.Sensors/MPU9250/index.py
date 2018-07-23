from machine import I2C, Pin
from mpu9250 import MPU9250
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
sensor = MPU9250(i2c)
print("MPU9250 id: " + hex(sensor.whoami))
while Thread[0]:
	print('acceleration:', sensor.acceleration)
	print('gyro:', sensor.gyro)
	print('magnetic:', sensor.magnetic)