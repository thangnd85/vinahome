# import pdb

import signal
import execute
import sys
signal.signal(signal.SIGTSTP, execute.handler)
signal.signal(signal.SIGINT, execute.signal_handler)
import dem
import threading
import time



dem.mainloop()

