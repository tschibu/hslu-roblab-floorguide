from pynaoqi_mate import Robot
from configuration import PepperConfiguration
import qi
import time


class LandMarkDetectionExample():
    def __init__(self):
        self.config = PepperConfiguration("Amber")
        robot = Robot(self.config)
        self.landMarkDetection = robot.ALLandMarkDetection
        self.memory = robot.ALMemory

        self.camera = robot.ALPhotoCapture
        self.tts = robot.ALTextToSpeech
        self.tts.setLanguage("English")
        self.audio = robot.ALAudioPlayer

    def takePicture(self):
        remote_folder_path = "/home/nao/recordings/cameras/"
        file_name = "myPicture.jpg"
        self.tts.say("say cheese!")
        qi.async(self.audio.playFile, "/home/nao/recordings/mp3/camera_shutter.mp3")
        time.sleep(3)
        self.camera.takePicture(remote_folder_path, file_name)

    def detectLandMark(self):
        self.tts.say("Starting Landmark Detection")
        memValue = "LandmarkDetected"
        self.landMarkDetection.subscribe("Test_Landmark", 500, 0.0)
        for i in range(0, 20):
            time.sleep(0.5)
            val = (self.memory).getData(memValue)
            print ""
            print "\*****"
            print ""

        # Check whether we got a valid output: a list with two fields.
        if (val and isinstance(val, list) and len(val) >= 2):
            # We detected landmarks !
            # For each mark, we can read its shape info and ID.
            # First Field = TimeStamp.
            timeStamp = val[0]
            # Second Field = array of Mark_Info's.
            markInfoArray = val[1]

            try:
                # Browse the markInfoArray to get info on each detected mark.
                for markInfo in markInfoArray:
                    # First Field = Shape info.
                    markShapeInfo = markInfo[0]
                    # Second Field = Extra info (i.e., mark ID).
                    markExtraInfo = markInfo[1]
                    # Print Mark information.
                    print "mark  ID: %d" % (markExtraInfo[0])
                    print "  alpha %.3f - beta %.3f" % (markShapeInfo[1], markShapeInfo[2])
                    print "  width %.3f - height %.3f" % (markShapeInfo[3], markShapeInfo[4])
                    print "  heading %.3f" % (markShapeInfo[5])
            except Exception, e:
                print "Landmarks detected, but it seems getData is invalid. ALValue ="
                print val
                print "Error msg %s" % (str(e))
        else:
            print "Error with getData. ALValue = %s" % (str(val))

        self.tts.say("Stopping Landmark Detection")
        self.landMarkDetection.unsubscribe("Test_Landmark")


    def talk(self):
        guide_dialog = self.dialog.loadTopic('/data/home/nao/dialogs/guide_dialog.top')
        self.dialog.activateTopic(guide_dialog)
        self.dialog.subscribe('my_dialog_example', 1000, 0)

        try:
            raw_input("\nSpeak to the robot. Press Enter when finished:")
        finally:
            # stopping the dialog engine
            self.dialog.unsubscribe('my_dialog_example')

            # Deactivating all topics
            self.dialog.deactivateTopic(guide_dialog)

            # now that the dialog engine is stopped and there are no more activated topics,
            # we can unload all topics and free the associated memory
            self.dialog.unloadTopic(guide_dialog)


pepper = LandMarkDetectionExample()
pepper.detectLandMark()
