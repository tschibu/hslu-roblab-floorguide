from pynaoqi_mate import Robot
from configuration import PepperConfiguration
import qi

#virtualRobotConfig = PepperConfiguration("Porter")
#myRobot = Robot(virtualRobotConfig)


class TakePictureExample():
    def __init__(self):
        self.config = PepperConfiguration("Porter")
        robot = Robot(self.config)
        self.camera = robot.ALPhotoCapture

    def takePicture(self):
        remote_folder_path ="/home/nao/recordings/cameras/"
        file_name = "myPicture.jpg"
        self.camera.takePicture(remote_folder_path, file_name)

app = TakePictureExample()
app.takePicture()