import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


def recognize_speech_from_mic(r, mic):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio, True, language = 'en')
        diary_file = open('diary.txt', 'a')
        diary_file.write(text)
        diary_file.close()
        return diary_file
    
def read_file(diary_file, chunk_size=5242880):
    with open(diary_file, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data