import alsaaudio
import vlc
import threading
import urllib.request
import urllib.parse
import re
import pafy
import random
import queue
import sqlite3 as lite
import time
import execute
import gih
conciu = lite.connect('data.db',check_same_thread=False)
def play_nhac(data,friendly_name_hass):
    print('Vào chương trình phát nhạc')
    p = 0
    while p < len(friendly_name_hass):
            try:
                r=friendly_name_hass[p].media_play()         
                if r==1:
                    # dem.speak("đã phát")
                    return None
                    
                else:
                    p+=1
            except:
                p+=1
                pass

    with conciu:
        curciu=conciu.cursor()
        curciu.execute("SELECT * FROM hamthucthi2")
        rows=curciu.fetchall()
        for row in rows:
            b = 0
            for i in range(0,11):
                if row[i].upper() in data.upper():
                    print(row[i]) 
                    b=1
                    break
            if b==1:
                break 
    vitrirow_i=data.find(row[i])
    print(vitrirow_i)
    data=data[vitrirow_i+len(row[i])+1: len(data)]
    print(data)
    query_string = urllib.parse.urlencode({"search_query" : data})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    random_song=random.randint(0,10)
    urlyt="http://www.youtube.com/watch?v=" + search_results[random_song]
    search_pre_write = (search_results[0],search_results[1],search_results[2],search_results[3],search_results[4],search_results[5],search_results[6],search_results[7],search_results[8],search_results[9],random_song)
    try:
        video = pafy.new(urlyt)
        best = video.getbestaudio()
        playurl = best.url
    except:
        playurl = "http://www.youtube.com/watch?v=jZDrfyVpIls"
    player=vlc.MediaPlayer(playurl)
    player.play()
    try:
        link_yt = gih.info_user()
        with link_yt:
            link_yt_ex = link_yt.cursor()
            link_yt_ex.execute("INSERT INTO link_music_youtube VALUES(?,?,?,?,?,?,?,?,?,?,?)",search_pre_write)
    except Exception as e:
        print(e)
    return player
def lay_am_luong():
    mixerr=alsaaudio.mixers()
    try_number=0
    while try_number <len(mixerr):
        try:
            m= alsaaudio.Mixer(mixerr[try_number])
            break
        except:
            print('Lỗi card âm thanh, đang thử card tiếp theo')
            try_number+=1
    try:
        vol = m.getvolume()
        vol = int(vol[0])
        player_volume=vol
    except Exception as e:
        player_volume = 80
        print(e)
    return player_volume


def phat_radio(data):
    if 'VOV3'in data:
        url = 'https://5a6872aace0ce.streamlock.net/nghevov3/vov3.stream_aac/playlist.m3u8'
    elif 'VOV1' in data: 
        url ='https://5a6872aace0ce.streamlock.net/nghevov1/vov1.stream_aac/playlist.m3u8'
    elif 'VOV2' in data:
        url ='https://5a6872aace0ce.streamlock.net/nghevov1/vov2.stream_aac/playlist.m3u8'
    elif 'VOV GIAO THÔNG' in data:
        url ='https://5a6872aace0ce.streamlock.net/nghevovgthn/vovgthn.stream_aac/playlist.m3u8'
    else:
        url = 'http://120.72.118.102:1935/live/channel3/playlist.m3u8'
    player=vlc.MediaPlayer(url)
    player.play()
    return player



def phat_tiep_theo():
    link_yt = gih.info_user()
    with link_yt:
        link_yt_ex1 = link_yt.cursor()
        link_yt_ex1.execute("SELECT * FROM link_music_youtube")
        rows_yt = link_yt_ex1.fetchall()
    for row in rows_yt:
        while True:
            yt=random.randint(0,11)
            if yt != row[10]:
                urlyt="http://www.youtube.com/watch?v=" + row[yt]
                break
        break
    video = pafy.new(urlyt)
    best = video.getbestaudio()
    playurl = best.url
    player=vlc.MediaPlayer(playurl)
    player.play()
    return player


def to_len():
    try:
        oo= alsaaudio.Mixer('Master')
    except:
        oo= alsaaudio.Mixer('PCM')
    vol = oo.getvolume()
    vol = int(vol[0])
    newVol = vol + 15
    if newVol < 100:
        oo.setvolume(newVol)
    else:
        oo.setvolume(100)
def nho_xuong():
    try:
        pp= alsaaudio.Mixer('Master')
    except:
        pp= alsaaudio.Mixer('PCM')
    vol = pp.getvolume()
    vol = int(vol[0])
    newVol1 = vol - 20
    
    if newVol1 > 30:
        pp.setvolume(newVol1)
    else:
        pp.setvolume(30)
def amluong(data):
    for vol_ex in data.split():
        if vol_ex.isdigit():
            vol_extract=vol_ex
            break
    try:
        m1= alsaaudio.Mixer('Master')
    except:
        m1= alsaaudio.Mixer('PCM')
    
    if int(vol_extract)<100 and int(vol_extract)>0:
        m1.setvolume(int(vol_extract))
    elif int(vol_extract)<0:
        m1.setvolume(30)
    elif int(vol_extract)>99:
        m1.setvolume(99)
    return vol_extract











