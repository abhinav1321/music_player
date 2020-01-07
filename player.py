from tkinter import *
from tkinter import messagebox, filedialog
import time
import vlc


root = Tk()
root.geometry('300x300')


class VlcPlayer:
    def __init__(self, filename):
        self.filename = filename

        self.p = vlc.MediaPlayer(self.filename)

    def play(self):
        print('pLaying')
        self.p.play()


    def pause(self):
        self.p.pause()

    def stop(self):
        print('stopping')
        self.p.stop()

    def set_volume(self, volume=50):
        self.p.audio_set_volume(int(volume))


obj = VlcPlayer(filename='music/song3.mp3')
obj.play()
timeout = time.time() + 20

while True:
    if time.time()>timeout:
        obj.stop()


