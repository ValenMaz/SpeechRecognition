# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:53:01 2022

@author: VALENMAZ
"""

import speech_recognition as sr
import webbrowser

sr.Microphone(device_index=1)


r=sr.Recognizer()


r.energy_threshold=5000

with sr.Microphone() as source:
    print("Habla")
    audio=r.listen(source) 
    try:
        text=r.recognize_google(audio)
        print("Dijiste : {}".format(text))
        url='https://www.google.co.in/search?q='
        search_url=url+text
        webbrowser.open(search_url)
    except:
        print("No puedo reconocerlo")

