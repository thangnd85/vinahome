from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import lun
from lun import S2L
from lun import L2S
import random
def ngayle_check(data):
    ngay = datetime.datetime.today()
    dd = ngay.day
    mm = ngay.month
    yy = ngay.year
    lunar = S2L(dd,mm,yy)
    nam_am = int(lunar[2])
    thang_am  = int(lunar[1])
    nam_nhuan = int(lunar[3])
    print ('>>> NGÀY LỄ')
    if 'TẾT TÂY' in data:
        xx = yy + 1
        ev = datetime.datetime(xx,1,1)
        n = str(ev.day)
        t = str(ev.month)
        nm = str(ev.year)
        d = ev - ngay
        a = 'Tết Tây '
        
    elif 'TẾT TA' in data:
        nam_a = nam_am + 1
        a2d = L2S(28,12,yy,nam_nhuan) #Đổi sag nggayf dương 28/12
        nd = a2d[0]
        td = a2d[1]
        nmd = a2d[2]
        daa = str(nd)+'-'+str(td)+'-'+str(nmd) #Đổi sag ddihj dạng ngày
        a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
        a2d = a2dnew + timedelta(3)			
        nnm = a2d.day
        tnm = a2d.month
        nnm = a2d.year
        nammoi = S2L(nnm,tnm,nnm)
        nam_nhuan = int(str(nammoi[3]))
        ev = L2S(1,1,nam_a,nam_nhuan)
        n = str(ev[0])
        t = str(ev[1])
        nm = str(ev[2])
        daa = str(n)+'-'+str(t)+'-'+str(nm)
        a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
        d = a2d - ngay
        a = 'Tết Ta '
        
    elif 'TRUNG THU' in data:
        ev = L2S(15,8,nam_am,nam_nhuan)
        n = str(ev[0])
        t = str(ev[1])
        nm = str(ev[2])
        daa = str(n)+'-'+str(t)+'-'+str(nm)
        a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
        d = a2d - ngay
        a = 'Trung thu'
        
    elif 'GIỖ TỔ' in data:
        ev = L2S(10,3,nam_am,nam_nhuan)
        n = str(ev[0])
        t = str(ev[1])
        nm = str(ev[2])
        daa = str(n)+'-'+str(t)+'-'+str(nm)
        a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
        d = a2d - ngay
        a = 'Giỗ tổ Hùng Vương'
        
    elif '30' in data:
        ev = datetime.datetime(yy,4,30)
        n = str(ev.day)
        t = str(ev.month)
        nm = str(ev.year)
        d = ev - ngay
        a = 'Giải phóng miền Nam'
        
    elif 'QUỐC KHÁNH' in data:
        ev = datetime.datetime(yy,9,2)
        n = str(ev.day)
        t = str(ev.month)
        nm = str(ev.year)
        d = ev - ngay
        a = 'Quốc khánh'
        
    else:
        pass
    dayleft = d.days
#	b = []
    if int(dayleft) > 29 :
        b =['Bạn mong chờ ngày '+a+' quá đấy! Còn lâu mà. ','Đùa nhau à '+a+'qua rồi mà. ','Sắp rồi, vài ngày nữa thôi. ']
    elif int(dayleft) < 30:
        b = ['Sắp đến '+a+' rồi.','Hình như ngày mai, à không phải. ','Rồi rồi, sắp được nghỉ rồi. ','Ráng chờ đi, còn vài ngày nữa nhé. ']
    c = random.choice(b)
    return c, dayleft, a,n,t,nm