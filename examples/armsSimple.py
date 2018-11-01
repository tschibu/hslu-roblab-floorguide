from pynaoqi_mate import Robot
from configuration import PepperConfiguration
import qi
import math
import time
import almath
import motion

minShoulderPitch = -119.5
maxShoulderPitch = 119.5
minShoulderAngle = 0.5
maxShoulderAngle = 89.5
minElbowYaw = -119.5
maxElbowYaw = 119.5
minElbowRoll = 0.5
maxElbowRoll = 89.5


virtualRobotConfig = PepperConfiguration("Porter")
myRobot = Robot(virtualRobotConfig)

myRobot.ALRobotPosture.goToPosture("StandInit", 1)
time.sleep(2)


myRobot.ALMotion.changeAngles("LShoulderRoll", math.radians(maxShoulderAngle), 1)
myRobot.ALMotion.changeAngles("RShoulderRoll", math.radians(-maxShoulderAngle), 1)
time.sleep(2)
myRobot.ALMotion.changeAngles("LShoulderRoll", math.radians(minShoulderAngle), 1)
myRobot.ALMotion.changeAngles("RShoulderRoll", math.radians(-minShoulderAngle), 1)
time.sleep(2)


myRobot.ALMotion.changeAngles("LShoulderPitch", math.radians(maxShoulderPitch), 1)
myRobot.ALMotion.changeAngles("RShoulderPitch", math.radians(maxShoulderPitch), 1)
time.sleep(2)
myRobot.ALMotion.changeAngles("LShoulderPitch", math.radians(minShoulderPitch), 1)
myRobot.ALMotion.changeAngles("RShoulderPitch", math.radians(minShoulderPitch), 1)
time.sleep(2)


myRobot.ALMotion.changeAngles("LElbowYaw", math.radians(maxElbowYaw), 1)
myRobot.ALMotion.changeAngles("RElbowYaw", math.radians(-maxElbowYaw), 1)
time.sleep(2)
myRobot.ALMotion.changeAngles("LElbowYaw", math.radians(minElbowYaw), 1)
myRobot.ALMotion.changeAngles("RElbowYaw", math.radians(-minElbowYaw), 1)
time.sleep(2)


myRobot.ALMotion.changeAngles("LElbowRoll", math.radians(maxElbowRoll), 1)
myRobot.ALMotion.changeAngles("RElbowRoll", math.radians(-maxElbowRoll), 1)
time.sleep(2)
myRobot.ALMotion.changeAngles("LElbowRoll", math.radians(minElbowRoll), 1)
myRobot.ALMotion.changeAngles("RElbowRoll", math.radians(-minElbowRoll), 1)
time.sleep(2)


myRobot.ALMotion.closeHand("RHand")
myRobot.ALMotion.closeHand("LHand")
time.sleep(2)


myRobot.ALMotion.openHand("RHand")
myRobot.ALMotion.openHand("LHand")
time.sleep(2)

myRobot.ALRobotPosture.goToPosture("StandInit", 1)