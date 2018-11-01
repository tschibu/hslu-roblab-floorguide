from pynaoqi_mate import Robot
from configuration import PepperConfiguration
import paramiko
import qi

class TakePictureExample():
    def __init__(self):
        self.config = PepperConfiguration("Porter")
        robot = Robot(self.config)
        self.camera = robot.ALPhotoCapture

    def takePicture(self):
        remote_folder_path ="/home/nao/recordings/cameras/"
        file_name = "myPictureRemo.jpg"
        self.camera.takePicture(remote_folder_path, file_name)

class PepperFileTransfer():
    def __init__ (self, config):
        self.config = config
    
    def transferFileFromPepperToLocalhost(self, remote_path, localpath):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.config.Ip, username=self.config.Username,
        password=self.config.Password)
        sftp = ssh.open_sftp()
        sftp.get(remote_path, local_path)
        sftp.remove(remote_path)
        sftp.close()
        ssh.close()


local_path = "/Users/tluscre1/Documents/Studium.Local/ROBLAB/files"
app = TakePictureExample()
app.takePicture()
fileTransfer = PepperFileTransfer(self.config)
fileTransfer.transferFileFromPepperToLocalhost((remote_folder_path+file_name,local_path+file_name))