import sys
sys.path.append("..")
import time
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration

roboterName = "Amber"
initPosition = "StandZero"

def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    tabletService = robot.session.service("ALTabletService")
    tabletService.loadApplication("floorguide_web")
    tabletService.showWebview()

if __name__ == "__main__":
    _main()