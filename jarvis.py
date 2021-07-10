import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Aftrnoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")
def takeCommand():
    #It takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")
        
        

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('write your mail ID','write your password')
    server.sendmail('write your mail ID',to,content)
    server.close()
if __name__ == '__main__':
    wishMe()
    while True : 
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            music_dir = 'F:\\jarvis\\fav_songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"mam, the time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codePath = "F:\\Keilversion4\\UV4\\Uv4.exe"
            os.startfile(codePath)

        elif 'open web whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        
        elif 'open gmail' in query:
            webbrowser.open("paste here link of gmail")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'latest news' in query:
            webbrowser.open("https://timesofindia.indiatimes.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/accounts/login//")

        elif 'email to sudha' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "Write here mail id for whom you want to send a mail" 
                sendEmail(to, content) 
                speak("Email has been sent!")
                print("Email has been sent!")
                

            except Exception as e:
                print(e)
                speak("Sorry... I am not able to send this email")


        






