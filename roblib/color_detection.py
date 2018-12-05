import paramiko
from scp import SCPClient
import os
import cv2
import numpy as np
import logging


class ColorDetection:
    HUE_COLORS = {
        359: 'red',
        0: 'red',
        245: 'blue',
        120: 'green',
        60: 'yellow'
    }

    USER_AMBER = 'nao'
    PASSWORD_AMBER = 'i1-p2e3p'
    HOST_AMBER = '192.168.1.101'

    USER_PORTER = 'nao'
    PASSWORD_PORTER = 'i2-p2e3p'
    HOST_PORTER = '192.168.1.102'

    TMP_IMG_LOCATION = '.tmp_image.jpg'

    '''
    define target square in image
    '''
    toprigth = [0.2, 0.5]
    bottomleft = [0.5, 0.8]


    def __init__(self, image_path, image_file):
        self.logger = logging.getLogger(__name__)

        self._image_path = image_path
        self._image_file = image_file

    def _createSSHClient(self, server, port, user, password):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port, user, password)
        return client

    '''
    Download image and setup local image path
    '''
    def _download_image(self, host):
        user = self.USER_AMBER
        password = self.PASSWORD_AMBER

        if self.HOST_PORTER == host:
            user = self.USER_PORTER
            password = self.PASSWORD_PORTER

        ssh = self._createSSHClient(host, 22, user, password)
        with SCPClient(ssh.get_transport()) as scp:
            scp.get(self._image_path + self._image_file)
            scp.close()

    def _detect_color(self):
        img = cv2.imread(self._image_file)
        org = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #boundary = ([188, 175, 156], [96, 81, 57])
        img = img[0:240,:]

        img_blur = cv2.GaussianBlur(img, (5, 5), 0)
        canny = cv2.Canny(img_blur,100,200)
        lower = np.array([60, 90, 100], dtype="uint8")
        upper = np.array([200, 200, 200], dtype="uint8")

        mask = cv2.inRange(img_blur, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)

        #img = img[240:360,280:320]
        cv2.imshow("image", np.hstack([img, output]))
        cv2.waitKey()
        cv2.imshow("image", canny)
        cv2.waitKey()

        height, width, c = img.shape
        toprigthpos = np.array([int(width * self.toprigth[0]), int(height * self.toprigth[1])])
        bottomleftpos = np.array([int(width * self.bottomleft[0]), int(height * self.bottomleft[1])])

        clip = org[toprigthpos[1]:bottomleftpos[1],toprigthpos[0]:bottomleftpos[0]]

        average = np.average(np.average(clip, axis=0), axis=0)
        avg_pixel = np.array([[average.astype(int)]])
        hsv = cv2.cvtColor(np.float32(avg_pixel), cv2.COLOR_RGB2HSV)

        self.logger.debug("detected HSV '" + str(hsv[0][0]) + "'")

        detected_value = hsv[0][0][0]

        return self.HUE_COLORS[min(self.HUE_COLORS, key=lambda x:abs(x-detected_value))]

    def get_color(self, host):
        self._download_image(host)
        color = self._detect_color()
        self.logger.info("color '" + str(color) + "' detected")
        os.remove(self._image_file)
        return color




