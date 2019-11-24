import dem
import speaking
import processss


def on_mo(friendly_name_hass,data):
    print(friendly_name_hass)
    p = 0
    if len(friendly_name_hass)==1 and str(dem.chsv.check_fr(data)).strip("'[]'") =='':
        aaaa=1
    else:
        aaaa=0
    while p < len(friendly_name_hass) and aaaa!=1:
        try:
            r=friendly_name_hass[p].turn_on()
            friendly_name1 = dem.chsv.check_fr(data)
            if r==1:
                if p== len(friendly_name_hass)-1:           # nếu là thiết bị cuối cùng mới đọc thông báo
                    speaking.speak("đã mở "+ str(friendly_name1).strip("'[]'"))
                p += 1
        except:
            speaking.speak('có lỗi thiết bị trên hass')
            p+=1
    
    if len(friendly_name_hass)==0 or aaaa==1:

        speaking.speak("vui lòng nói lại tên thiết bị")
        dem.time.sleep(0.5)
        processss.mixer.music.load('resources/ding.wav')
        processss.mixer.music.play()
        more_data=processss.re_ask()
        friendly_name_hass1 = processss.find_hass_friendly_name(more_data)
        if friendly_name_hass1 == []:
            speaking.speak('xin lỗi em không nghe được')
        else:
            t = 0
            while t < len(friendly_name_hass1):
                try:
                    rr = friendly_name_hass1[t].turn_on()
                    friendly_name1 = dem.chsv.check_fr(more_data) 
                    if rr == 1:
                        if t== len(friendly_name_hass1)-1:            
                            speaking.speak("đã mở "+ str(friendly_name1).strip("'[]'"))
                        t += 1
                except:
                    speaking.speak('có lỗi thiết bị trên hass')
                    t+=1
def off_tat(friendly_name_hass,data):
    q = 0
    if len(friendly_name_hass)==1 and str(dem.chsv.check_fr(data)).strip("'[]'") =='':
        aaaa=1
    else:
        aaaa=0
    while q < len(friendly_name_hass) and aaaa!=1:
        try:
            rr= friendly_name_hass[q].turn_off()
            friendly_name1 = dem.chsv.check_fr(data)
            if rr == 1:
                if q== len(friendly_name_hass)-1: #nếu là thiết bị cuối cùng mới đọc thông báo             
                    speaking.speak("đã tắt "+ str(friendly_name1).strip("'[]'"))
                q += 1
        except:
            speaking.speak('có lỗi thiết bị trên hass')
            q +=1		 



    if len(friendly_name_hass)==0 or aaaa==1:
        speaking.speak(" vui lòng nói lại tên thiết bị")
        processss.mixer.music.load('resources/ding.wav')
        processss.mixer.music.play()
        more_data=processss.re_ask()
        friendly_name_hass1 = processss.find_hass_friendly_name(more_data)
        if friendly_name_hass1 == []:
            speaking.speak('xin lỗi em không nghe được')
        else:
            z = 0
            while z < len(friendly_name_hass1):
                try:
                    r=friendly_name_hass1[z].turn_off()
                    friendly_name1 = dem.chsv.check_fr(more_data)
                    if r == 1:
                        if z== len(friendly_name_hass1)-1:
                            speaking.speak("đã tắt "+ str(friendly_name1).strip("'[]'"))
                        z += 1
                except:
                    speaking.speak('có lỗi thiết bị trên hass')
                    z +=1
def trangthai(sta):
    i = 0
    try:
        if sta == []:
            print('[DEBUG] 9005: STA empty')
            print('')
            speaking.speak('em không hiểu')
        else:
            while i < len(sta):
                doma = sta[i][1]
                enti = sta[i][2]
                do = sta[i][3]
                pa = sta[i][4]
                t,tt = dem.execute.check_state(doma,enti, do,pa)
                speaking.speak(sta[i][0]+ ' đang '+ t)
                i+=1
    except:
        pass

