# import pdb
# pdb.set_trace()
import os
import time
time.sleep(240)
os.system('killall pulseaudio')
os.system('pulseaudio -D')
#time.sleep(1)
#os.system('sudo pacmd set-source-volume 1 200000')
#time.sleep(1)
#os.system('sudo pulseaudio --start')
#time.sleep(1)


import dem
import threading
import execute


execute.run_thread(dem.mainloop)

