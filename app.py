from tkinter import *
from tkinter import messagebox, filedialog
import mp3info

import vlc

# from pygame import mixer
# mixer.init()

filename = 'music/song1.mp3'
flag = 0

root = Tk()
root.geometry('600x500')
root.title("Music Streamer")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icons/play.png'))

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

def change(photo_frame):
    new = PhotoImage(file='img1.jpg')
    photo_frame.configure(image=new)
    photo_frame.photo=new



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
            mp3info.info(filename)
            change(photo_frame)

        except:
            pass
    except:
        print('new song')

        p = vlc.MediaPlayer(filename)
        try:
            p.play()
            status_bar['text'] = 'Playing Song - ' + str(filename.split('/')[-1])
            mp3info.info(filename)
            change(photo_frame)


        except:
            pass

def set_vol(val):
    volume = int(val)
    try:
        p.audio_set_volume(volume)
    except:
        pass


detail_frame = Frame(root,height='300',width='100')
song_photo = PhotoImage(file='default.png')
song_photo.zoom(20,20)
photo_frame = Label(detail_frame, image=song_photo)


button_frame = Frame(root, height="400", width="300", bg="green")

play_photo = PhotoImage(file='icons/play.png')
play_btn = Button(button_frame, image=play_photo, command=play_music)
play_btn.pack(side=LEFT)



pause_photo = PhotoImage(file='icons/pause.png')
pause_btn = Button(button_frame, image=pause_photo, command=pause_music)
pause_btn.pack(side=LEFT)

stop_photo = PhotoImage(file='icons/stop.png')
stop_btn = Button(button_frame, image=stop_photo, command=stop_music)
stop_btn.pack(side=LEFT)


scale_frame1 = Frame(root, height="20", width="300")
volume_photo = PhotoImage(file='icons/volu.png')
Label(scale_frame1, image=volume_photo).pack(side=LEFT)
scale = Scale(scale_frame1, from_=0, to=100, orient=HORIZONTAL, relief=SUNKEN, command=set_vol)
scale.pack(side=LEFT)
scale.set(50)



status_bar = Label(root, text='Open a file to Play', relief=SUNKEN, anchor=W)

status_bar.pack(side=BOTTOM,fill=X)
Label(root, text='').pack(fill=X, side=BOTTOM)
button_frame.pack(side=BOTTOM)
scale_frame1.pack(side=BOTTOM)
photo_frame.pack(side=RIGHT)
detail_frame.pack(side=BOTTOM)

root.mainloop()

