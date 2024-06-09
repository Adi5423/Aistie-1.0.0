import speech_recognition as sr
from groq import Groq
import pyttsx3
# Initialize the engine
engine = pyttsx3.init()

# Groq Service 
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

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
            print("Say that again, sir")
            return "None"
        return Query

ab = True
# Call the function
while (ab):
    query =takeCommandHindi()
    groq_response = execute(query)
    speak(groq_response)
    print(groq_response)