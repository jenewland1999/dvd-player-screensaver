"""
# Imports

Imports modules needed for the program to function correctly.
These external modules are native to Python and allow for creating more advanced things that python doesn't allow by default.

"""
import turtle, time, random, os.path
from turtle import *

"""
# Pre Defined Options

Here are the hard-coded values for debug mode and toggling logging on and off.
These are added so that you can enable them for more information on the program while it runs.
In future, we could expand to using a seperate config file.

"""
debug = False
logEnabled = False

# Constants for Window
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SCREEN_NAME = "DVD Player"
SCREEN_TITLE = SCREEN_NAME + " (" + str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT) + ")"

# Constants for Log
"""
# Time and Date

I get the date and time in string format (Year Month Day/Hour Minute Second).
These are then used within the log as timestamps.

"""
getDate = time.strftime("%Y-%m-%d")
getTime = time.strftime("%H:%M:%S")
LOG_DIR = "./logs/"
LOG_NAME = LOG_DIR + getDate + ".log"
INFO = "[" + SCREEN_NAME + "/INFO]"
WARN = "[" + SCREEN_NAME + "/WARN]"
ERROR = "[" + SCREEN_NAME + "/ERROR]"
DEBUG = "[" + SCREEN_NAME + "/DEBUG]"

# Constants for Shape W/H
FG_WIDTH = 128
FG_HEIGHT = 128
FG_WIDTH_SIDE = FG_WIDTH/2
FG_HEIGHT_SIDE = FG_HEIGHT/2

# Foreground Pos Variables
foregroundX = 0
foregroundY = 0
foregroundDirX = 5
foregroundDirY = 5

# Colour Variables | Python is silly therefore rgb values are between 0-1
red = 0
green = 0
blue = 0

# Set screen window size
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 30, 30)
screen.title(SCREEN_TITLE)
screen.bgcolor((red, green, blue))

# Define object turtle as foreground then specify properties of the object (Object Ordinated Programming)
foreground = turtle.Turtle()
register_shape("assets/foreground.gif")
foreground.shape("assets/foreground.gif")
foreground.penup()

def createLog():
    'createLog will initialize the log file by creating a text document inside a log directory and then writing a title to the log file then closing the file -- we use log.close() because if we didn\'t we\'d end up with a memory leak which is bad'
    global time, date, INFO, WARN, ERROR, DEBUG, debug, config, LOG_NAME, LOG_DIR
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    log = open(LOG_NAME, "a")
    log.write("Log File: " + LOG_NAME)
    log.close()

def log(level, logMsg):
    'log(level, logMsg) (level=INFO/DEBUG/ERROR/WARN) (logMsg=String) allows you to create a log entry with a level parameter and a message paramater'
    global LOG_NAME
    getLogTime = "[" + time.strftime("%H:%M:%S") + "]"
    if logEnabled == True:        
        if os.path.isfile(LOG_NAME):
            log = open(LOG_NAME, "a")
            log.write("\n" + getLogTime + " " + level + ": " + logMsg)
            log.close()
        else:
            createLog()
            log = open(LOG_NAME, "a")
            log.write("\n" + getLogTime + " " + level + ": " + logMsg)
            log.close()
    return

def moveObject():
    'moveObject will set the initial foreground image position on the screen then sleeps for 0.01 second. After this it will begin moving the foreground image positive x and y'
    global foregroundX, foregroundY, foregroundDirX, foregroundDirY, screen
    foreground.setpos(foregroundX, foregroundY)
    time.sleep(0.01)

    foregroundX = foregroundX + foregroundDirX
    foregroundY = foregroundY + foregroundDirY

def changeColor():
    'changeColor will set red, green & blue to a random value between 0 and 1 using the random.uniform() function'
    global red, green, blue, screen
    red = random.uniform(0, 1)
    green = random.uniform(0, 1)
    blue = random.uniform(0, 1)
    screen.bgcolor((red, green, blue))
    if debug == True:
        log(INFO, "Changing Colour...")
        log(DEBUG, "Colour: " + str(round(red, 2)) + " " + str(round(green, 2)) + " " + str(round(blue, 2)))
    else:
        log(INFO, "Changing Colour...")

def changeForegroundXDir():
    'changeForegroundXDir will reverse the direction when it colides with the side of the screen. '
    global foregroundDirX
    foregroundDirX = foregroundDirX * -1
    if debug == True:
        log(INFO, "Changing Direction...")
        log(DEBUG, "Foreground X = " + str(foregroundX))
        log(DEBUG, "Foreground Y = " + str(foregroundY))
    else:
        log(INFO, "Changing Direction...")
        
def changeForegroundYDir():
    'changeForegroundYDir will reverse the direction when it colides with the side of the screen. '
    global foregroundDirY
    foregroundDirY = foregroundDirY * -1
    if debug == True:
        log(INFO, "Changing Direction...")
        log(DEBUG, "Foreground X = " + str(foregroundX))
        log(DEBUG, "Foreground Y = " + str(foregroundY))
    else:
        log(INFO, "Changing Direction...")

def borderCheck():
    'borderCheck checks whether the foreground image has collided with the side of the screen if so it then runs changeForegroundXDir/changeForegorundYDir and then changeColor'
    global foregroundX, foregroundY, foregroundDirX, foregroundDirY, screen
    # Right Side Border Detection
    if foregroundX > SCREEN_WIDTH/2 - FG_WIDTH_SIDE:
        changeForegroundXDir()
        changeColor()
    
    # Left Side Border Detection
    elif foregroundX < ((SCREEN_WIDTH/2 - FG_WIDTH_SIDE) *-1):
        changeForegroundXDir()
        changeColor()
        
    # Top Side Border Detection
    if foregroundY > SCREEN_HEIGHT/2 - FG_HEIGHT_SIDE:
        changeForegroundYDir()
        changeColor()
        
    # Bottom Side Border Detection
    elif foregroundY < ((SCREEN_HEIGHT/2 - FG_HEIGHT_SIDE) *-1):
        changeForegroundYDir()
        changeColor()

# Create Log
if logEnabled == True:
    createLog()

# Continuous Loop
while True:
    moveObject()
    borderCheck()
