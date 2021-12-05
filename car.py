from flask import Flask, render_template, Response, request
import time
import threading
import os

import requests
import sys
import time
import RPi.GPIO as GPIO

# in1 = 18
# in2 = 15
# en = 14
GPIO.setwarnings(False)

Forward = 18
Backward = 15
Enable = 15


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
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Backward, GPIO.LOW)
    print("Moving Forward")

    return "Yeah", 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
