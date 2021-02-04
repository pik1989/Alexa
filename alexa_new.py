# -*- coding: utf-8 -*-


import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
