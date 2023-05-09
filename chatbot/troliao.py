import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
from gtts import gTTS
import time 
import playsound
import wikipedia

language = 'vi'
wikipedia.set_lang('vi')
friday=pyttsx3.init()
voices = friday.getProperty('voices')
# for voice in voices:
#     if voice.languages[1] == 'vi':
#         friday.setProperty('voice', voice.id)
#         break

friday.setProperty('voice', voices[1].id)


def speak(audio):
    
    print('Bot: ' + audio)
    friday.say(audio)
    friday.runAndWait()
   
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("Bây giờ là ")
    speak(Time)

def welcome():
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Chào buổi sáng")
        elif hour>=12 and hour<18:
            speak("Chào buổi chiều")
        elif hour>=18 and hour<24:
            speak("Chào buổi tối")
        speak("Tôi có thể giúp gì cho bạn") 


def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='vi-VN')
        print("Tôi: "+query)
    except sr.UnknownValueError:
        print('Xin lỗi, tôi không hiểu. Hãy nhập vào đây')
        query = str(input('Yêu cầu của bạn: '))
    return query

if __name__  =="__main__":
    welcome()

    while True:
        language='vi'
        query=command().lower()
        if "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        
        elif "youtube" in query:
            speak("Bạn muốn tôi tìm gì")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')

        elif "quit" in query:
            speak("Tôi is off. Goodbye boss")
            quit()

        elif 'time' in query:
            time()
            