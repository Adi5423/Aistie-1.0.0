import speech_recognition as sr
import pyttsx3
from flask import Flask, render_template, request

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Create a Flask app instance
app = Flask(__name__)

# Set up Flask route for GUI
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def listen():
    audio = request.files['audio']
    text = r.recognize_google(audio)
    respond(text)
    return 'OK'

def record_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)
        return audio

def respond(voice_data):
    print("Responding...")
    if "wake up" in voice_data:
        wake_up()
    elif "hello" in voice_data:
        engine.say("Hello! How can I help you?")
        engine.runAndWait()
    else:
        engine.say("I didn't understand that. Try again!")
        engine.runAndWait()

def wake_up():
    print("Waking up...")
    respond("Hello! I'm awake.")

if __name__ == '__main__':
    app.run(debug=True)