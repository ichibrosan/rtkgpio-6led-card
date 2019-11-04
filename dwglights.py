#!/usr/bin/python3

from rtkgpio import *
from time import *

from sixledcard import *
from tricolor import *

class CLights:
    
    def __init__(self):
        self.led1 = TriColor(LED1R,LED1G,LED1B)
        self.led2 = TriColor(LED2R,LED2G,LED2B)
        self.led3 = TriColor(LED3R,LED3G,LED3B)
        self.led4 = TriColor(LED4R,LED4G,LED4B)
        self.led5 = TriColor(LED5R,LED5G,LED5B)
        self.led6 = TriColor(LED6R,LED6G,LED6B)
    

    def alloff(self):
        self.led1.setcolor(BLACK)
        self.led2.setcolor(BLACK)
        self.led3.setcolor(BLACK)
        self.led4.setcolor(BLACK)
        self.led5.setcolor(BLACK)
        self.led6.setcolor(BLACK)
            
    
    def hextet(self,x,color):
        if x & 0x20:
            self.led6.setcolor(color)
        else:
            self.led6.setcolor(BLACK)
        
        if x & 0x10:
            self.led5.setcolor(color)
        else:
            self.led5.setcolor(BLACK)
            
        if x & 0x08:
            self.led4.setcolor(color)
        else:
            self.led4.setcolor(BLACK)
                
        if x & 0x04:
            self.led3.setcolor(color)
        else:
            self.led3.setcolor(BLACK)
                    
        if x & 0x02:
            self.led2.setcolor(color)
        else:
            self.led2.setcolor(BLACK)
                        
        if x & 0x01:
            self.led1.setcolor(color)
        else:
            self.led1.setcolor(BLACK)
        

    def count(self):
        x = 0
        color = RED
        while(1):            
            self.hextet(x,color)         
            x += 1
            
            color += 1
            if color>BLUE:
                color = RED
            
            
            
            sleep(1)
