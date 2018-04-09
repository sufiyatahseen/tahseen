import speech_recognition as sr
r = sr.Recognizer()
with sr.microphone() as source:
    print("speak")
    audio = r.listen(source)

try:
    print("You said"+ r.recognize_google (audio))
except sr.UnknownvalueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}" .format(e)) 
