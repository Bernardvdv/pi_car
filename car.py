from flask import Flask, render_template, Response, request
import time
import threading
import os

import requests
import RPi.GPIO as gpio

in1 = 15
in2 = 18
en = 14

gpio.setmode(GPIO.BCM)
gpio.setup(in1,GPIO.OUT)
gpio.setup(in2,GPIO.OUT)
gpio.setup(en,GPIO.OUT)
gpio.output(in1,GPIO.LOW)
gpio.output(in2,GPIO.LOW)
p=gpio.PWM(en,1000)
p.start(25)



app = Flask(__name__)

@app.route('/')
def index():
    return "Yeah", 200

@app.route('/forward')
def forward():
    while(1):
        if x=='r':
            print("run")
            if(temp1==1):
                gpio.output(in1,gpio.HIGH)
                gpio.output(in2,gpio.LOW)
            
    return "Yeah", 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
