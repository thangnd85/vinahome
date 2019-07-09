import snowboydecoder
import sys
import signal
from googlesamples.assistant.grpc.pushtotalk import main
interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

model = "jarvis.umdl" 

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=[0.5,0.5])
print('Listening... Press Ctrl+C to exit')

detector.start(detected_callback=main,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()