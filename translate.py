# Aileen Pongnon
# CogxPy Project
# November 15, 2019 -

import csv

# createStates
def detection():
    print("CreateState Detection isActive")
    # if( gas pedal )
    #     gasPedal()
    # elif( brake pedal )
    #     brakePedal()

def evasion():
    print("CreateState Evasion isActive")
    # if( turn left )
    #     gasPedal()
    # elif( turn right )
    #     brakePedal()

# create goals
def gasPedal():
    print("Goal: Press Gas Pedal\n"
    "> Look at road environment\n"
    "> Think of pressing the gas pedal\n"
    "> Recall using right foot to press the gas pedal\n"
    "> Verify gas was pressed by movement in the car\n")
    return

def brakePedal():
    print("Goal: Press Brake Pedal\n"
    "> Look at road environment\n"
    "> Think of pressing the brake pedal\n"
    "> Recall using right foot to press the brake pedal\n"
    "> Verify brake was pressed by movement in the car\n")

def turnLeft():
    print("Goal: Turn Left\n"
    "> Look at road environment\n"
    "> Think of turning left\n"
    "> Recall how to turn left\n"
    "> Verify the car turned left\n")

def turnRight():
        print("Goal: Turn Right\n"
        "> Look at road environment\n"
        "> Think of turning right\n"
        "> Recall how to turn right\n"
        "> Verify the car turned right\n")

# file operations
def viewFile(tasks):
    # open the file
    handle = open(tasks, "r")
    print("Successfully openend file " + tasks)
    # printContents(handle)
    decipher(handle)
    # closing the file
    handle.close()

# reading & printing the contents of the file
# def printContents(fileHandle):
#     contents = fileHandle.read()
#     print(contents)

# decipher elements in the file (all tasks)
def decipher(fileHandle):
    # read in contents from file into a string
    contents = fileHandle.readline()
    contents = contents.rstrip('\n')

    # place each string in a position in list
    taskList = list(contents.split(", "))
    # print(taskList)

    # traverse through list to redirect to appropriate fct
    for i in range(len(taskList)):
        if(taskList[i] == "gas"):
            gasPedal()
        elif(taskList[i] == "brake"):
            brakePedal()
        elif(taskList[i] == "left"):
            turnLeft()
        elif(taskList[i] == "right"):
            turnRight()

# retrieving the file from the user
tasksFile = input('Enter the filename: ')
viewFile(tasksFile)
