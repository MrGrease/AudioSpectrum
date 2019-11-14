import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from moviepy.editor import*
from moviepy.video.io.bindings import mplfig_to_npimage
from moviepy.video.VideoClip import DataVideoClip
from PIL import Image
import matplotlib.pyplot as plt
import wave
import sys

def input2fig (audiocut):


    fig, ax = plt.subplots(frameon=False)
    plt.plot(audiocut, color='yellow',linewidth=10)
    fig = plt.gcf()
    fig.set_size_inches(6,6)
    plt.axis('off')
    fig.patch.set_alpha(0.0)
    return fig
    
def fig2data ( fig ):

    # draw the renderer
    fig.canvas.draw ( )
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = np.frombuffer ( fig.canvas.tostring_argb(), dtype=np.uint8 )
    buf.shape = ( w, h,4 )
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll ( buf, 3, axis = 2 )
    return buf



def imagetoclip(image,clips,currenttime):

    frame=ImageClip(image)#.set_duration(0.10)

    frame=frame.set_start(currenttime)

    frame=frame.set_end(currenttime+0.10)

    clips.append(frame)

    return clips
    

def cycle(clips,audiocut):

    figure=input2fig(audiocut)

    image=fig2data(figure)

    imagetoclip(image,clips)

    return clips

def audiowork(clips):


    
    
    
    audiofile = wave.open("temp.wav","rb")

    frames = audiofile.getnframes()
    rate = audiofile.getframerate()
    duration = frames / float(rate)
    
    sz = audiofile.getframerate()
    window = 1  # time window to analyze in seconds
    samplecount = int(duration)  # number of time windows to process
    signalscale = 0.1  # signal scale factor

    for num in range(samplecount):
        print('Processing from {} to {} s'.format(num*window, (num+1)*window))
        avgf = np.zeros(int(sz/2+1))
        snd = np.array([])
    # The sound signal for q seconds is concatenated. The fft over that
    # period is averaged to average out noise.
        
        for j in range(window):
            
            da = np.fromstring(audiofile.readframes(sz), dtype=np.int16)
            left, right = da[0::2]*signalscale, da[1::2]*signalscale
            lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))
            snd = np.concatenate((snd, (left+right)/2))
            avgf += (lf+rf)/2

            
        avgf /= window
    # Plot both the signal.
        plt.figure()
        a = plt.subplot(frameon=False)  # signal
        r = 2**16/2
        a.set_ylim([-20000, 20000])
        x = np.arange(44100*window)/44100
        y=np.split(x,10)
        m=np.split(snd,10)
        plt.axis('off')

        fig = plt.gcf()
        fig.patch.set_alpha(0.0)
        fig.set_size_inches(6,6)
        
        


        
        for i in range(0,9):
            print("Processing...")
            plt.plot(y[i], m[i], color='yellow',linewidth=2)
            myfig=fig2data (fig)
            clips=imagetoclip(myfig,clips,num+((i+1)/10))
    
    clips=concatenate(clips,method="compose")
    return clips
        
    
