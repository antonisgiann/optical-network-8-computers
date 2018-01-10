import threading
import time

class Mythread(threading.Thread):
    def __init__(self,func,*args):
        self.func=func
        self.args=args
        threading.Thread.__init__(self)

    def run(self):
        self.func(*self.args)
