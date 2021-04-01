import RPi.GPIO as GPIO
import time

try:
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
    arm = GPIO.PWM(16, 500)
    channels = [pitch,roll,yaw,throttle]
    arm.start(90)
    throttle.start(49)
    pitch.start(75)
    roll.start(75)
    yaw.start(95)
    time.sleep(4)
    for channel in channels:
        channel.ChangeDutyCycle(75)
    while True:
        continue 
except:
    arm.stop()
    for channel in channels:
        channel.stop()
    GPIO.cleanup()
