
import threading


threadLock = threading.Lock()
pbar = 0

def count():
    global pbar
    with threadLock:
        pbar += 1
        if(pbar%500==0):
            print('.', end="")

