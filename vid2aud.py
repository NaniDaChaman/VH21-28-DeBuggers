import moviepy.editor as mp
from playsound import playsound
filename=input("Enter the name of the file to be converted : ")
filename=filename+".mp4"
vidclip=mp.VideoFileClip(filename)
audfile=input("Enter the name of your audio file : ")+".mp3"
vidclip.audio.write_audiofile(audfile)
playsound(audfile)