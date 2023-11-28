from __future__ import print_function
import warnings
from googletrans import Translator
import pyttsx3
import speech_recognition as sr
import os
import streamlit as st
from gtts import gTTS
import playsound
import datetime
import calendar
import random
import webbrowser
import winshell
import ctypes
import subprocess
import pyjokes
import smtplib
import wikipedia
import pickle
import os.path
from twilio.rest import Client
import json
import requests
import time
import subprocess

# import sleep
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from selenium import webdriver
# from time import sleep
import wolframalpha

trans = Translator()
warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty(voices, voices[1].id)


# Required functios -->
#
def talk(audio):
    engine.say(audio)
    engine.runAndWait()


talk("Welcome boss !")


#
def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Luna could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data


# rec_audio()


#
def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)

    os.remove(audio)


#
def call(text):
    action_call = "luna"
    text = text.lower()
    if action_call in text:
        return True

    return False


#
def translate(sentence, destination):
    dest = destination[0:2].lower()
    ans = trans.translate(sentence, dest=dest)
    return ans


#
def detectt(sentence):
    return trans.detect(sentence)


#
def translated_res_voice(text, lang):
    print(text)
    tts = gTTS(text=text, lang=lang)
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)


#
def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return (
        "Today is "
        + week_now
        + ", "
        + months[month_now - 1]
        + " the "
        + ordinals[day_now - 1]
        + "."
    )


# With the help of Google API, feature below can be implemented

# def google_calendar():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)

#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 './cred.json', SCOPES)
#             creds = flow.run_local_server(port=0)

#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('calendar', 'v3', credentials=creds)

#     return service


#
# def calendar_events(num, service):
#     talk(f'Hey there! Good Day. Hope you are doing fine. These are the events to do today')
#     # Call the Calendar API
#     now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#     print(f'Getting the upcoming {num} events')
#     events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=num, singleEvents=True,
#                                           orderBy='startTime').execute()
#     events = events_result.get('items', [])

#     if not events:
#         talk('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         events_today = (event['summary'])
#         start_time = str(start.split("T")[1].split("-")[0])  # get the hour the event starts
#         if int(start_time.split(":")[0]) < 12:  # if the event is in the morning
#             start_time = start_time + "am"
#         else:
#             start_time = str(int(start_time.split(":")[0]) - 12)  # convert 24 hour time to regular
#             start_time = start_time + "pm"
#         talk(f'{events_today} at {start_time}')


# try:
#     service = google_calendar()
#     calendar_events(10, service)
# except:
#     talk("Could not connect to the local wifi network. Please try again later.")
#     exit()


#
# def send_email(to, content):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.ehlo()
#     server.starttls()

#     # Enable low security in gmail
#     server.login("email", "pass")
#     server.sendmail("email", to, content)
#     server.close()


