from machine import Pin, PWM
import time

# nodemcu / motor shield pins
pin1 = Pin(5, Pin.OUT)  # D1 Direction
pin2 = Pin(4, Pin.OUT)  # D2 Direction
pin3 = Pin(0, Pin.OUT)  # D3 Speed
pin4 = Pin(2, Pin.OUT)  # D4 Speed

# h-bridge pins
BIN1 = PWM(pin1, freq=750)
BIN2 = PWM(pin3, freq=750)
AIN1 = PWM(pin2, freq=750)
AIN2 = PWM(pin4, freq=750)

# speed/direction values
speed = 1023
fwd = 0
rev = 1023


def stop_all():
    for each in (BIN1, BIN2, AIN1, AIN2):
        each.duty(0)


def backward():
    print("Backward")
    BIN1.duty(speed)
    BIN2.duty(rev)
    AIN1.duty(speed)
    AIN2.duty(rev)


def forward():
    print("Forward")
    BIN1.duty(speed)
    BIN2.duty(fwd)
    AIN1.duty(speed)
    AIN2.duty(fwd)


def hardleft():
    print("HardLeft")
    BIN1.duty(speed)
    BIN2.duty(fwd)
    AIN1.duty(speed)
    AIN2.duty(rev)


def left():
    print("Left")
    BIN1.duty(speed)
    BIN2.duty(fwd)
    AIN1.duty(0)
    AIN2.duty(0)


def right():
    print("Right")
    BIN1.duty(0)
    BIN2.duty(0)
    AIN1.duty(speed)
    AIN2.duty(fwd)


def hardright():
    print("HardRight")
    BIN1.duty(speed)
    BIN2.duty(rev)
    AIN1.duty(speed)
    AIN2.duty(fwd)