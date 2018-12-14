import sys
import time
from logger import Logger
from speech import Speech
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from sensorHandler import SensorHandler

roboterName = "Amber"
initPosition = "StandZero" # StandInit, StandZero, Crouch

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    sensorhandler = SensorHandler(robot)

    #sensorhandler.write_operation_modes(3.0)
    sensorhandler.read_operation_modes()

if __name__ == "__main__":
    _main()
