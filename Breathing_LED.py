import RPi.GPIO as gpio 
import time

gpio.setwarnings(False) 
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT) #This sets the gpio 7 for output
l = gpio.PWM(7,100)#This sets the frequency to 100
l.start(1)#This sets the Duty Cycle to 1

"""This loop lets the LED breathe"""
for i in range (5):
    for i in range(1,100):
        l.ChangeDutyCycle(i)#This changes the Duty Cycle to i
        time.sleep(0.01)

    for i in range(100,1,-1):
        l.ChangeDutyCycle(i)
        time.sleep(0.01)
gpio.cleanup()


