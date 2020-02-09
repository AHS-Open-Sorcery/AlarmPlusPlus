import threading
import playsound

def thread_second():
    while 1:
        playsound.playsound('audio3.mp3', True)

processThread = threading.Thread(target=thread_second)  # <- note extra ','
processThread.start()

while 1:
  print("hi")