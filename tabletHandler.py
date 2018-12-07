__TABLETSERVICE = None #Roboter tabletService, set by __init__
MapWebapp = "FloorGuide_Map"
RoomSelection = "FloorGuide_RoomSelection"

class TabletHandler():
    def __init__(self, session):
        self.tabletservice = session.session.service("ALTabletService")
        global __TABLETSERVICE
        __TABLETSERVICE = self.tabletservice

    @staticmethod
    def startApp(appName):
        __TABLETSERVICE.loadApplication(appName)
        __TABLETSERVICE.showWebview()

    @staticmethod
    def getMapApp():
        return MapWebapp

    @staticmethod
    def getRoomSelectionApp():
        return RoomSelection
