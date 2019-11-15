# Aileen Pongnon
# CogxPy Project
# November 15, 2019 -

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
        print("Goal: Turn Left\n"
        "> Look at road environment\n"
        "> Think of turning right\n"
        "> Recall how to turn right\n"
        "> Verify the car turned right\n")

# read in file name
# decipher elements in the file (all tasks)
# put those tasks into a conclusvive array

gasPedal()
brakePedal()
turnLeft()
turnRight()
