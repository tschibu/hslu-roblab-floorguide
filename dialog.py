

class Dialog():
    def __init__(self, session):
        self.session = session
        self.dialog = session.ALDialog
        self.dialog.setLanguage("English")

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


