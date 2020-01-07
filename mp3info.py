from re import search
from mutagen.easyid3 import ID3
from mutagen import File




def info(filename):
    song_details = {
        'title':'',
        'artist':'',
        'album':'',
    }
    music = ID3(filename)
    for k, v in music.items():
        if k=='TALB':
            song_details['album'] = v
        if k=='TPE1':
            song_details['artist'] = v
        if k=='TIT2':
            song_details['title'] = v
        if search('APIC', str(k)):
            with open('img1.jpg', 'wb') as img:
                img.write(v.data)


    return song_details
