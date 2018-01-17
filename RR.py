import RPi.GPIO as gpio
import time
import pygame
import random

def LED(times, output_number, sleep):
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(output_number, gpio.OUT)
    for i in range(times):
        time.sleep(sleep)
        gpio.output(output_number, True)
        time.sleep(sleep)
        gpio.output(output_number, False)

def play(Frequency, sleep, times, output_number):
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(output_number, gpio.OUT)
    gpio.output(output_number, True)
    m = gpio.PWM(output_number, Frequency)
    m.start(50)
    for i in range(times):
        time.sleep(sleep)
        m.changeDutyCycle(100)
        time.sleep(sleep)
        m.ChangeDutyCycle(50)

    
