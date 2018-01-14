""" If your number and password are all right,
    this program will give you one billion dollars.
    Else,it will let the buzzer beep for three times!""" 
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
gpio.output(11, True)

number = input("Please enter the number:")
secret = raw_input("Please enter the password:")
if number == 123456789 and secret == "opensesame":
    print"You have one billion dollars!!!"
else:
    gpio.output(11, False)
    time.sleep(0.5)
    gpio.output(11, True)
    time.sleep(0.1)
    gpio.output(11, False)
    time.sleep(0.5)
    gpio.output(11, True)
    time.sleep(0.1)
    gpio.output(11, False)
    time.sleep(0.5)    
    gpio.output(11, True)
    time.sleep(0.1)
    gpio.cleanup()
    time.sleep(1)
gpio.cleanup()
    
