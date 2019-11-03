#!/usr/bin/python3

import RTk.GPIO as GPIO
import time

LED1R = 17
LED1G = 27
LED1B = 22
LED2R = 10
LED2G = 9
LED2B = 11
LED3R = 0
LED3G = 5
LED3B = 6
LED4R = 8
LED4G = 7
LED4B = 1
LED5R = 13
LED5G = 19
LED5B = 26
LED6R = 16
LED6G = 20
LED6B = 21

def init(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)

# main entry point
init(LED1R)
init(LED1G)
init(LED1B)

init(LED2R)
init(LED2G)
init(LED2B)

init(LED3R)
init(LED3G)
init(LED3B)

init(LED4R)
init(LED4G)
init(LED4B)

init(LED5R)
init(LED5G)
init(LED5B)

init(LED6R)
init(LED6G)
init(LED6B)

GPIO.output(LED6B,True)

number = 0
while(1):
    
