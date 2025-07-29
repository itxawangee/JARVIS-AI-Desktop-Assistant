try :
    import pyttsx3
except ModuleNotFoundError:
    import subprocess
    subprocess.run("pip install pyttsx3")
    import pyttsx3

def TTS(text):
    E = pyttsx3.init()#printing current voice rate
    E.setProperty('rate', 125) 
    V = E.getProperty('voices')
    E.setProperty('voice',V[1].id)
    E.say(text)
    E.runAndWait()
