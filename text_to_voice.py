from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
print("Enter file Name")
filename=input()
# The text that you want to convert to audio
ff = open(filename+'.txt','r')

filetext = ff.read()

# Language in which you want to convert
language = 'en'

myobj = gTTS(text=filetext, lang=language, slow=False)


myobj.save(filename+'.mp3')


