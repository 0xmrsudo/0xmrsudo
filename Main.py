import androidhelper

d=androidhelper.Android()

def speak(string):
    d.ttsSpeak(string)    
speak("hallo world")
