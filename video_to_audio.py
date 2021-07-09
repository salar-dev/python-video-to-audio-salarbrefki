# Salar Brefki
# YouTube: https://www.youtube.com/channel/UCphD-Ww9JnrBXRfzy6Ivg0g
# Facebook: https://www.facebook.com/salar.brefki/

import moviepy.editor
from tkinter.filedialog import *
import tkinter as tk
from tkinter import font
from tkinter import filedialog
import re
import os

# Function to convert the video
def convert_to_audio():
    # 1
    video = askopenfilename()
    video = moviepy.editor.VideoFileClip(video)
    # 2
    audio = video.audio
    audio_name = entry.get() + '.mp3'
    audio.write_audiofile(audio_name)
    # 3 move the sound to another dec
    folder_selected = filedialog.askdirectory()
    fol_sel = re.sub('/',  '//',    folder_selected)
    source = audio_name
    save_dec = fol_sel + '//' + audio_name
    os.replace(source, save_dec)

# UI Window
window = tk.Tk()
window.title('Video to audio')
myFont = font.Font(size=13)
window.geometry("400x200")

title = tk.Label(
    text="Video To Audio",
     font=("Arial", 25)
     , foreground='red').pack()

boxSize = tk.Frame(master=window, height=20).pack()

entry = tk.Entry(font = "Helvetica 12 bold", fg="red")
entry.insert(0, 'audio 1')
entry.pack()

boxSize = tk.Frame(master=window, height=20).pack()


button = tk.Button(
    text="Select Video",
    width=25,
    height=2,
    bg="red",
    fg="white",
    command=convert_to_audio
)
button['font'] = myFont
button.pack()

window.mainloop()
