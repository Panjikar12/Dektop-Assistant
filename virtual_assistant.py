import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import random
import pywhatkit as kt

engine = pyttsx3.init('sapi5')#sapi5 is a voice recognization techonology provided by microsoft
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #Wishing the user based on the current time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Raman")
    elif hour>=12 and hour<20:
        speak("Good Afternoon Raman")
    elif hour>=20:
        speak("Good Night Raman")
    speak("I am rachel and i am your personal desktop assistent How may i help you")

def takecommand():
    #it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listining what u want........")
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio)
    except Exception as e:
        #print(e)
        print("say that again pls......")
        return "None"
    return query
if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
    # logic for executing task based on queries
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif 'send email' in query:
            import mail
            mail.py
        elif 'open security camera' in query:
            speak('opening the security camera')
            import movement_detection
            movement_detection.py
        elif 'open youtube' in query:
            speak("opening youtube for u ")
            webbrowser.open("https://www.youtube.com/")
        elif 'close youtube' in query:
            speak("closing youtube for you ")
            os.system("taskkill /f /im chrome.exe")
        elif 'college' in query:
            speak("your present college is bms institute of technology and management here is some information about your college")
            webbrowser.open("https://bmsit.ac.in/")
        elif 'open linkedin' in query:
            speak("accessing your linkdin account ")
            webbrowser.open("https://www.linkedin.com/in/raman-panjikar-5634a8204")
        elif 'open whatsapp' in query:
            speak("accessing your whatsapp account ")
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open email' in query:
            speak("accessing your emails")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'close email' in query:
            speak("closing email for you")
            os.system("taskkill /f /im chrome.exe")
        elif 'open hotstar' in query:
            speak("opening hotstar for you")
            webbrowser.open("https://www.hotstar.com/in")
        elif 'close hotstar' in query:
            speak("closing hotstar for you")
            os.system("taskkill /f /im chrome.exe")
        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir,The time is {strTime}")
        elif 'play music' in query:
            speak("opening your fav music playlist ")
            my_music = 'E:\\Mohit Chauhan Best Of Me [2013-MP3-VBR-320Kbps] - [DJMaza]'
            songs = os.listdir(my_music)
            n = random.randint(0, 30)
            os.startfile(os.path.join(my_music, songs[n]))
        elif 'close music' in query:
            speak("closing your music file ")
            os.system("taskkill /f /im Groove.exe")
        elif 'iot' in query:
            project = 'C:\\Users\\Raman\\OneDrive\\Desktop\\iot_project'
            files = os.listdir(project)
            os.startfile(project)
        elif 'open telegram' in query:
            loc = 'C:\\Users\\Raman\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'
            os.startfile(loc)
        elif 'close telegram' in query:
            speak("closing your documents file sir")
            os.system("taskkill /f /im Telegram.exe")
        elif "vm" in query:
            loc1 = 'C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe'
            os.startfile(loc1)
        elif 'movie' in query:
            speak("your fav marvel movies")
            loc3 = 'D:\\MARVEL'
            os.startfile(loc3)
        elif '3rd sem' in query:
            speak("study materials of your third semester")
            loc4 = 'C:\\Users\\Raman\\OneDrive\\Desktop\\3rd sem MCA'
            os.startfile(loc4)
        elif 'my folder' in query:
            speak("accessing your documents sir")
            loc5 = 'C:\\mine'
            os.startfile(loc5)
        elif 'close my folder' in query:
            speak("closing your documents file sir")
            os.system("taskkill /f /im mine")
        elif 'open word' in query:
            speak("opening microsoft word for u sir")
            loc7 = 'C:Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(loc7)
        elif 'close word' in query:
            speak("closing microsoft word for you")
            os.system("taskkill /f /im WINWORD.EXE")
        elif 'open excel' in query:
            speak("opening microsoft excel for u")
            loc8 = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
            os.startfile(loc8)
        elif 'close excel' in query:
            speak("closing microsoft excel for you")
            os.system("taskkill /f /im EXCEL.EXE")
        elif 'open powerpoint' in query:
            speak("opening microsoft powerpoint for u")
            loc9 = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(loc9)
        elif 'close powerpoint' in query:
            speak("closing microsoft powerpoint for you")
            os.system("taskkill /f /im POWERPOINT.EXE")
        elif ' open google chrome' in query:
            speak("opening google chrome for u sir")
            loc9 = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(loc9)
        elif 'close google chrome' in query:
            speak("closing google chrome for you")
            os.system("taskkill /f /im chrome.exe")
        elif 'universe' in query:
            speak("presenting to you some of the best view of the universe")
            webbrowser.open("https://unsplash.com/s/photos/universe")
        elif 'thank' in query:
            speak("always at your service sir")
        elif 'search in google' in query:
            speak("information about your query")
            query = query.replace("search in google","")
            kt.search(query)
        elif 'good night' in query:
            speak("good night sir")
            speak("i am also going for some nap")
            exit()
        elif 'shutdown' in query:
            speak("shutting down your system sir")
            os.system("shutdown /s /t 1")
