import os
import threading
from playsound import playsound


class KAudio(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(KAudio, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.tapSound = "ui_tap.wav"
        self.confirmUpSound = "ui_confirm_up.wav"
        self.loadingSound = "ui_loading.wav"
        self.celebrationSound = "ui_celebration.wav"
        self.shutterSound = "ui_shutter.wav"

    def playSound(self, soundFile):
        print(f"{os.getcwd()}\\sounds\\{soundFile}")
        # threading.Thread(target=playsound, args=(f"{os.getcwd()}\\sounds\\"+soundFile,)).start()
        playsound(f"{os.getcwd()}\\sounds\\"+soundFile, False)

    def tap(self):
        self.playSound(self.tapSound)

    def confirm_up(self):
        self.playSound(self.confirmUpSound)

    def loading(self):
        self.playSound(self.loadingSound)

    def celebration(self):
        self.playSound(self.celebrationSound)

    def shutter(self):
        self.playSound(self.shutterSound)