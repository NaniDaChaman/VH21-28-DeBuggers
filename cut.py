from moviepy.editor import *
audioclip = AudioFileClip("mlk.wav")
audioclip.subclip(12,22).write_audiofile("chmlk.wav")
