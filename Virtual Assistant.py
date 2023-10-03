import tkinter as tk
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        return "None"

def execute_command():
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        webbrowser.open("https://www.google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("https://www.stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'D:\\songs\\bhakti'  # Change this to your music directory
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\ankit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Change this to your VS Code path
        os.startfile(codePath)

    elif 'email to Ankit' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "tiwarianku2001@gmail.com"  # Change this to the recipient's email address
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry, I am not able to send this email")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')  # Replace with your email and password
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

# Create the macOS-inspired GUI window
root = tk.Tk()
root.title("Virtual Assistant")

# Customize the GUI window to have macOS-like styling
root.geometry("200x100")
root.configure(bg="#ececec")  # Background color

# Create and configure a button with macOS styling
button = ttk.Button(root, text="Start", command=execute_command)
button.pack(padx=20, pady=20)
button.configure(style='mac.TButton')

# Style configuration for macOS-like widgets
style = ttk.Style()
style.configure('mac.TButton', foreground='black', font=('Helvetica', 14, 'bold'), background="#0077ff", borderwidth=0)
style.map('mac.TButton', foreground=[('active', 'white')])

# Start the GUI main loop
root.mainloop()
