import os
from pytube import YouTube

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

audio= yt.streams.filter(only_audiio=True).first()
output_file=audio.download()

basename = os.path.baseneme(output_file)
name, extension = os.path.splitext(basename)
audio_file=f'{name}.mp3'


