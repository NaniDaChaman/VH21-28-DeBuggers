from pydub import AudioSegment
song=AudioSegment.from_mp3("alls.mp3")
f10=song[:10000]
f10.export("inp.wav" ,format="wav")