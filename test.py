import RPi.GPIO as gpio
import time 
ir=5
gpio.setmode(gpio.BCM)
gpio.setup(ir,gpio.IN)
while(1):
    reading =gpio.input(ir)
    if (reading == False): 
       print ("black")
    else:
        print("white")

    time.sleep(1)