#
def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello"]

    response = ["howdy", "whats good", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""


#
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


# All possible operations performed by Luna-->
#
while True:
    try:
        text = rec_audio()
        text = text.lower()
        speak = ""

        if call(text):
            speak = speak + say_hello(text)

            if (
                "don't listen" in text
                or "do not listen" in text
                or "stop listening" in text
            ):
                talk("for how many seconds would you prefer me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + " seconds completed, you can ask now..."

            elif "quit" in text or "exit" in text:
                exit()

            elif "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = (
                    speak
                    + " "
                    + "It is "
                    + str(hour)
                    + ":"
                    + minute
                    + " "
                    + meridiem
                    + " ."
                )

            elif "who is" in text or "tell me about" in text:
                if "tell me about" in text:
                    text = text[18:]
                elif "who is" in text:
                    text = text[12:]

                wiki = wikipedia.summary(text, sentences=2)
                speak = speak + " " + wiki

            elif "who are you" in text or "define yourself" in text:
                speak = (
                    speak
                    + "Hello, I am an Assistant, Luna. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera"
                )

            elif "made you" in text or "created you" in text:
                speak = speak + "I was created by Deon Cardoza"

            elif "your name" in text:
                speak = speak + "My name is Luna"

            elif "who am I" in text:
                speak = speak + "You must probably be a human"

            elif "why do you exist" in text or "why did you come to this word" in text:
                speak = speak + "It is a secret"

            elif "how are you" in text:
                speak = speak + "I am awesome, Thank you"
                speak = speak + "\nHow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that your fine"

            elif "on youtube" in text:
                text = text[4:]
                text = text[: len(text) - 10]
                # ind = text.lower().split().index("youtube")
                search = text.split()
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" + "+".join(search)
                )
                speak = speak + "Opening " + str(search) + " on youtube"

            elif "in youtube" in text:
                text = text[4:]
                text = text[: len(text) - 10]
                # ind = text.lower().split().index("youtube")
                search = text.split()
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" + "+".join(search)
                )
                speak = speak + "Opening " + str(search) + " on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1 :]
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1 :]
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1 :]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

            elif "translate" in text or "meaning of" in text:
                talk("What would you like me to translate?")
                string = str(rec_audio())
                talk("In which language do i need to translate?")
                dest = str(rec_audio())
                ans = translate(string, dest)
                translated_res_voice(ans.text, ans.dest)

            elif "joke" in text:
                speak = speak + pyjokes.get_joke()
            elif "open" in text.lower():
                if "edge" in text.lower():
                    speak = speak + "Opening Microsoft Edge"
                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                    )

                # just pass correct location of folders

                # elif "word" in text.lower():
                #     speak = speak + "Opening Microsoft Word"
                #     os.startfile(r"")

                # elif "excel" in text.lower():
                #     speak = speak + "Opening Microsoft Excel"
                #     os.startfile(r"C:\...\EXCEL.EXE")

                # elif "vs code" in text.lower():
                #     speak = speak + "Opening Visual Studio Code"
                #     os.startfile(r"C:\...\Code.exe")

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "Opening Google\n"
                    webbrowser.open("https://google.com/")

                elif "stackoverflow" in text.lower():
                    speak = speak + "Opening StackOverFlow"
                    webbrowser.open("https://stackoverflow.com/")

                else:
                    speak = speak + "Application not available"

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"

            elif "shutdown" in text:
                talk(
                    "Your all current running processes will be terminated, do you still want to shutdown..."
                )
                check = rec_audio()
                if "yes" in check.lower():
                    talk("As you say...")
                    os.system("shutdown /s /t 1")

            elif "make a note" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)

                speak = speak + "I have made a note of that."

            elif "calculate" in text:
                # https://www.google.co.in/search?q=calculate+
                talk("What should I calculate ?")
                query = rec_audio()
                url = "https://www.google.co.in/search?q=calculate"+"".join(query)
                speak = speak + "This is the result"
                webbrowser.open(url)

            # Easy-peasy feature, only pass correct location of folders
            #
            # elif "change background" in text or "change wallpaper" in text:
            #     img = r""
            #     list_img = os.listdir(img)
            #     imgChoice = random.choice(list_img)
            #     randomImg = os.path.join(img, imgChoice)
            #     ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
            #     speak = speak + "Background changed successfully"

            # elif "play music" in text or "play song" in text:
            #     talk("Here you go with music")
            #     music_dir = r"C:\Users\Public\Bhojpuri"
            #     songs = os.listdir(music_dir)
            #     d = random.choice(songs)
            #     random = os.path.join(music_dir, d)
            #     playsound.playsound(random)

            # This feature can be used locally eaisly but is not advisable also, Google will discontinue it after 2024 fall.

            # elif "email to computer" in text or "gmail to computer" in text:
            #     try:
            #         talk("What should I say?")
            #         content = rec_audio()
            #         to = "Receiver email address"
            #         send_email(to, content)
            #         speak = speak + "Email has been sent !"
            #     except Exception as e:
            #         print(e)
            #         talk("I am not able to send this email")

            # elif "mail" in text or "email" in text or "gmail" in text:
            #     try:
            #         talk("What should I say?")
            #         content = rec_audio()
            #         talk("whom should i send")
            #         to = input("Enter To Address: ")
            #         send_email(to, content)
            #         speak = speak + "Email has been sent !"
            #     except Exception as e:
            #         print(e)
            #         speak = speak + "I am not able to send this email"

            # This feature can be used locally by Twilio API

            # elif "send message" in text:
            #     account_sid = "ACe2effc9f7e462bd04979b625958d4c44"
            #     auth_token = "5355013ee06dd0dded2ec5d62d873c76"
            #     client = Client(account_sid, auth_token)

            #     talk("What should i send")
            #     message = client.messages.create(
            #         body=rec_audio(), from_="+12242053708", to="+917339777697"
            #     )

            #     print(message.sid)
            #     speak = speak + "Message sent successfully"

            # Features below can be used locally by Walfram API

            # elif "calculate" in text or "send a message" in text:
            #     app_id = "H6PTH5-AAYGWHYPX9"
            #     client = wolframalpha.Client(app_id)
            #     ind = text.lower().split().index("calculate")
            #     text = text.split()[ind + 1 :]
            #     res = client.query(" ".join(text))
            #     answer = next(res.results).text
            #     speak = speak + "The answer is " + answer

            # elif "what is" in text or "who is" in text:
            #     app_id = "H6PTH5-AAYGWHYPX9"
            #     client = wolframalpha.Client(app_id)
            #     ind = text.lower().split().index("is")
            #     text = text.split()[ind + 1 :]
            #     res = client.query(" ".join(text))
            #     answer = next(res.results).text
            #     speak = speak + answer

            # https://www.google.co.in/search?q=meaning+of+yes+in+hindi

            response(speak)
    except:
        talk("I don't know that")
