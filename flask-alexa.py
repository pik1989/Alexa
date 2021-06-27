from flask import Flask,render_template,redirect,request
import warnings
warnings.filterwarnings('ignore')


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import sys


listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)




import os

app = Flask("__name__")



app.config["IMAGE_UPLOADS"] = "static/img/"



def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
    
    
def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('alexa', '')
            if 'alexa' in command:
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing....' + song)
        print("Playing....")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        
        engine_talk('Current Time is' + time)
    elif 'joke' in command:
        get_j = pyjokes.get_joke()
        print(get_j)
        engine_talk(get_j)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_talk(info)
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk("I didn't hear you properly")
        print("I didn't hear you properly")


@app.route('/')
def hello():
    return render_template("alexa.html")




@app.route("/home")
def home():
    return redirect('/')


@app.route('/submit',methods=['POST'])
def submit():
    
    run_alexa()
    
    
    return render_template("alexa.html")
        
    
    
    
    
    
    
if __name__ =="__main__":

    app.run()
    
if __name__ =="__main__":

    app.run()