def thietlap(friendly_name_hass,sta,data):
    q = 0
    try:
        r=friendly_name_hass[0].domain_extract()
        doma = sta[0][1]
        enti = sta[0][2]
        do = sta[0][3]
        pa = sta[0][4]
        t,tt = dem.execute.check_state(doma,enti, do,pa)
        tt = tt['attributes']['options']
    except:
        pass
    
    while q < len(friendly_name_hass):
        r=friendly_name_hass[q].domain_extract()
        if str(r)== 'input_select':
            for x in range(len(tt)):
                if tt[x].upper() in data.upper():
                    try:
                        res=friendly_name_hass[q].set_option(tt[x])
                        if res == 1:
                            speaking.speak(' thiết lập thành công ')
                            break
                    except:
                        pass
        q+=1
    
    if 'NHIỆT ĐỘ' in data.upper():
        
        qq=0
        data = data.split()
        x=0
        while x < len(data):
            if data[x].isnumeric() ==True and int(data[x])<32 and int(data[x])>15:
                degree = int(data[x])
                
                break
            x+=1

        while qq < len(friendly_name_hass):
            rep=friendly_name_hass[qq].domain_extract()
            
            if str(rep)== 'climate':
                
                res=friendly_name_hass[qq].set_temperature(degree)
                if res ==1:
                    speaking.speak('Thiết lập máy lạnh sang '+ str(degree)+ ' độ')
                    break
            qq+=1

def hen_gio(data):
    global t1
    from threading import Timer
    
    
    from time import ctime, strftime
    def check_time_in(xi_tin):
        split_lan1 = xi_tin.split()
        
        for m in range(0,len(split_lan1)):
            
            if ":" in split_lan1[m]:
                split_lan2 = split_lan1[m].split(":")
                
                break
            else:
                split_lan2=[]
        return split_lan2

    def more_info_friendly(data,friendly_name):
        continuego=1
        if friendly_name== []:
            qa = 0
            while qa<3:
                qa+=1
                speaking.speak('tác vụ cần làm là gì')
                more_data=processss.re_ask()
                if 'HỦY' in more_data.upper():
                    speaking.speak('thoát chế độ hẹn giờ')
                    continuego=0
                    break
                else:
                    friendly_name = processss.find_hass_friendly_name(more_data)
                    if friendly_name ==[]:
                        pass
                    else:
                        data=more_data
                        break
        return data, friendly_name, continuego                
    def more_info_time(data,time_in_data):
        continue_go =1
        time_in_data=check_time_in(data)
        if time_in_data ==[]:
            qb = 0
            while qb<3:
                qb+=1
                speaking.speak('cung cấp thời điểm thực hiện')
                more_data1=processss.re_ask()
                if 'HỦY' in more_data1.upper():
                    speaking.speak('thoát khỏi chế độ hẹn giờ')
                    continue_go = 0								   
                    break

                else:
                    time_in_data=check_time_in(more_data1)
                    if time_in_data ==[]:
                        pass
                    else:
                        break

        return time_in_data, continue_go
    friendly_name = processss.find_hass_friendly_name(data)
    print(friendly_name)
    time_in_data=check_time_in(data)
    print(time_in_data)
    continue_go=1
    if friendly_name == []:
        abc = more_info_friendly(data,friendly_name)
        friendly_name =abc[1]
        data = abc[0]
        continue_go=abc[2]
        
    if continue_go ==1:
        if time_in_data == []:
            abcd = more_info_time(data,time_in_data)
            time_in_data = abcd[0]
            continue_go=abcd[1]
    if continue_go == 1:
        time_set = dem.datetime.timedelta(hours=int(time_in_data[0]), minutes = int(time_in_data[1]),seconds=00)
        print(time_set)
        time_now_hour =strftime("%H")
        time_now_minute =strftime("%M")
        time_now_second =strftime("%S")
        time_now=dem.datetime.timedelta(hours=int(time_now_hour), minutes = int(time_now_minute),seconds = int(time_now_second))
        
        second_delta = time_set-time_now
        
        secondelta=str(second_delta).split(":")
        
        second_delta_final = int(secondelta[0])*3600+int(secondelta[1])*60+int(secondelta[2])
        
    
    if len(friendly_name) !=0 and int(second_delta_final) >1:
        seconds=int(second_delta_final)
        print('ok')
        speaking.speak('đã đặt hẹn giờ' )
        if 'HẸN GIỜ' in data:
            data=data.replace("HẸN GIỜ","")
            
        t1 = Timer(seconds,processss.jarvis,[data])
        t1.start()
    else:
        speaking.speak('xin thử lại sau')