import qi
import functools

class Tracer():
    def __init__(self, session):
        self.session = session
        self.memory = session.ALMemory
        self.task = qi.PeriodicTask()

    def traceTask(self):
        accx = self.memory.getData("Device/SubDeviceList/InertialSensorBase/AccelerometerX/Sensor/Value")
        accy = self.memory.getData("Device/SubDeviceList/InertialSensorBase/AccelerometerY/Sensor/Value")
        accz = self.memory.getData("Device/SubDeviceList/InertialSensorBase/AccelerometerZ/Sensor/Value")
        gyrox = self.memory.getData("Device/SubDeviceList/InertialSensorBase/GyroscopeX/Sensor/Value")
        gyroy = self.memory.getData("Device/SubDeviceList/InertialSensorBase/GyroscopeY/Sensor/Value")
        gyroz = self.memory.getData("Device/SubDeviceList/InertialSensorBase/GyroscopeZ/Sensor/Value")

        print("Accelometer -> X: " + str(accx) + ", Y: " + str(accy) + ", Z: " + str(accz))
        print("Gyrometer   -> X: " + str(gyrox) + ", Y: " + str(gyroy) + ", Z: " + str(gyroz))

    def start(self):
        self.task.setCallback(self.traceTask)
        self.task.setUsPeriod(100000)
        self.task.start(True)
        qi.async(self.traceTask, delay=100000)

    def stop(self):
        self.task.stop()
