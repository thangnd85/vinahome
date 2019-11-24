import json
import requests
import threading
import gih
import sys
version = gih.get_config('version_above084')
class sensor():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
    def domain_extract(self):
        rr='sensor'
        return rr
class binary_sensor():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
    def domain_extract(self):
        rr='binary_sensor'
        return rr
class climate():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
    def domain_extract(self):
        rr='climate'
        return rr
    def set_temperature(self,degree):
        if version == 'right':
            url = self.domain+'/api/services/climate/set_temperature'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',

}
        else:
            url = self.domain + '/api/services/climate/set_temperature?api_password='+ self.password
            headers = {'content-type': 'application/json'}
            
        payload = {'entity_id': 'climate.'+self.entity_id_ex, 'temperature':degree}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
class switch():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
    def turn_on(self):
        if version == 'right':
            url = self.domain+'/api/services/switch/turn_on'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/switch/turn_on?api_password='+ self.password
            headers = {'content-type': 'application/json'}
            
        payload = {'entity_id': 'switch.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def turn_off(self):
        if version == 'right':
            url = self.domain+'/api/services/switch/turn_off'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/switch/turn_off?api_password='+ self.password
            headers = {'content-type': 'application/json'}
        payload = {'entity_id': 'switch.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def domain_extract(self):
        rr='switch'
        return rr
class input_select():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
        
    def set_option(self,option):
        if version == 'right':
            url = self.domain+'/api/services/input_select/select_option'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',

}
        else:
            url = self.domain + '/api/services/input_select/select_option?api_password='+ self.password
            headers = {'content-type': 'application/json'}
            
        payload = {'entity_id': 'input_select.'+self.entity_id_ex, 'option':option}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def domain_extract(self):
        rr='input_select'
        return rr





class media_player():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
    def turn_on(self):
        if version == 'right':
            url = self.domain+'/api/services/media_player/turn_on'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/media_player/turn_on?api_password='+ self.password
            headers = {'content-type': 'application/json'}
            
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def turn_off(self):
        if version == 'right':
            url = self.domain+'/api/services/media_player/turn_off'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/media_player/turn_off?api_password='+ self.password
            headers = {'content-type': 'application/json'}
        


        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def media_play(self):
        if version == 'right':
            url = self.domain+'/api/services/media_player/media_play'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/media_player/media_play?api_password='+ self.password
            headers = {'content-type': 'application/json'}
            
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def media_pause(self):
        if version == 'right':
            url = self.domain+'/api/services/media_player/media_pause'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/media_player/media_pause?api_password='+ self.password
            headers = {'content-type': 'application/json'}
            
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            print(r)
            return r

    def domain_extract(self):
        rr='media_player'
        return rr
class script():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
    def turn_on(self):
        if version == 'right':
            url = self.domain+'/api/services/script/turn_on'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/script/turn_on?api_password='+ self.password
            headers = {'content-type': 'application/json'}
        payload = {'entity_id': 'script.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r

    def domain_extract(self):
        rr='script'
        return rr
class light():
    def __init__(self,entity_id_ex=[],domain='',password=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.password = password
    def turn_on(self):
        if version == 'right':
            url = self.domain+'/api/services/light/turn_on'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/light/turn_on?api_password='+ self.password
            headers = {'content-type': 'application/json'}
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def turn_off(self):
        if version == 'right':
            url = self.domain+'/api/services/light/turn_off'
            headers = {
    'Authorization': 'Bearer '+ self.password,
    'content-type': 'application/json',
}
        else:
            url = self.domain + '/api/services/light/turn_off?api_password='+ self.password
            headers = {'content-type': 'application/json'}
        
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('[DEBUG] - Phản hồi từ Home Assistant: '+ str(r))
            print('')
            if str(r)=='<Response [200]>':
                r=1
                return r
        except:
            r = 0
            return r
    def domain_extract(self):
        rr='light'
        return rr
class define():
    def __init__(self,domain_ex=[], entity_id_ex=[],domain='',password=''):
        self.domain_ex = domain_ex
        self.entity_id_ex= entity_id_ex
        self.domain = domain
        self.password = password
    def define(self):
        if self.domain_ex == 'switch':
            self.object = switch(self.entity_id_ex,self.domain,self.password)
        if self.domain_ex =='script':
            self.object = script(self.entity_id_ex,self.domain,self.password)
        if self.domain_ex == 'light':
            self.object = light(self.entity_id_ex,self.domain,self.password)
        if self.domain_ex == 'sensor':
            self.object = sensor(self.entity_id_ex,self.domain,self.password)
        if self.domain_ex == 'binary_sensor':
            self.object = binary_sensor(self.entity_id_ex,self.domain,self.password)
        if self.domain_ex == 'media_player':
            self.object = media_player(self.entity_id_ex,self.domain,self.password)
        if self.domain_ex == 'input_select':
            self.object = input_select(self.entity_id_ex,self.domain,self.password)
        if self.domain_ex == 'climate':
            self.object = climate(self.entity_id_ex,self.domain,self.password)
        return self.object

def check_state(domain_ex=[],entity_id_ex=[],domain='',password=''):
    if version == 'right':
        url = domain + '/api/states/'+ domain_ex+ '.'+ entity_id_ex
        headers = {
    'Authorization': 'Bearer '+ password,
    'content-type': 'application/json',
}
    else:
        url = domain + '/api/states/'+ domain_ex+ '.'+ entity_id_ex+'?api_password='+password
        headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    r = r.json()
    qq=r
    r = r['state']
    if r == 'off':
        r = 'tắt'
    elif r == 'on':
        r= 'mở'
    else:
        pass
    return r,qq
def run_thread(func,data=None):
    if data is not None:
        t = threading.Thread(target = func, args = (data,))
        t.start()

    else:
        t = threading.Thread(target = func, args = ())
        t.start()

        

def signal_handler(sig, frame):
    
        print('BẠN MỚI ẤN CTRL+C PHẢI KHÔNG, BYE BYE NHÉ')
        
        sys.exit(0)




def handler(signum, frame):
    print('Ố Ô, THẤY BẠN ẤN CTRL+Z RỒI, NHƯNG MÀ TÔI CHẶN RỒI NHÉ')
