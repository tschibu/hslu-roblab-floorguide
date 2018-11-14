from pynaoqi_mate import Robot
from configuration import PepperConfiguration
import qi

virtualRobotConfig = PepperConfiguration("Porter")
myRobot = Robot(virtualRobotConfig)


# Hands
# open
myRobot.ALMotion.openHand("RHand")
myRobot.ALMotion.openHand("LHand")

# close
myRobot.ALMotion.closeHand("RHand")
myRobot.ALMotion.closeHand("LHand")

