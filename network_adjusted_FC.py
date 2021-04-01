# This is the main script file that will regulate the raspberry pi's communication with input and output to flight controllers. Feel free to edit this code and push to main branch.
# For big changes to the code, push to master branch and generate a pull request into the main branch. This way, code can be easily controlled with caution.

print("Welcome to the SLES Robotics Drone Project. The Flight Controller Script is underway. \nHave fun you rascals \n")

# Module Imports Here

import RPi.GPIO as GPIO
import keyboard
import time\
import os

# Defines and sets up GPIO channels

base_value = 55

# Provides an option for testing certain parts of the code

test_info_str = ["1)  Run a basic LED light through GPIO 13. Tests if GPIO is functioning properly.\n", "2)  Tests to ensure that the keyboard module is installed and working properly."]

def testFunctionOne():
    print("Running GPIO output test \n\n")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.OUT)
    p = GPIO.PWM(13, 500)
    p.start(10)
    print("Go")
    input('Press return to change:')
    p.ChangeDutyCycle(80)
    input('Press return to stop:')
    p.stop()
    print("stopping")
    GPIO.cleanup()

def testFunctionTwo():
    print("Running keyboard module test\n\n")
    print("Pressing A key should output a stream of lols. Press q to end keyboard test.")
    while True:
        if keyboard.is_pressed("a"):
            time.sleep(.1)
            print("lol")
        elif keyboard.is_pressed("q"):
            break
        else:
            continue

def moveOnConfirm():
    skipTest = input("\nMoving past the test phase. Confirm (y/n)?\n")
    if skipTest == "y" or skipTest == "Y" or skipTest == "Yes" or skipTest == "yes":
        runDrone()
    elif skipTest == "n" or skipTest == "No" or skipTest == "No" or skipTest == "no":
        testCode()
    else:
        moveOnConfirm()

def testCode():
    try:
        for information in test_info_str:
            print(information + "\n")
        typeTest = input("\n\nPress Control-C to exit the testing phase and skip to code execution. Press a number above and enter for a specific test scenario. Simply press enter to run all tests.\n\n")
        if (typeTest == "1"):
            testFunctionOne()
            moveOnConfirm()
        elif (typeTest == "2"):
            testFunctionTwo()
            moveOnConfirm()
        elif (typeTest == ""):
            testFunctionOne()
            testFunctionTwo()
            moveOnConfirm()
        else:
            print("Enter a valid option\n")
            testCode()
    except: 
        moveOnConfirm()


# Creating the Function that will actually run the drone

def runDrone():
    print("Entering drone flight mode.")
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
    throttle.ChangeDutyCycle(45)
    arm = GPIO.PWM(16, 500)
    arm.start(90)
    time.sleep(2)
    while True:
        received_char = os.system('nc -lN -p 9000').read().decode('utf-8')
        if received_char == 'w':
            throttle.ChangeDutyCycle(95)
            print('w')
            time.sleep(.1)
        elif received_char == 's':
            throttle.ChangeDutyCycle(65)
            print('s')
            time.sleep(.1)
        elif received_char == 'p':
            print('stopping')
            break
        else:
            throttle.ChangeDutyCycle(55)
    for channel in channels:
        channel.stop()
    arm.stop()
    GPIO.cleanup()

# Function Ordering and Flow Control (runDrone referenced from moveOnConfirm() inside of testCode())

testCode()