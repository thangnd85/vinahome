from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import re


def ngaymai():
    print ('Ngày mai')
    a = 'Ngày mai'
    ngay = datetime.date.today() + timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def ngaymot():
    print ('Ngày mốt')
    a = 'ngày mốt'
    ngay = datetime.date.today() + timedelta(2)
    yy = ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def homqua():
    print ('Hôm qua')
    a = 'hôm qua'
    ngay = datetime.date.today() - timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def homnay():
    a = 'hôm nay'
    print ('Hôm nay')
    ngay = datetime.date.today()
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    return a,ngay,yy,mm,dd
def ngaykhac(data):
    today=datetime.date.today()
    print ('Ngày khác')
    if 'NGÀY' in data:
        ngay = re.search ('NGÀY (.+?)(.+?)', data)
        dd = int(ngay.group(1)+ngay.group(2))
    else: 
        dd = today.day
    if 'THÁNG' in data:
        thang = re.search ('THÁNG (.+?)(.+?)', data)
        mm = int(thang.group(1)+thang.group(2))	
    else:
        mm = today.month    
    yy = today.year		
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)
    daa = str(yy)+'-'+str(mm)+'-'+str(dd)
    ngay = datetime.datetime.strptime(daa, '%Y-%m-%d') 
    return a,ngay,yy,mm,dd

def kiemtra_thu(a,ngay,yy,mm,dd):
    wd=date.weekday(ngay)
    
    days= ["THỨ HAI","THỨ BA","THỨ TƯ","THỨ NĂM","THỨ SÁU","THỨ BẢY","CHỦ NHẬT"]
    if dd < 10:

        docngay = 'ngày mùng '+ str(dd) + ' '
    else: 
        docngay = 'ngày ' + str(dd) + ' '
    return a, days[wd], docngay,mm