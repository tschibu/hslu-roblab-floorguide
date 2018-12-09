'''
- Laser Operation Modes:
0: all lasers off
1: horizontal laser on
2: 2x vertical lasers on
3: horizontal + 2x vertical lasers on
4: shovel laser on
5: shovel + horizontal laser on
6: shovel + 2x vertical lasers on
7: shovel + horizontal + 2x vertical lasers on

- Laser Operation Actuators (to change Operation Mode):
Device/SubDeviceList/Platform/LaserSensor/Front/Reg/OperationMode/Actuator/Value
Device/SubDeviceList/Platform/LaserSensor/Right/Reg/OperationMode/Actuator/Value
Device/SubDeviceList/Platform/LaserSensor/Left/Reg/OperationMode/Actuator/Value

- Laser Operation Sensors (to read the Operation Mode):
Device/SubDeviceList/Platform/LaserSensor/Front/Reg/OperationMode/Sensor/Value
Device/SubDeviceList/Platform/LaserSensor/Right/Reg/OperationMode/Sensor/Value
Device/SubDeviceList/Platform/LaserSensor/Left/Reg/OperationMode/Sensor/Value
-----------------------------------------------------
'''

class SensorHandler():
    def __init__(self, session):
        self.memory = session.ALMemory
        self.motion = session.ALMotion
        self.dcm = session.DCM

    def read_operation_modes(self):
        print("Front: " + str(self.memory.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Reg/OperationMode/Sensor/Value")))
        print("Right: " + str(self.memory.getData("Device/SubDeviceList/Platform/LaserSensor/Right/Reg/OperationMode/Sensor/Value")))
        print("Left: " + str(self.memory.getData("Device/SubDeviceList/Platform/LaserSensor/Left/Reg/OperationMode/Sensor/Value")))

    def write_operation_modes(self, value):
        t = self.dcm.getTime(0)
        self.dcm.set(["Device/SubDeviceList/Platform/LaserSensor/Front/Reg/OperationMode/Actuator/Value", "Merge", [[0.0, t]]])
        self.dcm.set(["Device/SubDeviceList/Platform/LaserSensor/Right/Reg/OperationMode/Actuator/Value", "Merge", [[0.0, t]]])
        self.dcm.set(["Device/SubDeviceList/Platform/LaserSensor/Left/Reg/OperationMode/Actuator/Value", "Merge", [[0.0, t]]])
        self.motion.setExternalCollisionProtectionEnabled("All", False)
