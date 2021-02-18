#Importing Modules
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#Setting up engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#fuction for making engine audio based

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function for Wishing good morning, afternoon and evening
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Reeuzaki, How may i help you")

def takeCommand():
    #it takes microphone input and return strings based output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

#main
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
    # Logic for executing tasks based on query
        
        #Sites
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
           webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

        elif 'open udemy' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://udemy.com")

        elif 'open stack overflow' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://stackoverflow.com")


        #Ide(s) and text editors
        elif 'open code' in query:
            codePath = "C:\\Users\\aditya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open charm' in query:
            charmPath = "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.2\\bin\\pycharm64.exe"
            os.startfile(charmPath)

        elif 'open sublime' in query:
            sublimePath = "C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(sublimePath)

        

        #Fun concepts
        elif 'thanks' in query:
            speak('Welcome')

        elif 'tell me a joke' in query:
            speak('What’s the difference between a police officer and a bullet? When a bullet kills someone else, you know it’s been fired')

        elif 'tell me another joke' in query:
            speak('I was about to make a sodium joke. but nah')