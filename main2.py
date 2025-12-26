import speech_recognition as sr
import webbrowser
import pyttsx3
import time
recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
def processcommand(c):
    if  "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://www.linkedin.com")
    
        
    
   

if __name__ == "__main__":
    speak("Initializing nexa. I am ready to assist you")
    
    while True:
    
    
        
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = recognizer.listen(source, timeout=2)
                

            
            print("recognizing...")
            word = recognizer.recognize_google(audio)
            
            if(word.lower() == "nexa"):
                speak("ya")
                time.sleep(1)
                
                with sr.Microphone() as source:
                    print("nexa active")
                    audio = recognizer.listen(source)
                    
                    command = recognizer.recognize_google(audio)
                    
                    processcommand(command)
                    
                    
            
            
        
        except Exception as e:
            print("Error; {0}".format(e))

   
