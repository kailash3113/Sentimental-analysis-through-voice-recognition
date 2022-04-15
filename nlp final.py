from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import pyttsx3
from pyttsx3.engine import Engine
import weakref
import random

compressing_background_voice = ["compressing the background",
                  "The background noise is compressed",
                  "Clearing the background noise",
                  "clearing the background noise, please wait",
                  "Clearing the buzz noise",
                  "The background buzz noise is cleared",
                  "hey gorgeous, The background noise is compressing"]

please_speak = ["kindly speak",
                "please speak",
                "Hey gorgeous, please speak",
                "can you speak, please",
                "Hey buddy, Kindly speak"]

voice_is_recording = ["Your voice is recognizing",
                      "recognizing your sentiment",
                      "recognizing your cute voice",
                      "analyzing your sentiment",
                      "analyzing your voice"]

         
def init():
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()    
    with sr.Microphone() as source:
        cbvr = random.sample(compressing_background_voice,1)
        print("".join(cbvr))
        engine.say(cbvr)
        recognizer.adjust_for_ambient_noise(source,duration=1)
        psvr = random.sample(please_speak,1)
        print("".join(psvr))    
        engine.say(psvr)
        engine.runAndWait()
        recoadedaudio = recognizer.listen(source)
        vrsc = random.sample(voice_is_recording,1)
        print("".join(vrsc))
        engine.say(vrsc)
        engine.runAndWait()
           
    try:
        Text = recognizer.recognize_google(recoadedaudio,language='en-US')
        print("Your message : {}".format(Text))
       
    except Exception as ex:
        print(ex)
    engine.say(Text)  
    sentence = [str(Text)]
    analyzer=SentimentIntensityAnalyzer()
    for i in sentence:
        v = analyzer.polarity_scores(i)
        maxval = max(zip(v.values(),v.keys()))[1]
        print(v)
           
        out = []
        if maxval=='neu':
            out = "The recorded statement is neutral"
            
        elif maxval=='pos':
            out = "The recorded statement is positive"
        else:
            out = "The recorded statement is Negative"
        print(out)


    engine.say(out)
    engine.runAndWait()
    volume = engine.getProperty('volume')  
    engine.setProperty('volume',0.7)    
    rate = engine.getProperty('rate')   # getting details of current speaking rate                      #printing current voice rate
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[0].id)
   
    return out

from tkinter import *
from PIL import Image,ImageTk
class NLP:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("976x560")
        self.img=Image.open('imgnlp.jpg').resize((976,560))
        self.img=ImageTk.PhotoImage(self.img)
        self.my_canvas = Canvas(self.root)
        self.my_canvas.place(x=0,y=0,relheight=1,relwidth=1)
        self.my_canvas.create_image(0,0 ,image=self.img, anchor="nw")
        #self.my_canvas.create_text(97, 25, text="Sentimental Analysis through Voice Recognition",fill='white',anchor = "nw",font=("Courier",22,'bold'))
        self.my_canvas.create_text(60,140, text="Press the button to start recording...",fill='white',anchor = "nw",font=("Times New Roman",17,'bold'))
        self.but=Button(text="Record",command=self.record,height=2,width=10)
        self.but.place(x=190,y=190)
        self.text_canvas=self.my_canvas.create_text(60,250, text="",fill='white',anchor = "nw",font=("Courier",12,'bold'))
        self.root.mainloop()
    def record(self):
        try:
            self.my_canvas.itemconfig(self.text_canvas,text="")
            self.my_canvas.delete(self.imgemoji1)
        except:
            print("initiating")
            
        x= init()
        self.my_canvas.itemconfig(self.text_canvas,text=x)
        self.imgemoji(x)
            
    def imgemoji(self,n):
        if(n=="The recorded statement is neutral"):
            self.imgemoji1=Image.open('neutral.jpe+g').resize((200,200))
            self.imgemoji1=ImageTk.PhotoImage(self.imgemoji1)
            self.emoji=self.my_canvas.create_image(130,300,image=self.imgemoji1, anchor="nw")
        elif(n=="The recorded statement is positive"):
            self.imgemoji1=Image.open('pos.jpg').resize((200,200))
            self.imgemoji1=ImageTk.PhotoImage(self.imgemoji1)
            self.emoji=self.my_canvas.create_image(130,300,image=self.imgemoji1, anchor="nw")
        elif(n=="The recorded statement is Negative"):
            self.imgemoji1=Image.open('neg.jpg').resize((200,200))
            self.imgemoji1=ImageTk.PhotoImage(self.imgemoji1)
            self.emoji=self.my_canvas.create_image(130,300,image=self.imgemoji1, anchor="nw")
            
if  __name__=='__main__':
    app=NLP()

    
_activeEngines = weakref.WeakValueDictionary()

def init(driverName=None, debug=False):

   
    try:
        eng = _activeEngines[driverName]
    except KeyError:
        eng = Engine(driverName, debug)
        _activeEngines[driverName] = eng
    return eng


def speak(text):
    engine = init()
    engine.say(text)
    engine.runAndWait()






