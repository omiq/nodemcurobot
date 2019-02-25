from machine import Pin, PWM
import time

""" nodemcu pins from the motor shield """
pin1 = Pin(5, Pin.OUT)  # D1
pin2 = Pin(4, Pin.OUT)  # D2
pin3 = Pin(0, Pin.OUT)  # D3
pin4 = Pin(2, Pin.OUT)  # D4

""" named after the L9110 h-bridge pins """
BIN1 = PWM(pin1, freq=750)
BIN2 = PWM(pin3, freq=750)
AIN1 = PWM(pin2, freq=750)
AIN2 = PWM(pin4, freq=750)

""" TODO: variable speed """
speed = 950


def stop_all():
    for each in (BIN1, BIN2, AIN1, AIN2):
        each.duty(0)


def backward():
    BIN1.duty(0)
    BIN2.duty(speed)
    AIN1.duty(0)
    AIN2.duty(speed)


def forward():
    print("Forward")
    BIN1.duty(speed)
    BIN2.duty(0)
    AIN1.duty(speed)
    AIN2.duty(0)


def left():
    BIN1.duty(speed)
    BIN2.duty(0)
    AIN1.duty(0)
    AIN2.duty(speed)


def right():
    BIN1.duty(0)
    BIN2.duty(speed)
    AIN1.duty(speed)
    AIN2.duty(0)


