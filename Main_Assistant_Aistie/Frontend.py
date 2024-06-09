# from Aistie import Main
# from Aistie import Aistie
import datetime
import os
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import requests
import time
from selenium import webdriver
import linecache
from gesture import gesture
import pywhatkit
import pyperclip
from groq import Groq
from hand_control_draw import drawing
import tkinter as tk 
from tkinter import StringVar, messagebox

# Initialize the engine
engine = pyttsx3.init()
# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def clear_output(output_text):
    output_text.delete("1.0", tk.END)
    
client = Groq()
    
def execute(query):
                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {
                                "role": "user",
                                "content": query
                            },
                        ],
                        temperature=1,
                        max_tokens=1024,
                        top_p=1,
                        stream=True,
                        stop=None,
                    )

                    response = ''
                    for chunk in completion:
                        response += chunk.choices[0].delta.content or ""

                    return response


def saver(reminds):
                    file = open(path, "a")
                    unsuccesfull = False
                    try:
                        for key, query in reminds.items():
                            if key is not None:
                                file.write(str(key) + " - " + query + "\n")
                    except Exception as e:
                        print(f"Error: {e}. Reminders: {reminds}")
                        unsuccesfull = True
                    file.close()
                    return unsuccesfull


def remind(key, query):
                    while True:
                        reminds = {None:None}
                        try:
                            if key == "None" or query == "None":
                                speak("Sorry sir can't set that. Please say something else!")
                                return
                            else:
                                reminds.update({key:query})
                                print(f"Reminders before saver: {reminds}")
                                unsuccesfull = saver(reminds)
                                print(f"Reminders after saver: {reminds}")
                                speak("I will remind you about that")
                                # Clear the reminds dictionary except for None:None
                                reminds = {k: v for k, v in reminds.items() if k is None and v is None}
                                break
                                return
                        except Exception as e:
                            speak("Sorry sir, i faced a failure doing that. Please try again.")
                            print(e)
                            reminds = {None:None}
                            return

path = "D:\\Py_Start\\Programming\\Projects\\Laptop_Assistant\\Main_Assistant_Aistie\\reminder\\reminders.txt"

def reader(key):
                    with open(path, "r") as file:
                        lines = file.readlines()
                        if key != 0:
                            for i in range(len(lines) - 1,-1,-1):
                                line = lines[i]
                                index = line.find("-")
                                if key in (line[index+1:].strip()):   #checks if the key mathces what the user asked to get the reminder
                                    output = line[:index].strip() + line[index:].strip()  # Remove all the things before the key 
                                    speak(output)  # Speak the result
                                    return output
                                else:
                                    speak("Sorry Sir , no reminders found for that key.")
                                    return
                        else:
                            # speak("If you don't have key value. I am reading the last reminder save if i found any!!")
                            if len(lines) == 0:
                                hour = int(datetime.datetime.now().hour)
                                if hour >= 0 and hour < 12:
                                    wish ="Morning!"
                                elif hour >= 12 and hour < 18:
                                    wish = "Noon!"
                                else:
                                    wish = "Evening!"

                                speak("That's Cool sir looks like I don't have any reminders for you there. Enjoy the " + wish)
                            else:
                                line = lines[-1]  # Use the last line of the list
                                index = line.find("-")
                                output = line[index+1:].strip()  # Remove all the things before "-" and strip any leading/trailing whitespace
                                speak(output)  # Speak the result
                                return output

capasity = "I can open websites, search for things on the internet, tell the time , greet you , play music , can set reminders for you in the system , can read the left reminders, trying to open applications also ."

# Initialize the engine
engine = pyttsx3.init()
# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
                engine.say(text)
                engine.runAndWait()
                


def wishMe():
                    hour = int(datetime.datetime.now().hour)
                    if hour >= 0 and hour < 12:
                        speak("   Good morning!")
                    elif hour >= 12 and hour < 18:
                        speak("  Good afternoon!")
                    else:
                        speak("   Good evening!")
                    speak("   I am you personal assistant Sir. My name is Aistie. Please tell me how may I assist you today!!")

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
                        print("  Say that again please...")
                        return "None"


                    if 'p s t' in query or "PST" in query :
                        query = query.lower()
                        search_query = query.replace("pst" , "+")
                        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
                        speak("Opening youtube for the song sir")

                    # elif "the time" in query:
                    #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    #     speak(f"Sir, the time is {strTime}")

                    return query

