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

def forward(t, right_turn_back, right_turn, left_turn):  #定义前进的函数
    init()#初始化引脚
    gpio.output (12, True)  #让右电机逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)

def backward(t, right_turn_back, right_turn, left_turn,):  #定义后退的函数
    init()#初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机顺转
    gpio.output (22, False)  #让左电机不顺转
    gpio.output (18, True)  #让左电机逆转
    gpio.setup(7,gpio.OUT)  
    gpio.output(7,True)
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)
    
def turn_right(t, right_turn_back, right_turn, left_turn):  #定义右转的函数
    init()#初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)

def turn_left(t, right_turn_back, right_turn, left_turn):  #定义左转的函数
    init()#初始化引脚
    gpio.output (12, True)  #让左电机逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出
    gpio.setwarnings(False)


    
