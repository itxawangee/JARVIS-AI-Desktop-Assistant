from Engine.STT import STT
from Engine.TTS import TTS
from Brain.Brain import get_answer
import webbrowser
try :
    import pywhatkit as kt
except ModuleNotFoundError:
    import subprocess
    subprocess.run('pip install pywhatkit')
    import pywhatkit as kt
TTS("Allow me to introduce myself I am Jarvis of virtual artificial intelligence and I am here to assist you how may I help you, Sir")
TTS("Select the options you want to set the mode for your Jarvis press one for the input control press two for the speech to text function")

x = int(input())
if x == 1 :
    while True:
        text = input()
        if "jarvis" in text.lower():
            text = text.replace("jarvis","")
            text = text.replace("who is ","")
            text = text.replace("what is ","")
            TTS(get_answer(text))

        if "search in youtube" in text:
            text = text.replace("jarvis","")
            text = text.replace("search in youtube","")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")

        if "search in google" in text:
            text = text.replace("jarvis","")
            text = text.replace("search in google","")
            TTS("Searching about your requests sir")
            webbrowser.open(f"https://www.google.com/search?q={text}")
            TTS(f"You can see the search result about {text} in your screen")
        
        if "music on youtube" in text:
            text = text.replace("music on youtube","")
            TTS(f"playing your music {text}")
            text = text.replace('play',"")
            TTS(f'enjoy sir')
            kt.playonyt(text)
            


if x == 2:
    while True:
        text = str(STT()).lower()

        if "jarvis" in text:
            text = text.replace("jarvis","")
            text = text.replace("who is ","")
            text = text.replace("what is ","")
            TTS(get_answer(text))

        if "search in youtube" in text:
            text = text.replace("jarvis","")
            text = text.replace("search in youtube","")
            TTS("Searching about your requests sir")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
            TTS(f"You can see the search result about {text} in your screen")

        if "search in google" in text:
            text = text.replace("jarvis","")
            text = text.replace("search in google","")
            TTS("Searching about your requests sir")
            webbrowser.open(f"https://www.google.com/search?q={text}")
            TTS(f"You can see the search result about {text} in your screen")

        if "music on youtube" in text:
            text = text.replace("music on youtube","")
            text = text.replace('play',"")
            TTS(f"playing your music {text}")
            kt.playonyt(text)
            TTS('enjoy sir')

