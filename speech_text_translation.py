import speech_recognition as sr
import tkinter as tk 
from tkinter.ttk import *
import requests
import json
#import sys 

record="Not started"

KEY = ''  #API key for Yandex Translation API
API_BASE = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

r = sr.Recognizer() #Recognizer class 
 
try:
    def rec_audio():   #function to record audio
        global record
        mic=sr.Microphone() #fuction to access the microphone
        with mic as source :
            print("recording audio....say something..:" )
            r.adjust_for_ambient_noise(source) #function to cancel the background noise
            audio=r.listen(source) #function to listen the speech
            record=r.recognize_google(audio) #google speech API to recognize the speech
        print("Did you just say:"+record)
        vtext['text']=record

        return record
except:
    print("Error while recording the audio")


widget=tk.Tk(className="VTconverter") #creation of GUI widget
title=tk.Label(widget,text="Wanna print what you say....Hit the Button below") #label function
title.pack()
rec=tk.Button(widget,text="Record",command=lambda:rec_audio()) #button function
rec.pack()
widget.update()
vtext=tk.Label(widget,text="Not started")
vtext.pack()
gtext=tk. Button(widget,text="German",command=lambda:translate_en_to_de(record))
gtext.pack()
gtext=tk.Label(widget,text=" ")
gtext.pack()
ltext=tk.Button(widget,text="Latin",command=lambda:translate_en_to_la(record))
ltext.pack()
ltext=tk.Label(widget,text=" ")
ltext.pack()
frtext=tk.Button(widget,text="French",command=lambda:translate_en_to_fr(record))
frtext.pack()
frtext=tk.Label(widget,text=" ")
frtext.pack()
stext=tk.Button(widget,text="Spanish",command=lambda:translate_en_to_es(record))
stext.pack()
stext=Label(widget,text=" ")
stext.pack()



def startpy():

    print(record)

    ft_content = translate_en_to_de(record) #calling function to translate to German
    fh_content = translate_en_to_la(record) #calling function to translate to Latin 
    fs_content = translate_en_to_fr(record) #calling function to translate to French
    fk_content = translate_en_to_es(record) #calling function to trnaslate to Spanish

    #print(record)
    #print(ft_content)
    #print(fh_content)
    #print(fs_content)
    #print(fk_content)

def translate_en_to_de(content):       #function to translate to German
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-de')

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    gtext['text']=tr_content


    return tr_content

def translate_en_to_la(content):       #function to translate to Latin
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-la')

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]
     
    ltext['text']=tr_content

    return tr_content

def translate_en_to_fr(content):       #function to translate to French
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-fr')

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    frtext['text']=tr_content


    return tr_content

def translate_en_to_es(content):       #function to translate to Spanish
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-es')

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]
    stext['text']=tr_content


    return tr_content 


widget.mainloop()

if __name__ == '__main__':
    startpy()

  



