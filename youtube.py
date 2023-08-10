import os
from pytube import YouTube
import re

link='https://www.youtube.com/watch?v=Epz7-L-NJnA'
yt= YouTube(link)
print(f'Title: {yt.title}')
print(f'Number of views: {yt.views}')
print(f'Rating of the video: {yt.rating}')
print(f'Thubnail: {yt.thumbnail_url}')

ys=yt.streams.get_highest_resolution()
print('downloading')
ys.download()
print('Download compelted!')

def youtube_audio_downloader(ink):
    if 'youtube.com' not in link:
        print('Invalid youtube link')
    return False

audio= yt.streams.filter(only_audiio=True).first()
print('downaloding audio...', end='')
output_file=audio.download()
if os.path.exists(output_file):
   print('done')
else:
   print('error')
   

basename = os.path.baseneme(output_file)
name, extension = os.path.splitext(basename)
audio_file=f'{name}.mp3'
audio_file = re.sub('\s+', '-', audio_file)
os.rename(basename, audio_file)

mp3 = youtube_audio_downloader(link)
print(mp3)
    
   
    
