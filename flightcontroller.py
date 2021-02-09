# This is the main script file that will regulate the raspberry pi's communication with input and output to flight controllers. Feel free to edit this code and push to main branch.
# For big changes to the code, push to master branch and generate a pull request into the main branch. This way, code can be easily controlled with caution.

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 500)
p.start(66.7)
print("Go")
input('Press return to change:')
p.ChangeDutyCycle(75)
input('Press return to stop:')
p.stop()
print("stop")
GPIO.cleanup()

print("Welcome to the SLES Robotics Drone Project. The Flight Controller Script is underway. \nHave fun you rascals!")

