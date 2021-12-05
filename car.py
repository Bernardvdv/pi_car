from flask import Flask, render_template, Response, request
import time
import threading
import os

import requests
import RPi.GPIO as gpio

in1 = 18
in2 = 15
en = 14

gpio.setmode(gpio.BCM)
gpio.setup(in1,gpio.OUT)
gpio.setup(in2,gpio.OUT)
gpio.setup(en,gpio.OUT)
gpio.output(in1,gpio.LOW)
gpio.output(in2,gpio.LOW)
p=gpio.PWM(en,1000)
p.start(25)



app = Flask(__name__)

@app.route('/')
def index():
    return "Yeah", 200

@app.route('/forward')
def forward():
    while(1):
        gpio.output(in1,gpio.HIGH)
        gpio.output(in2,gpio.LOW)

    return "Yeah", 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
