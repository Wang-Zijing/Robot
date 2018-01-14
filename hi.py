"""This program will ask your name,
and then it will make the LED say 'hi' to you
with Morse code."""
import  RPi.GPIO as gpio
import  time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7,gpio.OUT)

name = raw_input("What's your name?\n")
def di(times):
    for i in range(times):
        time.sleep(0.2)
        gpio.output(7, True)
        time.sleep(0.2)
        gpio.output(7, False)

def da(times):
    for i in range(times):
        time.sleep(0.2)
        gpio.output(7, True)
        time.sleep(0.6)
        gpio.output(7, False)

di(4)
time.sleep(0.6)
di(2)
print "Hi,"+name+"!"
gpio.cleanup()

