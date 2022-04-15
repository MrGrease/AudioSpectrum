## What is "AudioSpectrum"

**Audiospectrum** program that uses libraries such as **moviepy** o create a video with a background,text and audio which can be provided by the user. 

The program starts by importing audio from the user, the name of the audio file can be provided with the first argument of the program when running through the command line. It then generates a background from a jpg file which the user can provide by replacing the sample background image named Background.jpg. The program turns the background image into an **Imageclip** which is a function of the **moviepy** that allows the user to convert images into video. The **Imageclip** object is then added to an array named **clips** which will be used to combine every aspect of the video at the end of the program.

Once the background is generated, the program checks for a second argument, if provided the second argument will be used as a string. This string will be the text that is displayed on the video. If no argument is provided "No Text Entered" will be the string used to build a **Textclip** which is function of the **moviepy** library that allows the user to create videos with text.

Once both these tasks are completed the program converts the audio into a **wav** file which is saved as **temp.wav** this is done to allow **wave** library to read "frames" of data from the audio as samples.

It then superimposes an audio spectrum made by taking samples from the audio that the user provides every second. Each sample is then split into 20 pieces on an array and each piece is plotted individually by having the signal on one axis and time on the other. These plots are then taken and have their backgrounds removed including any and all axis, which leaves us with only the plot itself. The plot itself is then converted to an **Imageclip**. Each **Imageclip** is 0.05 seconds in length. After every sample is taken, each **Imageclip** is concatenated into a single video which is then combined with the rest of the other **moviepy** objects.

After all the **moviepy** objects are combined the program outputs the combined video data as an mp4.

## Requirements
* numpy - for its arrays
* matplotlib - for plotting the audio
* moviepy - for converting everything into video data
* wave - for examining the audio data
* sys - for taking in the arguments through cmd

### Execution
0. A background jpg (optional), and an audio file MUST be provided. 
1. Execution is done through main.py, or the commandline.
> python main.py [name of audio file] [string to be displayed]
2. The line listed above with the required sections filled will start the process, if no audio is provided the program will look for "audio.wav".
3. The program will output the video outside of the folder it is currently in once it is done.

### Sample video
[Sample video displaying result](https://youtu.be/GwYxQnCL3qM)
