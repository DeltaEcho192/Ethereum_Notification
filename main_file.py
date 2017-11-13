import threading
from threading import Thread
import time

def func1():
    starttime=time.time()
    while True:
        import setup_file
        localtime = time.asctime( time.localtime(time.time()) )
        print ("setup", localtime)
        time.sleep(86400)

def func2():
    starttime2=time.time()
    while True:
        import price_check
        localtime = time.asctime( time.localtime(time.time()) )
        print ("check", localtime)
        time.sleep(600)

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