def takeCommandHindi():
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print('Listening')
                        r.pause_threshold = 0.7
                        audio = r.listen(source)
                        try:
                            print("Recognizing")
                            Query = r.recognize_google(audio, language='hi-In')
                            print("The query is:", Query)
                        except Exception as e:
                            print(e)
                            print("Say that again please...")
                            return "None"
                        return Query



def get_weather(city):
                    api_key = "066d7dce815c25f9814b08e0090399a0"
                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    complete_url = f"{base_url}appid={api_key}&q={city}"
                    response = requests.get(complete_url)
                    data = response.json()
                    if data["cod"] != "404":
                        main_data = data["main"]
                        weather_data = data["weather"][0]
                        temperature = main_data["temp"] - 273.15
                        pressure = main_data["pressure"]
                        humidity = main_data["humidity"]
                        description = weather_data["description"]
                        return f"The current temperature in {city} is {temperature:.2f} degrees Celsius. The pressure is {pressure} hPa and the humidity is {humidity}%. The weather is currently {description}."
                    else:
                        return "City not found."

ar = True
def Aistie():
                    # global is_awake
                    # is_awake = True
                    # if ar == True :
                    #     wishMe()
                    while True:
                        ar = False
                        query = takeCommand()
                        query=query.lower()
                        # datetime.datetime.now().strftime("%I:%M %p") == '00:00'
                        # speak("   Happy BIrthday Sir Wish you the best wish ")
                        if "wikipedia" in query:
                            speak("  Searching Wikipedia...")
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=2)
                            speak("  According to Wikipedia")
                            print(results)
                            speak(results)

                        #  Convert 24-hour time to AM/PM time
                        elif "the time" in query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f"Sir, the time is {strTime}")

                        elif "open youtube" in query:
                            webbrowser.open("youtube.com")
                            speak("   Opening Youtube")

                        elif 'wait' in query or 'sleep' in query:
                            speak("Okay sir, I'll wait for your command.")
                            is_awake = False

                        elif 'who are you' in query:
                            speak(" I am your personal Assistant Sir. My name is Aistie. i also have the control on your system to assist you sir.")

                        elif "open google" in query:
                            webbrowser.open("google.com")
                            speak("   Opening Google")    

                        elif 'open'in query and 'gesture'in query:
                            speak('Sure , sir now i have some amazing options in gesture control , hope you seeing the list on screen')    
                            speak("Sir , Press Yes for Gesture Drawing Control , and , No for Gesture Mouse Control")
                            ask = messagebox.askquestion("Gesture Controller" , "YES for Drawing \n NO for Mouse")
                            # engine.runAndWait()
                            if "yes" in ask:
                                code = True
                                speak("Here's your Gesture Drawing Controller Sir. Enjoy")
                                drawing(code)
                                continue
                            else:
                                code = True
                                speak("Here's your Gesture Mouse Controller Sir. Enjoy")
                                gesture(code)
                                continue
                            
                        elif 'play ' in query:
                            # speak("Sure sir. Just tell me the name of the Song. with the keyword p s t to search on youtube. ")
                            search_query = query.replace("play" , "" )
                            pywhatkit.playonyt(search_query)
                            speak("Sure sir. Playing " + search_query)
                            break
                        
                        
                        
                        elif 'how are you' in query or 'how r u' in query or 'how you doing' in query or ' how u doing' in query:
                            speak('I am an AI, and I don\'t have feelings. Although i feel great to be developed and breath by the lines of code by python. ')

                        # elif 'what time is it' in query:
                        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        #     speak(f"The time is {strTime}")


                        elif 'close the browser' in query:
                            browser = webbrowser.get(webbrowser.WindowsDefault)
                            browser.close()


                        elif 'what can you do' in query or 'what can u do' in query:
                            speak (f"For now not much but. {capasity} How may i further assist you sir?")

                        elif 'search' in query:
                            speak("Sure sir on youtube. or google?")
                            search_query = query.replace("search", "")
                            webbrowser.open_new_tab(f"https://www.google.com/search?q={search_query}")
                            speak(f"Here is the search results for {search_query}")

                        elif 'open' in query:
                            app_name = query.replace("open", "")
                            speak(f"Opening {app_name}")
                            os.system(f"open {app_name}")

                        elif 'great work assistant' in query : 
                            speak ("Thankyou sir your words help me improve\n What further to help you?")

                        elif 'greet me' in query or 'wish me' in query:
                            wishMe()

                        elif 'close' in query:
                            app_name = query.replace("close", "")
                            speak(f"Closing {app_name}")
                            os.system(f"killall {app_name}")

                        elif 'set' in query and "reminder" in query:
                            speak('Sure sir tell me the reminder you want to save')
                            reminder = takeCommand()
                            if "use the last copied one " in reminder:
                                reminder = pyperclip.paste()
                                speak("Okay sir i got that. Would you also like to set any key for that to easily find that later?")
                                check_query=takeCommand()  # Move this line up here
                                if "sure" in check_query or "yes" in check_query:
                                    speak("Okay sir tell me the key for your reminder please!")
                                    key = takeCommand()
                                    time.sleep(2.5)
                                    remind(key,pyperclip.paste())
                                    speak("I have set that sir what further to do?")
                                else:
                                    time.sleep(2.5)
                                    remind(0,pyperclip.paste())
                                    speak("I have set that sir what further to do?")
                            else:        
                                speak("Okay sir i got that. Would you also like to set any key for that to easily find that later?")
                                check_query=takeCommand()  # Move this line up here
                                if "sure" in check_query or "yes" in check_query:
                                    speak("Okay sir tell me the key for your reminder please!")
                                    key = takeCommand()
                                    time.sleep(2.5)
                                    remind(key,reminder)
                                    speak("I have set that sir what further to do?")
                                else:
                                    time.sleep(2.5)
                                    remind(0,reminder)
                                    speak ("I have set that sir what further to do?")

                        elif 'show' in query and "reminder" in query:
                            speak("Sure sir. Do you have the key for the reminder. ")
                            check_query = takeCommand()
                            if 'yes' in check_query or "i do" in check_query or 'i have' in check_query:
                                speak("Go ahead with the key sir?")
                                key = takeCommand()
                                time.sleep(3.5)
                                reader(key)
                            else:
                                speak("No problem sir. Just lee mee check if i have any latest reminder for you or not!!")
                                time.sleep(3.5)
                                reader(0)


                        elif "weather" in query:
                            city = query.split("weather in")[-1].strip()
                            response = get_weather(city)
                            speak(response)

                        elif 'thank you' in query:
                            speak('My pleasure sir, feel free to ask me anything!')

                        elif 'bye' in query or 'exit' in query or 'quit' in query:
                            speak('Goodbye! Have a great day.')
                            # check0 = False
                            break


                        else:
                            groq_response = execute(query)
                            speak(groq_response)
                            print(groq_response)

                        # if check0 == True :
                        #     continue
                        # else:
                        #     break
                        
                            '''
                            speak("Would you like me to search that on the internet sir?")
                            takeCommand()
                            if 'yes' in query or 'go ahead' in query or 'sure' in query:
                                # search_query = query.replace("search", "")
                                webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
                                speak("Found this result sir!!")
                            elif 'exit' in query:
                                speak('Goodbye! Have a great day.')
                                break 
                            else:
                                speak("Sorry sir, I am unable to help you with that. Tell me what more to assist with?")
                            ''' 

    
    

