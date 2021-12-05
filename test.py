import sys
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

Forward = 9
Backward = 10
Enable = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(Enable, GPIO.OUT)

p=GPIO.PWM(Enable, 1000)
p.start(25)

def forward(t):
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Backward, GPIO.LOW)
    print("Moving Forward")

def reverse(t):
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")

while(1):
    forward(3)
