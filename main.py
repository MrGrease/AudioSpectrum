import numpy as np
from moviepy.editor import*
import sys
import textandbackground as tnbg
import audiospectrum as auds


def main():
#config variables

    screenSize = (800,600)

    clips = []


#end of config variables

#import Audio
    if len(sys.argv)>1:
        audioclipname = sys.argv[1]
        audioclip = AudioFileClip(audioclipname)
    else:
        audioclip = AudioFileClip("audio.wav")

    video_Duration =audioclip.duration

#Use the background.jpeg in the folder as a background for the video
    clips=tnbg.backgroundgeneration(clips,video_Duration)
#Generate some text and add it to the video
    clips=tnbg.textgeneration(clips,sys.argv,screenSize)
#Convert audio to wav so we can work on it
    audioclip.write_audiofile("temp.wav", fps=44100, nbytes=2, buffersize=2000, codec="pcm_s16le", bitrate="256k", ffmpeg_params=None, write_logfile=False, verbose=True)
#Obtain fft from wav
    clips.append(auds.audiowork([]))
#Combine all the clips
    final_Clip = CompositeVideoClip(clips,size = screenSize).set_duration(video_Duration)
#Set the Audio to be played
    final_Clip = final_Clip.set_audio(audioclip)
#Save the clips to a video file
    final_Clip.write_videofile("../AudioSpectrumVisualizedOutput.mp4",fps=10,codec='libx264')

#Credits    
    print ("Audio spectrum visualizer by;")
    print ("Mehmet Emre Yorulmaz")
#End of Main


if __name__== "__main__":
  main()
