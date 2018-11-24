import os
import time
import qi
import functools

#Tracer can be started with the start() method and stopped with the stop() method
#it writes a *.csv file with all the data
#timestamp, accx, accy, accz, gyrox, gyroy, gyroz, wflpos, wfrpos, wbpos

_FILESTREAM = open("team10_room_guide.csv", "a")
_SEP = " , "

class Tracer():
    def __init__(self, session):
        self.session = session
        self.memory = session.ALMemory
        self.task = qi.PeriodicTask()

    def traceTask(self):
        timestamp = time.time()
        accx = self.memory.getData("Device/SubDeviceList/InertialSensorBase/AccelerometerX/Sensor/Value")
        accy = self.memory.getData("Device/SubDeviceList/InertialSensorBase/AccelerometerY/Sensor/Value")
        accz = self.memory.getData("Device/SubDeviceList/InertialSensorBase/AccelerometerZ/Sensor/Value")
        gyrox = self.memory.getData("Device/SubDeviceList/InertialSensorBase/GyroscopeX/Sensor/Value")
        gyroy = self.memory.getData("Device/SubDeviceList/InertialSensorBase/GyroscopeY/Sensor/Value")
        gyroz = self.memory.getData("Device/SubDeviceList/InertialSensorBase/GyroscopeZ/Sensor/Value")
        wflpos = 0 #self.memory.getData("Device/SubDeviceList/InertialSensorBase/WheelFL/Position/Sensor/Value")
        wfrpos = 0 #self.memory.getData("Device/SubDeviceList/InertialSensorBase/WheelFR/Position/Sensor/Value")
        wbpos = 0 #self.memory.getData("Device/SubDeviceList/InertialSensorBase/WheelB/Position/Sensor/Value")

        self._write(timestamp, accx, accy, accz, gyrox, gyroy, gyroz, wflpos, wfrpos, wbpos)

    def start(self):
        self.task.setCallback(self.traceTask)
        self.task.setUsPeriod(100000)
        self.task.start(True)
        qi.async(self.traceTask, delay=100000)

    def stop(self):
        self.task.stop()

    def _write(self, timestamp, accx, accy, accz, gyrox, gyroy, gyroz, wflpos, wfrpos, wbpos):
        txt = str(timestamp) + _SEP + str(accx) + _SEP + str(accy) + _SEP + str(accz)
        txt = txt + _SEP + str(gyrox) + _SEP + str(gyroy) + _SEP + str(gyroz)
        txt = txt + _SEP + str(wflpos) + _SEP + str(wfrpos) + _SEP + str(wbpos)
        _FILESTREAM.write(txt+os.linesep)
