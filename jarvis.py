import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour >=0 and hour <12:
        speak("Good Afternnon!")
    else:
        speak("Good Evening!")
        
    speak("Hello i am Jarvis how can i help you?")

def takeCommand():
    '''It takes Microphone input from the user and returns string output'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nisargshah501@gmail.com','Pass')
    server.sendmail('nisargshah501@gmail.com',to,content)
    server.close()
    
if __name__ == "__main__":
    wishme()
    val = True
    query = takeCommand().lower()
        #Logic for executing task based on query
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=2)
        print(result)
        speak("According to wikipedia ")
        speak(result)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'open chrome' in query:
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(path)

    elif 'play music' in query:
        music_dir = "D:\\Entertainment\\Songs"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")
    
    elif 'open code' in query:
        path = "C:\\Users\\Nisarg Shah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
        
    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "************"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            print("There was a problem...")
            
    elif 'stop the program' in query:
        speak("Thank you, I hope to see you again!")
        # break