#!/usr/bin/python3
# tricolor.py

from rtkgpio import *

BLACK=0
RED=1
GREEN=2
BLUE=3

class TriColor:
    def __init__(self,red,green,blue):
        self.redpin = red
        self.greenpin = green
        self.bluepin = blue
        self.red = RTkGPIO(red)
        self.green = RTkGPIO(green)
        self.blue = RTkGPIO(blue)
        self.color = BLACK
    
    def setcolor(self,color):
        if color == BLACK:
            self.red.off()
            self.green.off()
            self.blue.off()
        if color == RED:
            self.red.on()
            self.green.off()
            self.blue.off()
        if color == GREEN:
            self.red.off()
            self.green.on()
            self.blue.off()
        if color == BLUE:
            self.red.off()
            self.green.off()
            self.blue.on()

#####################
# eof - tricolor.py #
#####################

