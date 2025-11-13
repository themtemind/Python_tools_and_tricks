# This is to get a link to an NPR podcast audio file and play it using pygame's mixer. a simple radio
from pygame import mixer
import requests, bs4
from io import BytesIO

#<a class="audio-module-listen" href="https://prfx.byspotify.com/e/play.podtrac.com/npr-500005/traffic.megaphone.fm/NPR1805005492.mp3?p=500005&amp;e=nsv2-s1-20251113-0100-long&amp;d=280&amp;t=podcast&amp;size=5056585&amp;sc=siteplayer&amp;aw_0_1st.playerid=siteplayer">
url ="https://www.npr.org/podcasts/500005/npr-news-now"
try:
    res = requests.get(url)
    res.raise_for_status()
except Exception as e:
    print(f"Error {e}")

soup = bs4.BeautifulSoup(res.text, 'html.parser')
audio = soup.find_all('a',{'class':'audio-module-listen'})

for item in audio:
    #Obtain the web link for audio file
    audi = item['href']
    mp3 = audi.find("?") #Remove unwanted components
    mp3 = audi[0:mp3]

    voice = requests.get(mp3)
    #Need to create some space in RAM to play the audio file smoothly
    file = BytesIO()
    file.write(voice.content)
    file.seek(0)

    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():
        continue 