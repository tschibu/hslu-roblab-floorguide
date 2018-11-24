class Tablet():

    def __init__(self):
        self.__init__()

    def onLoad(self):
        pass

    def onUnload(self):
        pass

    def _getTabletService(self):
        tabletService = None
        try:
            tabletService = self.session().service("ALTabletService")
        except Exception as e:
            self.logger.error(e)
        return tabletService

    def onInput_onStart(self):
        # We create TabletService here in order to avoid
        # problems with connections and disconnections of the tablet during the life of the application
        tabletService = self._getTabletService()
        if tabletService:
            tabletService.showWebview("http://www.google.ch")
        else:
            self.logger.warning("ALTabletService not found.")
        self.onStopped()
