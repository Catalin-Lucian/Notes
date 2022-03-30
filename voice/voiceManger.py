import threading

import speech_recognition as sr
import pyttsx3
from PyQt5.QtCore import QObject, pyqtSignal


class VoiceManager(QObject):
    sNewNote = pyqtSignal()
    sInsertTitle = pyqtSignal(str)
    sInsertContent = pyqtSignal(str)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VoiceManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(VoiceManager, self).__init__()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()

    def speechToText(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.energy_threshold = 1000
            self.recognizer.operation_timeout = 2
            audio = self.recognizer.listen(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        try:
            response["transcription"] = self.recognizer.recognize_google(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["success"] = False
            response["error"] = "Unable to recognize speech"

        return response

    def textToSpeech(self, myText):
        self.engine.say(myText)
        self.engine.runAndWait()

    def start(self):
        action = 'new command'
        print(action)
        quitFlag = True
        while quitFlag:
            text = self.speechToText()
            print(f"----new command----  state:{action}")
            if not text["success"] and text["error"] == "API unavailable":
                print("ERROR: {}\nclose program".format(text["error"]))
                break
            while not text["success"]:
                print("I didn't catch that. What did you say?\n")
                text = self.speechToText()
            if text["transcription"].lower() == "exit":
                quitFlag = False
            print(text["transcription"].lower())

            if action == 'new command':
                self.textToSpeech(text["transcription"].lower())
                if "new note" in text["transcription"].lower():
                    self.sNewNote.emit()
                    action = 'insert'
                if "insert" in text["transcription"].lower():
                    action = 'insert'

            elif action == 'insert':
                if "stop" in text["transcription"].lower():
                    action = "new command"
                elif 'title ' in text["transcription"].lower():
                    self.sInsertTitle.emit(text["transcription"].lower().replace('title ', ''))
                elif 'content' in text["transcription"].lower():
                    action = 'content'
            elif action == 'content':
                if "stop" in text["transcription"].lower():
                    action = "new command"
                else:
                    self.sInsertContent.emit(text["transcription"].lower())


