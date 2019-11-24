import os
import time
i = input('Bạn muốn cài đặt vào hệ thống (1) hay venv (2): ')
if i == '1':
	import st
elif i == '2':
	os.system('sudo apt-get install python3-dev python3-venv')

#	os.system('env/bin/python -m pip install --upgrade pip')
	import st_env
else:
	print ('Bạn chọn sai rồi. Bye!')

