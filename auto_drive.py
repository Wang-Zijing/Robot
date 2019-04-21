# -*- coding: utf-8 -*-
import  RPi.GPIO as gpio    #导入所有模块
import  time
import  sys
import  random

def init():  #定义初始化GPIO引脚的函数
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.IN)
    gpio.setwarnings(False)

def forward(t):  #定义前进的函数
    init()  #初始化引脚
    gpio.output (12, True)  #让右电机逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def backward(t):  #定义后退的函数
    init()  #初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, True)  #让右电机顺转
    gpio.output (22, False)  #让左电机不顺转
    gpio.output (18, True)  #让左电机逆转
    gpio.setup(7,gpio.OUT)  #打开倒车灯
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def turn_right(t):  #定义右转的函数
    init()  #初始化引脚
    gpio.output (12, False)  #让右电机不逆转
    gpio.output (16, False)  #让右电机不顺转
    gpio.output (22, True)  #让左电机顺转
    gpio.output (18, False)  #让左电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def turn_left(t):  #定义左转的函数
    init()  #初始化引脚
    gpio.output (12, True)  #让左电机逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def  stop(t):
    init()
    gpio.output (12, False)  #让左电机不逆转
    gpio.output (16, False)  #让左电机不顺转
    gpio.output (22, False)  #让右电机不顺转
    gpio.output (18, False)  #让右电机不逆转
    time.sleep(t)  #等待时间t
    gpio.cleanup()  #清除引脚的输出

def output_ultrasonic_wave():
    init()
    gpio.output(13,True)
    time.sleep(0.00001)
    gpio.output(13,False)
    while gpio.input(15) == False:
        pass
    t1 = time.time()
    gpio.cleanup()
    return t1

def distance():
    gpio.setwarnings(False)   
    t1 = output_ultrasonic_wave()
    init()
    gpio.setwarnings(False)
    while gpio.input(15) == True:
        pass
    t2 = time.time()
    t  = t2 - t1
    distance = t * 34000 / 2
    gpio.cleanup()
    return distance

while True:
    forward(0.05)
    d = distance()
    if  d < 15:
        stop(1)
        backward(1)
        turn = random.randint(1, 2)
        if turn == 1:
            turn_left(1.5)
        else:
            turn_right(1.5)
    gpio.cleanup()
