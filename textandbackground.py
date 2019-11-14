import numpy as np
from moviepy.editor import*


def backgroundgeneration(clips,video_Duration):
    
#Add a background to display on the video

    backGround = (ImageClip("Background.jpg").set_duration(video_Duration))

    clips.append(backGround)

    return clips
    

#End of Background generation

def textgeneration(clips,arguments,screenSize):
    
#Generate Text to display on the video using inbuilt moviepy functions
    
    if len(arguments)>2:
        videoText = arguments[2]
    else:
        videoText = "No Text Entered"
        
    textToBePrinted = TextClip(videoText,method='caption',color="purple",font="Arial",kerning=5,fontsize=50)

    compositeClip = CompositeVideoClip([textToBePrinted.set_pos("bottom")],size=screenSize)
    
    clips.append(compositeClip)

    return clips
    
#End of Text Generation
