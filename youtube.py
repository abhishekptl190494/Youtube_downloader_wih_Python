import os
from pytube import YouTube
import re
import openai

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


#loadinf opeai api key

with open('key.txt', 'r') as f:
    api_key = f.read().strip('\n')
    assert api_key.startswith('sk-')
openai.api_key = api_key

def transcribe(audio_file):
    if not os.path.exists(audio_file):
        print('audio does not exist')
        return False
    
    with open(audio_file, 'rb') as f:
        print('start transcribe..', end='')
        transcipt = openai.Audio.transcribe('whisper-1', f)
        print('done')

        name, extension = os.path.splitext(audio_file)
        transcript_name= f'transcipt-{name}.txt'
        with open(transcript_name, 'w')as f:
            f.write(transcribe['text'])

    return transcript_name
transcript_name = transcribe(mp3)
with open(transcript_name) as f:
    print(f.read())

    if not os.path.exists(transcript_name):
        print('transcript does not exists')
        
    with open(transcript_name)as f:
        transcript = f.read()

    system_prompt = 'I want to act as a Life coach'
    prompt = f'''create a summary of the following text.
    Text: {transcript}

    ...sdsdsd...sdsdsd...sdsdsd...dfgf.g.fg.f.gfg...gfgfgfgds....'''

    print('start summarizing', end='')
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system', 'content': system_prompt},
            {'role':'user', 'content': prompt}
        ],
        max_tokens=2048,
        temperature=1
    )
    print('done')
r=response['choices'][0]['message']['content']



    



    
   
    
