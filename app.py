from tkinter import *
from tkinter import messagebox, filedialog

import vlc

# from pygame import mixer
# mixer.init()

filename = 'music/song1.mp3'
flag = 0

root = Tk()
root.geometry('400x300')
root.title("Music Streamer")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='play.png'))

text = Label(root, text="Welcome to The Music-World").pack()


def message():
    messagebox.showinfo('Welcome to Music World', "This music Player is Made with Python Tkinter!"
                                                  "It plays music with the help of pygame mixer."
                                                  "created by Abhinav Sharma "
    
                                                  " Contact - abhinavsharma150@gmail.com ")


def browse():
    global filename
    filename = filedialog.askopenfilename()
    status_bar['text'] = "Selected Song - " + str(filename.split('/')[-1]) + " -- Click Play button to play"



# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Sub-menus
submenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Open', command=browse)
submenu.add_command(label='Exit', command=root.destroy)

submenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help!', menu=submenu)
submenu.add_command(label='About Us',
                    command=message)





def stop_music():
    try:
        p.stop()
        status_bar['text'] = 'Click on Play to play again'
    except:
        pass


def pause_music():
    p.pause()
    status_bar['text'] = 'Music Paused'



def play_music():
    try:
        global p
        p.stop()

        p = vlc.MediaPlayer(filename)
        try:
            p.play()
            status_bar['text'] = 'Playing Song - ' + str(filename.split('/')[-1])
        except:
            pass
    except:
        print('new song')

        p = vlc.MediaPlayer(filename)
        try:
            p.play()
            status_bar['text'] = 'Playing Song - ' + str(filename.split('/')[-1])
        except:
            pass

def set_vol(val):
    volume = int(val)
    try:
        p.audio_set_volume(volume)
    except:
        pass


frame = Frame(root, height="200", width="200", bg="green")

play_photo = PhotoImage(file='play.png')
play_btn = Button(frame, image=play_photo, command=play_music)
play_btn.pack(side=LEFT)

pause_photo = PhotoImage(file='pause.png')
pause_btn = Button(frame, image=pause_photo, command=pause_music)
pause_btn.pack(side=LEFT)

stop_photo = PhotoImage(file='stop.png')
stop_btn = Button(frame, image=stop_photo, command=stop_music)
stop_btn.pack(side=LEFT)


frame1 = Frame(root, height="20", width="300")
volume_photo = PhotoImage(file='volu.png')
Label(frame1, image=volume_photo).pack(side=LEFT)
scale = Scale(frame1, from_=0, to=100, orient=HORIZONTAL,relief=SUNKEN, command=set_vol)
scale.pack(side=LEFT)
scale.set(50)

status_bar = Label(root, text='Open a file to Play', relief=SUNKEN, anchor=W)

status_bar.pack(side=BOTTOM,fill=X)
Label(root, text='').pack(fill=X, side=BOTTOM)
frame.pack(side=BOTTOM)
frame1.pack(side=BOTTOM)


root.mainloop()

