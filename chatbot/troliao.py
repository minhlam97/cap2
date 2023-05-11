import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
from gtts import gTTS
import time 
import playsound
import wikipedia

# wikipedia.set_lang('vi')
# language = 'vi'

bot=pyttsx3.init()
voices = bot.getProperty('voices')
# vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
bot.setProperty('voice', voices[1].id)
# friday.say("chào các bạn")
# friday.runAndWait()

def speak(audio):
    
    print('Bot: ' + audio)
    bot.say(audio)
    bot.runAndWait()
   
    
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
        query = c.recognize_google(audio,language='vi')
        print("Tôi: "+query)
    except sr.UnknownValueError:
        speak('Xin lỗi, tôi không hiểu. Hãy nhập vào đây')
        query = str(input('Yêu cầu của bạn: '))
    return query

if __name__  =="__main__":
    welcome()

    while True:
        language='vi'
        query=command().lower()
        if "google" in query:
            speak("Bạn muốn tôi tìm gì")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là {search} trên google')
        
        elif "youtube" in query:
            speak("Bạn muốn tôi tìm gì")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là {search} trên youtube')

        elif query:
            wikipedia.set_lang("vi")
            que= wikipedia.summary(query, sentences=1)
            speak(que)

        # elif 'mấy giờ' in query:
        #     time()
            
        elif "tạm biệt" in query:
            speak("Tạm biệt bạn, Hẹn gặp lại")
            quit()