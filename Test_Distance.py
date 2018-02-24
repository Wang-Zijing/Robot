import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.IN)

All = 0

for i in range(10):
    time.sleep(1)
    gpio.output(13, True)
    time.sleep(0.00001)
    gpio.output(13,False)
    while gpio.input(15) == False:
        pass
    t1 = time.time()
    while gpio.input(15) == True:
        pass
    t2 = time.time()
    d = (t2-t1) * 34000 / 2
    All = All + d

distance = All/10
print"The height of your ceiling is:", distance,"cm"

    
