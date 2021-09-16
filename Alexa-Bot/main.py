import speech_recognition as sr
import pyttsx3
import pywhatkit as pwk
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

# change rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# change voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# function for talking
def talk(text):
        engine.say(text)
        engine.runAndWait()

# intro speech
talk('Hello there i am you alexa')
talk('What can i do for you ?')

# function for checking the keyword from the user 
def takeCommand():
    try:
        with sr.Microphone() as source:
            
            print('Listening...')
            
            # set the listening to recognize speech
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            # check if the keyword is spoken
            if 'alexa' in command:    
                command = command.replace('alexa', '')
    except:
        pass
    
    return command

# main function
def runAlexa():
    command = takeCommand();
    if "play" in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        print('Playing...')
        pwk.playonyt(song)
    elif 'tell' in command and 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search' in command:
        person = command.replace('search', '')
        pwk.search(person)
    elif 'info about'in command:
        person = command.replace('info about', '')
        info = wikipedia.summary(person, sentences=2)
        talk(info)
    elif 'exit' in command:
        exit()
        
# runners
while 1:
    runAlexa()
