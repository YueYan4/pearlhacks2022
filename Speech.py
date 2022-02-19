from distutils.command.check import SilentReporter
import speech_recognition as sr
import time

r = sr.Recognizer()
r.energy_threshold = 300
mic = sr.Microphone()
    
#function to get mic input and write it to a txt file
def recognize_speech_from_mic(r, mic):
    print("Start talking")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            diary_file = open('diary.txt', 'a')
            diary_file.write(text)
            diary_file.close()
            print(text)
            return diary_file
        except Exception:
            print("Sorry, I didn't get that")
   
#function to read the txt file 
def read_file(diary_file):
    with open(diary_file, 'rb') as _file:
        while True:
            data = _file.read()
            if not data:
                break
            yield data
  
  
time.sleep(1)          
while 1:          
    recognize_speech_from_mic(r, mic)