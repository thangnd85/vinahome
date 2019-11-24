from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import re
import lun
from lun import S2L
from lun import L2S
from gtts import gTTS
import os
import pygame
import time
from pygame import mixer
from helper import *
import speaking
def ngaymai():
    print ('Âm lịch ngày mai')
    a = 'Ngày mai'
    ngay = datetime.date.today() + timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def ngaymot():
    print ('Âm lịch ngày mốt')
    a = 'ngày mốt'
    ngay = datetime.date.today() + timedelta(2)
    yy = ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def homqua():
    print ('Âm lịch hôm qua')
    a = 'hôm qua'
    ngay = datetime.date.today() - timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def homnay():
    a = 'hôm nay'
    print ('âm lịch hôm nay')
    ngay = datetime.date.today()
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd

def ngaykhac(data):
    today=datetime.date.today()
    print ('Âm lịch ngày')
    if 'NGÀY' in data:
        ngay = re.search('NGÀY (.+?)(.+?)', data)
        dd = int(ngay.group(1)+ngay.group(2))
    else: 
        dd = today.day
    if 'THÁNG' in data:
        thang = re.search('THÁNG (.+?)(.+?)', data)
        mm = int(thang.group(1)+thang.group(2))	
    else:
        mm = today.month    
    yy = today.year		
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)
    daa = str(yy)+'-'+str(mm)+'-'+str(dd)
    ngay = datetime.datetime.strptime(daa, '%Y-%m-%d')
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)+' năm nay'
    return a,ngay,yy,mm,dd



def kiemtra_amlich(a, ngay,yy,mm,dd):
    lunar_date = S2L(dd, mm, yy)
    ngay_am = str(lunar_date[0])
    list_thang = ["tháng Giêng","tháng Hai","tháng Ba","tháng Tư","tháng Năm","tháng Sáu","tháng Bảy","tháng Tám","tháng Chín","tháng Mười","tháng Mười một","tháng Chạp"]
    thang_am = int(str(lunar_date[1]))-1
    thang_am1 = list_thang[thang_am]
    can = ['Canh ', 'Tân ', 'Nhâm ', 'Quý ', 'Giáp ', 'Ất ', 'Bính ', 'Đinh ','Mậu ','Kỷ ']
    chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
    nam = int(str(lunar_date[2]))
    vitri_can = nam % 10
    vitri_chi = nam % 12
    nam_am = str(lunar_date[2])
    # lunar_text2 = 'Ngày: ' + str(lunar_date[0]) + ' - ' + thang_am1  + ' năm '  + can[vitri_can] + chi[vitri_chi] + ' (' +  str(lunar_date[2]) +')'
    ss = int(ngay_am)
    nam_nhuan = int(str(lunar_date[3]))	
    if ss == 15:
        speaking.speak(a+" là ngày rằm "+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+' ' + nam_am)
    elif ss == 1:
        speaking.speak(a+" là ngày mùng một "+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+ ' ' + nam_am)
    elif ss>1 and ss<15:
        days_left = 15 - ss
        speaking.speak(a+" là ngày " + ngay_am +' '+ thang_am1 + ' năm ' + can[vitri_can] +' '+ chi[vitri_chi] +' '+ nam_am + ". Còn " + str(days_left) + " ngày nữa là đến rằm")
    elif ss>15 and ss<30:
        thang_sau = thang_am + 1
        if thang_am < 12:
            nam_a = nam_am 
        else:
            nam_a = nam_am + 1
            # ny = yy + 1
            a2d = L2S(28,12,yy,nam_nhuan)
            nd = a2d[0]
            td = a2d[1]
            nmd = a2d[2]
            daa = str(nd)+'-'+str(td)+'-'+str(nmd)
            a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
            ngaytet = a2dnew.day
            thangtet = a2dnew.month
            namtet = a2dnew.year
            nammoi = S2L(ngaytet,thangtet,namtet)
            nam_nhuan = int(str(nammoi[3]))
        next = L2S(1,thang_sau,int(nam_a), nam_nhuan)
        nd = next[0]
        td = next[1]
        nmd = next[2]
        daa = str(nd)+'-'+str(td)+'-'+str(nmd)
        a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
        delta = a2dnew - datetime.datetime.today()
        days_left = delta.days
        thang_am = list_thang[thang_am]
        ngay_am =str(lunar_date[0])
        speaking.speak(a+' là ngày ' + ngay_am +' '+ thang_am + ' năm ' + can[vitri_can]+' ' + chi[vitri_chi]+' ' + nam_am)					  
    else:
        speaking.speak(str(a)+'  là ngày ' + str(ngay_am)+' ' + str(thang_am) + ' năm ' + str(can[vitri_can])+' ' + str(chi[vitri_chi])+ ' ' + str(nam_am))