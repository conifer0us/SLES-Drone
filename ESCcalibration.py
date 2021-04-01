import RPi.GPIO as GPIO

import time


base_value = 55

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
pitch = GPIO.PWM(18, 500)
roll = GPIO.PWM(13, 500)
yaw = GPIO.PWM(19, 500)
throttle = GPIO.PWM(12, 500)
channels = [pitch,roll,yaw,throttle]
for channel in channels:
        channel.start(base_value)
input ("press return")
throttle.ChangeDutyCycle(99)
time.sleep(2)
throttle.ChangeDutyCycle(45)
time.sleep(2)
for channel in channels:
        channel.stop()
arm.stop()
GPIO.cleanup()
        
