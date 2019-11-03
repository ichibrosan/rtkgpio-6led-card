#!/usr/bin/python3

# Copyright (c) 2019 Douglas Wade Goodall, All Rights Reserved.

import RTk.GPIO as GPIO

#import time


class RTkGPIO:
    
    def __init__(self,pin):
        self.pin = pin
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,False)
        
    def on(self):
        GPIO.output(self.pin,True)
        
    def off(self):
        GPIO.output(self.pin,False)

###################    
# eof - rtkgio.py #
###################      