def frontend():
    window = tk.Tk()
    window.title("Aistie - Your AI Assistant")
    window.geometry("1520x950")  # Adjust the size as needed

    # Add a title label
    title_label = tk.Label(window, text="Aistie AI Assistant", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)

    # Create the input/output area
    input_frame = tk.Frame(window)
    input_frame.pack()

    # Input text box
    input_text = tk.Text(input_frame, height=5, width=50)
    input_text.pack(side="left", padx=10)

        # Output text box
    output_text = tk.Text(input_frame, height=8, width=50, state="disabled")  # Start as disabled
    output_text.pack(side="right", padx=10)

    # Buttons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    # Speak button
    # speak_button = tk.Button(button_frame, text="Speak", command=lambda: speak(input_text.get("1.0", "end-1c")))
    speak_button = tk.Button(button_frame, text="Speak", command=lambda: speak(input_text.get("1.0", "end-1c")))
    speak_button.pack(side="left", padx=5)

    # talk button
    talk_button = tk.Button(button_frame, text="Talk", command=lambda: Aistie())
    talk_button.pack(side="left", padx=5)

    # Clear button
    clear_button = tk.Button(button_frame, text="Clear", command=lambda: clear_output(output_text))
    clear_button.pack(side="left", padx=5)

    # ... Add other features (reminder, weather, etc.) as frames ...

    window.mainloop()

if __name__ == "__main__":
    frontend()