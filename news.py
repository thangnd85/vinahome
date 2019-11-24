import requests
from bs4 import BeautifulSoup as bs
import re
import random
import vlc
import time
import threading
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

link = requests.get("http://netnews.vn/audio-hai.html", headers=headers)
soup = bs(link.content,"lxml")
#print(soup)
c = soup.find_all("script")
s = len (c)
for i in range (0,s):
    if '.mp3' in str(c[i]):
        m = str(c[i])
#        link = re.sub(r'id[.+?] = ','',link)
#        l = re.match(r'http://.*?\.mp3',link)
#        print (link)
        start = m.find('http://')
        kk = m[start:]
        end = kk.find('.mp3')
        me = kk[0:end+4]
#        print (me)
    
t = soup.find_all("a")
ss = len(t)
ll = []
for i in range (0,ss):
    if ('http://' in str(t[i]) and '.html' in str(t[i]) and 'audio' in str(t[i])):
        l = str(t[i])
        ll.append(l)
#        print (str(i))
#        print (l)
#        l = bs(l,"lxml")
qu = [me]
sss = len(ll)
for i in range (0,sss):
    h1 = str(ll[i])
    start = h1.find('href="')
    kk = h1[start:]
    end = kk.find('.html')
    h1l = kk[6:end+5]
#    print (h1l)
    url = 'http://netnews.vn/'+h1l
    link = requests.get(url, headers=headers)
    soup = bs(link.content,"lxml")
    c = soup.find_all("script")
    s = len (c)

    for j in range (0,s):
        if '.mp3' in str(c[j]):
            m = str(c[j])
#        link = re.sub(r'id[.+?] = ','',link)
#        l = re.match(r'http://.*?\.mp3',link)
#        print (link)
            start = m.find('http://')
            kk = m[start:]
            end = kk.find('.mp3')
            me = kk[0:end+4]
            
#            print (me)
            qu.append(me)
print (qu)
def player():
    song_list= random.sample(qu, 4)
    Instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
    for song in song_list:
        player=Instance.media_player_new()
        media=Instance.media_new(song)
        time.sleep(10)
        media.get_mrl()
        player.set_media(media)
        player.play()
        playing = set([1,2,3,4])
        time.sleep(2)
        duration = player.get_length() / 1000
        mm, ss = divmod(duration, 60)
        name = song.replace('http://medianews.netnews.vn:8080/netnews/archive/radio','Tin :')
        naame = name.replace('.mp3','')
        print (name)
        while True:
            state = player.get_state()
            if state not in playing:
                break
            continue
thread = threading.Thread(target=player)
thread.start()
