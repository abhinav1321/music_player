from tkinter import *
from tkinter import messagebox, filedialog
import mp3info
import time


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
    info=mp3info.info(filename)
    title1['text']=info['title']
    title0['text']='TITLE:'
    artist0['text']='ARTIST:'
    artist1['text']=info['artist']
    album0['text']='ALBUM:'
    album1['text']=info['album']
    new = PhotoImage(file='img1.jpg')
    new = new.subsample(2,2)
    photo_frame.configure(image=new)
    photo_frame.photo=new

def song_list():

    try:
        import scraping
        list = scraping.top_songs()
        # print(list)
        new_window=Tk()
        new_window.title('TOP 20 SONGS')
        for i,song in enumerate(list):
            song_var=''
            print(song[0])
            frame =Frame(new_window)
            song_lbl=Label(frame,text='SONG- '+str(song[0]),anchor=W,relief=SUNKEN)
            desc_lbl=Label(frame,text='    Description- '+str(song[1]),anchor=W)
            song_var=song[0]

            def combine_funcs(*funcs):
                def combined_func(*args, **kwargs):
                    for f in funcs:
                        f(*args, **kwargs)

                return combined_func

            def button_check(buttonName):
                buttonVal = buttonName
                print(buttonVal)

                # button=Button(frame,text='Download'+str(song_var),command=lambda :scraping.download(song_var))
            button = Button(frame, text='Download'+str(song_var), command=combine_funcs(lambda :scraping.download(song_var), lambda
                buttonName='Download'+str(song_var): button_check(buttonName)))

            song_lbl.pack(side=LEFT)
            desc_lbl.pack(side=LEFT)
            button.pack(side=LEFT)
            frame.pack(side=TOP)

        new_window.mainloop()


    except Exception as e:
        print(e)


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

submenu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Weekly TOP 20', menu=submenu)
submenu.add_command(label='Search',
                    command=song_list)



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
            change(photo_label)



        except:
            pass
    except:
        print('new song')

        p = vlc.MediaPlayer(filename)
        try:
            p.play()

            status_bar['text'] = 'Playing Song - ' + str(filename.split('/')[-1])
            mp3info.info(filename)
            change(photo_label)



        except:
            pass



def set_vol(val):
    volume = int(val)
    try:
        p.audio_set_volume(volume)
    except:
        pass

def audio_slider(val):
    length=p.get_length()
    print(length)
    unit=int(length/1000)
    new_length=unit*int(val)
    p.set_time(new_length*10)
    new_time = time.strftime('%H:%M:%S', time.gmtime(new_length))
    time_label['text'] = str(new_time)



def time_slider():
    set_new=int(100*p.get_time()/p.get_length())
    scale1.set(set_new)



detail_frame = Frame(root,height='300',width='100')
photo_frame = Frame(detail_frame)
text_frame = Frame(detail_frame)

song_photo = PhotoImage(file='default.png')
song_photo=song_photo.subsample(3,3)
photo_label = Label(photo_frame, image=song_photo)
photo_label.pack()


title0 = Label(text_frame,text='',font='Helvetica 18 bold')
title1 = Label(text_frame,text='')

artist0 = Label(text_frame, text='',font='Helvetica 18 bold')
artist1 = Label(text_frame, text='')

album0 = Label(text_frame, text='',font='Helvetica 18 bold')
album1 = Label(text_frame, text='')

title0.pack(), title1.pack(), artist0.pack(), artist1.pack(), album0.pack(), album1.pack()
photo_frame.pack(side=RIGHT)
text_frame.pack(side=RIGHT)

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

scale_frame2 = Frame(root)
time_label=Label(scale_frame2,text="00:00",anchor=W)
time_label.pack(side=LEFT)
scale1 = Scale(scale_frame2,orient=HORIZONTAL,  length=600,command=audio_slider)

scale1.pack()



status_bar = Label(root, text='Open a file to Play', relief=SUNKEN, anchor=W)

status_bar.pack(side=BOTTOM,fill=X)
Label(root, text='').pack(fill=X, side=BOTTOM)
scale_frame2.pack(side=BOTTOM)
button_frame.pack(side=BOTTOM)
scale_frame1.pack(side=BOTTOM)
photo_frame.pack(side=RIGHT)
detail_frame.pack(side=BOTTOM)


root.mainloop()









