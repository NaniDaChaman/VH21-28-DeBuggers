# -*- coding: utf-8 -*-
"""speechrecon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y96WLKsq-iYVpqtW-OsFdEoopPOokHWM
"""

import speech_recognition as sr
#from IPython.display import Audio
from moviepy.editor import *
import os

filen=input("Enter the name of the file to be converted : ")
filen=filen+".mp4"
vidclip=VideoFileClip(filen)#creates video clip object
filename=input("Enter the name of your audio file : ")+".wav" 
vidclip.audio.write_audiofile(filename)#extracts audio and writes the clip as an audio file

if "Video_Chunks" not in os.listdir() :
  os.mkdir("Video_Chunks")
else :
  path=os.getcwd()+"/Video_Chunks/"
  for aud in list(filter(lambda x:x.endswith(".mp4"),os.listdir(path))):
    os.remove(path+aud)

i=0.0
l="1"
while i< vidclip.end :
  if i+20<vidclip.end:
    vidclip.subclip(i,i+20).write_videofile(os.getcwd()+"/Video_Chunks/"+f"{filename[:-4]}{l}.mp4")
  else :
    vidclip.subclip(i,vidclip.end).write_videofile(os.getcwd()+"/Video_Chunks/"+f"{filename[:-4]}{l}.mp4")
  i=i+20
  l=l+"1"

#udio("chmlk.wav")

#filename=input("Your Audio File : ")+".wav"

if "Audio_Chunks" not in os.listdir() :
  os.mkdir("Audio_Chunks")
else :
  path=os.getcwd()+"/Audio_Chunks/"
  for aud in list(filter(lambda x:x.endswith(".wav"),os.listdir(path))):
    os.remove(path+aud)

wholeclip=AudioFileClip(filename)
i=0.0
l="1"
while i< wholeclip.end :
  if i+20<wholeclip.end:
    wholeclip.subclip(i,i+20).write_audiofile(os.getcwd()+"/Audio_Chunks/"+f"{filename[:-4]}{l}.wav")
  else :
    wholeclip.subclip(i,wholeclip.end).write_audiofile(os.getcwd()+"/Audio_Chunks/"+f"{filename[:-4]}{l}.wav")
  i=i+20
  l=l+"1"

audch=list(filter(lambda x:x.endswith(".wav"),os.listdir(f'{os.getcwd()}/Audio_Chunks/')))

audch

if "Text_Chunks" not in os.listdir() :
  os.mkdir("Text_Chunks")
else :
  path=os.getcwd()+"/Text_Chunks/"
  for aud in list(filter(lambda x:x.endswith(".txt"),os.listdir(path))):
    os.remove(path+aud)

def textmaker(filename):
  r=sr.Recognizer()
  with sr.AudioFile(filename) as source:
      audio_data = r.record(source)
      try :
        text =  r.recognize_google(audio_data)
        return text
      except Exception as e:
        return "[Unknown]"

for filename in audch:
  txtfile=f'{os.getcwd()}/Text_Chunks/{filename[:-4]}.txt'
  f=open(txtfile,'w')
  f.write(textmaker(f"{os.getcwd()}/Audio_Chunks/{filename}"))
  f.close()
#f=open("mlt.txt",'r')
#print(f.read())
#f.close()

if "Sub_Video_Chunks" not in os.listdir() :
  os.mkdir("Sub_Video_Chunks")
else :
  path=os.getcwd()+"/Sub_Video_Chunks/"
  for aud in list(filter(lambda x:x.endswith(".mp4"),os.listdir(path))):
    os.remove(path+aud)

for filename in list(filter(lambda x:x.endswith(".txt"),os.listdir(f'{os.getcwd()}/Text_Chunks/'))):
  txtfile=f'{os.getcwd()}/Text_Chunks/{filename}'
  vidfile=f'{os.getcwd()}/Video_Chunks/{filename[:-4]}'
  vidclip=VideoFileClip(vidfile+".mp4")
  f=open(txtfile,'r')
  clip = TextClip(f"{f.read()}", font ="Arial-Bold", fontsize = vidclip.size[1]*0.05, color ="white")
  clip = clip.set_pos('bottom').set_duration(vidclip.duration)
  subvidclip = CompositeVideoClip([vidclip,clip])
  subvidclip.write_videofile(os.getcwd()+"/Sub_Video_Chunks/"+f"{filename[:-4]}.mp4")
# showing  clip  
  #clip.ipython_display()
  f.close()

fin=[]
l1=list(filter(lambda x:x.endswith(".mp4"),os.listdir(f'{os.getcwd()}/Sub_Video_Chunks/')))
l1.sort()
for filename in l1:
  vidfile=f'{os.getcwd()}/Sub_Video_Chunks/{filename}'
  vidclip=VideoFileClip(vidfile)
  fin.append(vidclip)
final_clip = concatenate_videoclips(fin)
final_clip.write_videofile(os.getcwd()+"/subedclip.mp4")

'''l1=list(filter(lambda x:x.endswith(".mp4"),os.listdir(f'{os.getcwd()}/Sub_Video_Chunks/')))
l1.sort()
print(l1)


from moviepy.editor import *

list(filter(lambda x:x.endswith(".txt"),os.listdir(f'{os.getcwd()}/Text_Chunks/')))

#Audio(f"{os.getcwd()}/Audio_Chunks/chmlk2.wav")

"""A little bit about the os module : Its a way to allow python to interact with the operating system especially its file directories.

Note : when files are reffered to by their names in python : they are in the current working directory. ie In the content directory in google colab.

CWD: is also the folder in which python is operating. It starts at '/content' but can be changed using chdir(path string)
"""

import os
os.getcwd()#returns a path string of the cwd.

os.chdir("/content/sample_data")
os.getcwd()

"""Making a directory will make a new folder in our directory net. we take an relative/ absolute path with the foler to be creaed at the end creating a new folder. """

os.mkdir("Geeks")

"""List Dir :- in CWD"""

#os.chdir("/content")
os.listdir()
os.listdir("/content/sample_data")'''