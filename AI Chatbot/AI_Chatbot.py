import os
import openai
import speech_recognition as sr
import pyttsx3
import datetime

openai.api_key = os.environ.get("OPENAI_API_KEY")

def chatgpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-IN')
        print(f"User: {query}")
        return query
    except Exception as e:
        print(e)
        return ""

def get_text():
    return input("Enter your command >> ")

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.say(text)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, Aritt!")
    elif hour>=12 and hour<16:
        speak("Good AfterNoon, Aritt!")
    else:
        speak("Good Evening, Aritt!")
    speak("I am AR!. How may I help you?")

if __name__ == "__main__":
    # speak("Hello! How can I assist you?")
    WishMe()
    while True:
        print("\nChoose input method:")
        print("1. Voice")
        print("2. Text")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            user_input = get_audio().lower()
        elif choice == "2":
            user_input = get_text().lower()
        elif choice == "3":
            speak("Goodbye, See you soon!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
            continue

        if user_input in ["quit", "exit", "bye", "goodbye"]:
            speak("Goodbye, See you soon!")
            break

        elif user_input in ["who are you", "what are you", "introduce yourself"]:
            speak("I am AR, your personal assistant. I can help you with your queries.")
            continue
        
        elif user_input in ["what is the time", "time"]:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            continue
        
        elif user_input in ["what is the date", "date"]:
            strDate = datetime.datetime.now().strftime("%d-%m-%Y")
            speak(f"The date is {strDate}")
            continue
        
        elif user_input in ["what is your name", "your name"]:
            speak("I am AR, your personal assistant.")
            continue
        
        elif user_input in ["how are you", "how do you do"]:
            speak("I am good. Thank you for asking.")
            continue
        
        elif user_input in ["what can you do", "what are your capabilities"]:
            speak("I can assist you with your queries. You can ask me anything.")
            continue
        
        elif user_input in ["who created you", "who is your creator"]:
            speak("I was created by Aritta Sinha.")
            continue
        
        elif user_input in ["what is your purpose", "why were you created"]:
            speak("I was created to assist you with your queries.")
            continue

        elif user_input in ["youtube", "open youtube", "yt"]:
            speak("Opening Youtube")
            os.system("start brave https://www.youtube.com")
            continue

        elif user_input in ["whatsapp", "open whatsapp"]:
            speak("Opening Whatsapp")
            os.system("start whatsapp")
            continue

        elif user_input in ["spotify", "open spotify"]:
            speak("Opening Spotify")
            os.system("start spotify")
            continue

        elif user_input in ["google", "open google"]:
            speak("Opening Google")
            os.system("start brave https://www.google.com")
            continue

        elif user_input in ["instagram", "open instagram", "insta"]:
            speak("Opening Instagram")
            os.system("start brave https://www.instagram.com")
            continue

        elif user_input in ["moodle", "open moodle"]:
            speak("Opening Moodle")
            os.system("start brave https://learn.gitam.edu")
            continue

        elif user_input in ["glearn", "open glearn"]:
            speak("Opening G-learn")
            os.system("start brave https://login.gitam.edu")
            continue

        elif user_input in ["mail", "open mail"]:
            speak("Opening Mail")
            os.system("start brave https://mail.google.com/mail/u/1")
            continue
        
        response = chatgpt(user_input)
        speak(response)
