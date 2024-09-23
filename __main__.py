from threading import Thread
from time import sleep

def someWork(val):
    for k in range(20):
        print(f"In function {x}")
        sleep(0.4)   # 400 milliseconds

def main():
    # Args must be a list
    t1 = Thread(target = someWork, args=(51,))
    t1.start()
    for m in range(20):
        print(f"In Main {m}")
        sleep(0.25)   # 250 milliseconds