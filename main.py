from tkinter import *
from pygame import mixer
from tkinter import filedialog
import os
from PIL import ImageTk, Image

list=[]

musik=0

mixer.init()
root = Tk()
load = Image.open("image.png")
render = ImageTk.PhotoImage(load)
root.iconphoto(False, render)
root.title("Pemutar Musik Sederhana")

master_frame = Frame(root)
master_frame.pack()

info_frame = Frame(master_frame)
info_frame.grid(row=0, column=1)

controls_frame = Frame(master_frame)
controls_frame.grid(row=0, column=0)

file_frame = Frame(master_frame)
file_frame.grid(row=1, column=1)

song_state = Label(info_frame, width=60, text="No Song Played", font="Arial 8 bold")
song_state.grid(row=0, column=0)

song_box = Listbox(info_frame, width=60,height=20, selectbackground="#FD841F", bg="#B3FFAE")
song_box.grid(row=2, column=0)

def prev_song():
    global musik
    musik=musik-1
    if musik == 0:
        musik=len(list)
    back = songs[musik]

    mixer.music.load(back)
    mixer.music.play()
    song_state['text'] = "Playing"
def next_song():
    global musik
    musik=musik+1
    if musik == len(list):
        musik=0
    next_s = list[musik]

    mixer.music.load(next_s)
    mixer.music.play()
    song_state['text'] = "Playing"
def play():
    musik=list[0]
    mixer.music.load(musik)
    mixer.music.play()
    song_state['text'] = "Playing"
def pause():
    if song_state['text'] == "Pause":
        mixer.music.unpause()
        song_state['text'] = "Playing"

    else:
        mixer.music.pause()
        song_state['text'] = "Pause"
def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "Stoped"

def open_folder():
    global songs
    songs = filedialog.askopenfilenames(initialdir='tracks/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    for song in songs:
        list.append(song)
        song_box.insert(END, os.path.basename(song))



back_button = Button(controls_frame,text="⟸", width=5,height=5, command=prev_song)
forward_button = Button(controls_frame,text="⟹", width=5,height=5, command=next_song)
play_button = Button(controls_frame,text="▶", width=5,height=5, command=play)
pause_button = Button(controls_frame,text="⏸️", width=5,height=5, command=pause)
stop_button = Button(controls_frame,text="🛑", width=5,height=5, command=stop)
back_button.grid(row=0, column=0)
forward_button.grid(row=1, column=0)
play_button.grid(row=2, column=0)
pause_button.grid(row=3, column=0)
stop_button.grid(row=4, column=0)

openfolder_button = Button(file_frame,width=15, text="Select Music", command=open_folder)
openfolder_button.grid(row=1,column=0)
root.mainloop()