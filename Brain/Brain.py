try :
    import webbrowser
    import wikipedia
except ModuleNotFoundError:
    import subprocess
    subprocess.run('pip install wikipedia')
    import webbrowser

from Engine.TTS import TTS

def get_answer(text):
    try:
        return wikipedia.summary(text,sentences=1)
    except Exception :
        TTS("Searching about your requests sir")
        webbrowser.open(f"https://www.google.com/search?q={text}")
        TTS(f"You can see the search result about {text} in your screen")

