"""This program will make the buzzer sing a song
   called 'Little Star'."""
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
gpio.output(11, True)
m = gpio.PWM(11,262)
m.start(50)
time.sleep(0.5)
m.ChangeDutyCycle(100)
time.sleep(0.2)
m.ChangeDutyCycle(50)
m.ChangeFrequency(262)
time.sleep(0.5)
m.ChangeDutyCycle(100)
time.sleep(0.2)

def play(Prequency):
    m.ChangeDutyCycle(50)
    m.ChangeFrequency(Prequency)
    time.sleep(0.5)
    m.ChangeDutyCycle(100)
    time.sleep(0.2)
    m.ChangeDutyCycle(50)
    m.ChangeFrequency(Prequency)
    time.sleep(0.5)
    m.ChangeDutyCycle(100)
    time.sleep(0.2)

def play2(Prequency):
    m.ChangeDutyCycle(50)
    m.ChangeFrequency(Prequency)
    time.sleep(0.5)
    m.ChangeDutyCycle(100)
    time.sleep(0.7)

play(392)
play(440)

play2(392)

play(349)
play(330)
play(294)

play2(262)

play(392)
play(349)
play(330)

play2(294)

play(392)
play(349)
play(330)

play2(294)
gpio.cleanup()
