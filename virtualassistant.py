import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
   engine.say(audio)
   #engine.say('My current speaking rate is ' + str(rate))
   engine.runAndWait()
   #engine.stop()


def wishme():
   hour=int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morning")
   elif hour>=12 and hour<18:
      speak("Good Afternoon")
   else:
      speak("Good Evening")
speak("Hello Urwashi! How may I help you?")
speak("what are you searching for?")

def acceptcommand():
   ''' it takes microphone input from user and give strind as output command'''
   # Initialize the recognizer 
   r = sr.Recognizer() 
     # use the microphone as source for input.
   with sr.Microphone() as source:
      print("listening.....")
      r.pause_threshold=1
      audio=r.listen(source)
   
   try:
      print("Recognizing......")
      query=r.recognize_google(audio,language='en-in')
      print(f"user said:{query}\n")#user query printed

   except Exception as e:
      print("Repeat again")
      return "None"
   return query
      
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('urwashi238srivastava@gmail.com', 'your-password')
    server.sendmail('urwashi238srivastava@gmail.com', to, content)
    server.close()


if __name__=='_main':
   
   wishme()
   #coding for wikipedia........................
   while True:
      query=take_command()
      if wikipedia in query:
         speak("searching wikipedia")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)
      #to open youtube in  browser......
      elif 'open youtube' in query:
         webbrowser.open("youtube.com")
      #to open google
      elif 'open google' in query:
         webbrowser.open("google.com")
      #to play music...............
      elif 'play music' in query:
         music_dir='D:\\pythonprogram'
         songs=os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))
      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")    
         speak(f"Sir, the time is {strTime}")

      elif 'open code' in query:
         codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

      elif 'email to urwashi' in query:
         try:
            speak("What should I say?")
            content = takeCommand()
            to = "urwashi238srivastava.com"    
            sendEmail(to, content)
            speak("Email has been sent!")
         except Exception as e:
            print(e)
            speak("Sorry my friend harry bhai. I am not able to send this email")  '''  
