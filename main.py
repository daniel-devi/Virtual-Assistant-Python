# Libraries
import subprocess  # To Run Os Commands
import wolframalpha
import pyttsx3  # A python Text to Speech Library
# import tkinter
import json
import speech_recognition as sr  # A Speech Recognition Library with Python
import datetime
import wikipedia  # Python Library to get  Wikipedia Result
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from ecapture import ecapture as ec
# EMAIL LOGIN
from Password import EMAIL_ADDRESS, EMAIL_PASSWORD
# Main Program

# Some Customization

print("DEVA YOUR VIRTUAL ASSISTANT .............")

name_choice = str(input("What do you want to name Your Virtual Assistant: "))

if len(name_choice.strip()) <= 0:
    name_choice = "DEVA"


# Initializing Voice of Virtual Assistant

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
pyttsx3.init(driverName='sapi5') 

# Defining Some Special Command

# Speak Command to Make the Virtual Assistant Talk


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# A Greeting
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    myName = f"{name_choice} 1 point 0"
    speak("I am your Assistant")
    speak(myName)


# Give the User a Name and Call Him
def username():
    speak("What should i call you ")
    userName = takeCommand()
    if userName == "None":
        speak("Didn't get that, Try Again")
        userName = takeCommand()

    speak("Welcome Mister")
    speak(userName)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", userName.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, ")


# Take Voice Command
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

    except Exception as error:
        print(error)
        print("Unable to Recognize your voice.")
        speak("Sorry Didn't get that")
        return "None"

    return query

# Send Email


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, to, content)
    server.close()


############## All Command ###################

if __name__ == '__main__':
    def clear(): return os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            results = wikipedia.summary(
                query.replace("wikipedia", ""), sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            try:
                if "what is" in query or "who is" in query:
                    client = wolframalpha.Client("XGJ7U5-TTQHJJ6E48")
                    res = client.query(query)
            except Exception as e:
                print("An error occurred:", e)
                speak("An Error Happened")
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                speak("NO Result")
                print("No results")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            
        elif 'open instagram' in query:
            speak("Here you go to INSTAGRAM\n")
            webbrowser.open("instagram.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            speak("Here you go to Github .Happy coding")
            webbrowser.open("github.com")

        elif 'the time' in query:
            strTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
            speak(f"Sir, the time is {strTime}")

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"  # Email
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send it to?")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
            speak("I have Done that")

        elif "change name" in query:
            speak("What would you like to call me")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Daniel.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "XGJ7U5-TTQHJJ6E48"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open("www.google.com/search?q=", query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Daniel. further It's a secret")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r""
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Daniel")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Daniel ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif 'open minecraft' in query:
            appli = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\TLauncher\TLauncher.lnk"
            os.startfile(appli)

        elif 'open vscode' in query:
            appli = r"C:\Users\devon\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
            os.startfile(appli)

        elif "don't listen" in query or "stop listening" in query:
            speak(f"for how much time you want to stop, please only say a number {name_choice} from listening commands")
            a = takeCommand()
            number = a
            time.sleep(number)
            print(number)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google/ maps / place/" + location + "")

        ###### WINDOWS COMMAND ##########

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shut down system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown /s')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        ##### Random Command #######

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "496fc6f9ea9848027c008feb96f80711"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(
                    current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak(
                "I don't have any mutal feelings am just a Assistant Created by Daniel ")

        # elif "" in query:
            # Command go here
            # For adding more commands
