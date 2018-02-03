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
    for i in range (3):##This makes a loop.
    gpio.cleanup()
    time.sleep(1)
gpio.cleanup()
    
