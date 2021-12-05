from flask import Flask, render_template, Response, request
import time
import threading
import os

import requests
import RPi.GPIO as gpio

in1 = 15
in2 = 18
en = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)



app = Flask(__name__)

@app.route('/')
def index():
    return "Yeah", 200

@app.route('/forward')
def forward():
    while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            
    return "Yeah", 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
