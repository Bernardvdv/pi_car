from flask import Flask, render_template, Response, request
import time
import threading
import os

import requests
import sys
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

Forward = 10
Backward = 9
Enable = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(Enable, GPIO.OUT)

p=GPIO.PWM(Enable, 1000)
p.start(25)

app = Flask(__name__)

@app.route('/')
def index():
    return "Yeah", 200

@app.route('/forward')
def forward():
    while True:
        GPIO.output(Forward, GPIO.HIGH)
        GPIO.output(Backward, GPIO.LOW)
        print("Moving Forward")
    return "Moving Forward", 200

@app.route('/backward')
def backward():
    while True:
        GPIO.output(Forward, GPIO.LOW)
        GPIO.output(Backward, GPIO.HIGH)
        print("Moving Backward")
    return "Moving Backward", 200

@app.route('/stop')
def backward():
    while True:
        GPIO.output(Forward, GPIO.LOW)
        GPIO.output(Backward, GPIO.LOW)
        print("Stop")
    return "Stop", 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
