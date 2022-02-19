import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 300
mic = sr.Microphone()


def recognize_speech_from_mic(r, mic):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            diary_file = open('diary.txt', 'a')
            diary_file.write(text)
            diary_file.close()
            return diary_file
        except Exception:
            return "Error"
    
def read_file(diary_file, chunk_size=5242880):
    with open(diary_file, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data