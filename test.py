#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import the json library
import json
import requests
import urllib
#text = input('Nhập câu muốn chuyển: ')
url = "https://viettelgroup.ai/voice/api/tts/v1/rest/syn"
data = {"text": 'Nhập câu muốn chuyển: Dịch vụ tự động chuyển đổi văn bản thành tiếng nói Tiếng Việt, sử dụng trí tuệ nhân tạo với ngữ điệu tự nhiên, đa dạng giọng đọc và dễ dàng tích hợp', "voice": "doanngoclev2", "id": "2", "without_filter": False, "speed": 1.0, "tts_return_option": 2}
headers = {'Content-type': 'application/json', 'token': 'demo_token'}
cert_path = (dirname+'/wwwvtccai.crt')
response = requests.post(url, data=json.dumps(data), headers=headers)
#if encounter SSL error because of https certificate, please comment out above line and use the line below to  make insecure connections   (this will expose your application to security risks, such as man-in-the-middle attacks.)
#response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
# Headers is a dictionary
print(response.headers)
# Get status_code.
print(response.status_code)
# Get the response data as a python object.
data = response.content
f = open("tmp/test.wav", "wb")
f.write(data)
f.close()