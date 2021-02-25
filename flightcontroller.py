# This is the main script file that will regulate the raspberry pi's communication with input and output to flight controllers. Feel free to edit this code and push to main branch.
# For big changes to the code, push to master branch and generate a pull request into the main branch. This way, code can be easily controlled with caution.

print("Welcome to the SLES Robotics Drone Project. The Flight Controller Script is underway. \nHave fun you rascals \n")

# Module Imports Here

import RPi.GPIO as GPIO

# Provides an option for testing certain parts of the code

test_info_str = ["1)  Run a basic LED light through GPIO 13. Tests if GPIO is functioning properly.\n"]

def testFunctionOne():
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

def moveOnConfirm():
    skipTest = input("\nMoving past the test phase. Confirm (y/n)?\n")
    if skipTest == "y" or skipTest == "Y" or skipTest == "Yes" or skipTest == "yes":
       print("\n") 
    else:
        testCode()

def testCode():
    try:
        for information in test_info_str:
            print(information + "\n")
        typeTest = input("\n\nPress Control-C to exit the testing phase and skip to code execution. Press a number above and enter for a specific test scenario. Simply press enter to run all tests.\n\n")
        if (typeTest == "1"):
            testFunctionOne()
            moveOnConfirm()
        elif (typeTest == ""):
            testFunctionOne()
            moveOnConfirm()
        else:
            print("Enter a valid option\n")
            testCode()
    except: 
        moveOnConfirm()


# Creating the Function that will actually run the drone

def runDrone():
    print("Entering drone flight mode.")

# Function Ordering and Flow Control

testCode()
runDrone()
