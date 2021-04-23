# This is the main script file that will regulate the raspberry pi's communication with input and output to flight controllers. Feel free to edit this code and push to main branch.
# For big changes to the code, push to master branch and generate a pull request into the main branch. This way, code can be easily controlled with caution.

print("Welcome to the SLES Robotics Drone Project. The Flight Controller Script is underway. \nHave fun you rascals \n")

# Module Imports Here

import time
import RPi.GPIO as GPIO
import os

# Defines and sets up GPIO channels

base_value = 55

# Provides an option for testing certain parts of the code

test_info_str = ["1)  Run a basic LED light through GPIO 13. Tests if GPIO is functioning properly.\n", "2)  Tests to ensure that the keyboard module is installed and working properly.\n", "3) Tests to make sure motor comes on by altering throttle; press space to stop.\n", "4) Test to make sure the process of shutting down processes on port 9000 is effective."]

def testFunctionOne():
    print("Running GPIO output test \n\n")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.OUT)
    p = GPIO.PWM(13, 500)
    p.start(10)
    print("Go")
    input('Press anything to change:')
    p.ChangeDutyCycle(80)
    input('Press anything to stop:')
    p.stop()
    print("stopping")
    GPIO.cleanup()

def testFunctionTwo():
    print("Running keyboard module test\n\n")
    print("Pressing A key should output a stream of lols. Press q to end keyboard test.")
    while True:
        letter_pressed = input().replace("\n", "").replace(" ","")[0]
        if letter_pressed=="a":
            time.sleep(.1)
            print("lol")
        elif letter_pressed == "q":
            break
        else:
            continue

def testFunctionThree():
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
    print("Press s to stop")
    while True:
        cont_var = input().replace("\n", "").replace(" ","")[0]
        if cont_var == "s":
            arm.stop()
            for channel in channels:
                channel.stop()
            GPIO.cleanup()
            break
        continue 

def testFunctionFour():
    print("Starting multiple listening programs on port 9002 to test shutdown program.")
    for i in range(10):
        os.popen("nc -lk 9002")
    print(os.popen("fuser 9002/tcp").read() + "Press a key to cancel the processes.")
    input()
    for pid in os.popen("fuser 9002/tcp").read().replace("  "," ").split(" "):
        if pid:
            os.popen("kill " + pid)
    print("\nProcesses now open on 9002:\n"+os.popen("fuser 9002/tcp").read())


def moveOnConfirm():
    skipTest = input("\nMoving past the test phase. Confirm (y/n)?\n").replace("\n", "").replace(" ","")[0]
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
        typeTest = input("\n\nPress x to exit the testing phase and skip to code execution. Press a number above and enter for a specific test scenario. Simply press a to run all tests.\n\n").replace("\n", "").replace(" ","")[0]
        if (typeTest == "1"):
            testFunctionOne()
            moveOnConfirm()
        elif (typeTest == "2"):
            testFunctionTwo()
            moveOnConfirm()
        elif (typeTest == "3"):
            testFunctionThree()
            moveOnConfirm()
        elif (typeTest == "4"):
            testFunctionFour()
            moveOnConfirm()
        elif (typeTest == "a"):
            testFunctionOne()
            testFunctionTwo()
            testFunctionThree()
            testFunctionFour()
            moveOnConfirm()
        elif (typeTest == "x"):
            moveOnConfirm()
        else:
            print("Enter a valid option\n")
            testCode()
    except:
        print("Script shutting down (Hopefully you did this on purpose)")


# Creating the Function that will actually run the drone

def runDrone():
    print("Entering drone flight mode.")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    pitch = GPIO.PWM(18, 500)
    roll = GPIO.PWM(13, 500)
    yaw = GPIO.PWM(19, 500)
    throttle = GPIO.PWM(12, 500)
    arm = GPIO.PWM(16, 500)
    horizon = GPIO.PWM(17, 500)
    channels = [pitch,roll,yaw,throttle]
    arm.start(90)
    throttle.start(49)
    pitch.start(75)
    roll.start(75)
    yaw.start(95)
    horizon.start(90)
    time.sleep(4)
    for channel in channels:
        channel.ChangeDutyCycle(75)
    while True:
        key_pressed = input().replace("\n", "").replace(" ","")[0]
        if key_pressed == 'w':
            throttle.ChangeDutyCycle(95)
            time.sleep(.1)
        elif key_pressed == "s":
            throttle.ChangeDutyCycle(65)
            time.sleep(.1)
        elif key_pressed == "p":
            break
        elif key_pressed == "r":
            throttle.ChangeDutyCycle(55)
        else:
            throttle.ChangeDutyCycle(55)
    for channel in channels:
        channel.stop()
    arm.stop()
    horizon.stop()
    GPIO.cleanup()

# Function Ordering and Flow Control (runDrone referenced from moveOnConfirm() inside of testCode())

os.popen("nc -l 9003 | sudo python3 /home/pi/Desktop/SLES-Drone/listen_stop.py")
testCode()