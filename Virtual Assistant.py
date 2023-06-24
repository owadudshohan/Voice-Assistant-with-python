import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
from email.message import EmailMessage
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("I am your assistant. What can I do for you?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
    
        print("Say that again please...")  
        return "None"
    return query

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jehansarker6@gmail.com', 'jehansarker')
    email = EmailMessage()
    email['From'] = 'jehansarker6@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    "you": "jehansarker6@gmail.com",
    "mostak": "mostakmohosin1@gmail.com",
    "pavel": "jamiul002@gmail.com",
    "shehab": "sh.shihab.ss@gmail.com"
}

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'send an email' in query:
            try:
                speak('To Whom you want to send email')
                name = takeCommand()
                receiver = email_list[name]
                print(receiver)
                speak('What is the subject of your email?')
                subject = takeCommand()
                speak('Tell me the text in your email')
                message = takeCommand()
                send_email(receiver, subject, message)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,I am not able to send this email")  

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")

        elif 'tata'or'goodbye'or'bye'or'exit' in query:
                speak('Goodbye, Thank you for using me. See you again')
                break