'''
created for completion of course
@author: Muthu Revanth M

Language Translations:
de-German
la-Latin
fr-French
es-Spanish'''

import speech_recognition as sr
import requests
import json
import sys 


KEY = 'trnsl.1.1.20190406T031103Z.818a2060024ab0d3.88840fa03a5aa7b017ccd07e681b2657084fdb12'
API_BASE = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

r = sr.Recognizer()


try:
    def rec_audio():
        global record
        mic=sr.Microphone()
        with mic as source :
            print("recording audio....say something..:" )
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
        record=r.recognize_google(audio)
        print("Did you just say:"+record)
        return audio
except:
    print("Error while recording the audio")
rec_audio()

print()
def startpy():

    word=record
    ft_content = translate_en_to_de(word)
    fh_content = translate_en_to_la(word)
    fs_content = translate_en_to_fr(word)
    fk_content = translate_en_to_es(word)

    print(word)
    print(ft_content)
    print(fh_content)
    print(fs_content)
    print(fk_content)

def translate_en_to_de(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-de')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content

def translate_en_to_la(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-la')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content

def translate_en_to_fr(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-fr')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content

def translate_en_to_es(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-es')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content   

if __name__ == '__main__':
    startpy()
  




