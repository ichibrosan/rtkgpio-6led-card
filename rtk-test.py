#!/usr/bin/python3

#import * FROM rtkgpio
from rtkgpio import *

led1 = RTkGPIO(LED1G)
led1.on()
