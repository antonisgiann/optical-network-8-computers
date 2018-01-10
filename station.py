import random
import package
import time

class station:
    #the constructor for the station objects
    def __init__(self,buffersize,iden):
        self.iden=iden
        self.buffersize=buffersize
        self.buffer=[]
        self.delay={ 'delay' : 0 ,'packages': 0 }
        self.packagesdropped=0
        self.WANT_TO_SENT=False

    #fuction for creating a package 
    def createpack(self,probability):
        n = random.random()
        #check if the station will create a package
        if n<probability :
            newpack = package.package()
            #if the package was created check if the buffer is full
            if len(self.buffer) == self.buffersize :
                del(newpack)
                self.packagesdropped += 1
            #if there is space on the buffer append the package
            else:
                self.buffer.append(newpack)



    #fuction for sending a package
    def sendpack(self):
        #check if there is a package in the buffer
        if self.buffer :
            #calculate the delay of the package
            self.delay['delay'] += time.time() - self.buffer[0].timecreated 
            self.delay['packages'] += 1
            self.buffer.pop(0)


        
