import smtplib
import speech_recognition as sr
import pyttsx3 as ps
import webbrowser 
import wikipedia
import os
import random


emails = ['razibravo76@gmail.com','jamiembroideryart@gmail.com','ahmedgulam83@gmail.com']
#smtp server setup....
EMAIL_ADD = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
def senmail(to,content):
    with smtplib.SMTP('smtp.gmail.com',587) as ser:
            ser.ehlo()
            ser.starttls()
            ser.ehlo()
            ser.login(EMAIL_ADD,EMAIL_PASS)
            ser.sendmail(EMAIL_ADD,to,content)
            ser.close()


#speech recognition setup......
engine = ps.init('sapi5')
v = engine.getProperty('voices')
rt = engine.getProperty('rate')
engine.setProperty('rate',rt-50)
engine.setProperty('voice',v[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("how may i help you")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something: ")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio,language='en-in')
            print(f"you said: {query}\n")

        except:
            print("sorry could not regognize your voice")
            return"none"
        return query
            
if __name__ == "__main__":
    f = True
    while f:
        query = command()
        speak(query)
        if 'how are you' in query:
            speak("i am good and you")
            
        elif 'what is your name' in query:
            speak("i am jarvis")
            
        elif 'Wikipedia' in query:
            speak('Searching wikipedia please wait')
            query = query.replace("Wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            
        elif 'open Google' in  query:
            webbrowser.open("google.com")
            
        elif 'open YouTube' in  query:
            webbrowser.open("youtube.com")
            
        elif 'open Gmail' in  query:
            webbrowser.open("gmail.com")
            
        elif 'open Paint' in  query:
            soft_dir ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\mspaint.exe"
            os.startfile(soft_dir)
             
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            rf = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[rf]))
            
        elif 'open my SQL' in query:
            soft_dir = "C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe"
            os.startfile(soft_dir)

        elif 'open WhatsApp' in query:
            soft_dir = "C:\\Users\\198\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(soft_dir)
       
        elif 'send mail' in query:
            try:
                speak("what should i send")
                content=command()
                speak("message has been stored   whom should i send")
                print("available emails are: ")
                for i in range(len(emails)):
                    print(i,emails[i])
                speak("select mail index number")
                em = command()
                if em == 0 or em == 'zero':
                    to = emails[0] 
                    senmail(to,content)
                    speak("email has been sent!")
                elif em == 1 or em == 'one':
                    to =emails[1]
                    senmail(to,content)
                    speak("email has been sent!")
                elif em == 2 or em == 'two' or em == 'Tu':
                    to =emails[2]
                    senmail(to,content)
                    speak("email has been sent!")
                else:
                    speak("no email found")
            except:
                print("sorry email cant be send")
        elif 'exit' in  query:
            f = False            
