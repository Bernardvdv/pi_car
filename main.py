#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os

import colorsys
import math

import requests

import pantilthat
from sys import exit

pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)

pi_camera = VideoCamera(flip=True) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/<direction>/<int:angle>')
def api(direction, angle):
    if angle < 0 or angle > 180:
        return "{'error':'out of range'}"

    angle -= 90

    if direction == 'pan':
        pantilthat.pan(angle)
        return "{{'pan':{}}}".format(angle)

    elif direction == 'tilt':
        pantilthat.tilt(angle)
        return "{{'tilt':{}}}".format(angle)

    return "{'error':'invalid direction'}"

@app.route('/rgb')
def rgb():
#     while True:
    t = time.time()
    b = (math.sin(t * 2) + 1) / 2
    b = int(b * 255.0)
    t = round(time.time() * 1000) / 1000
    r, g, b = [int(x*255) for x in  colorsys.hsv_to_rgb(((t*100) % 360) / 360.0, 1.0, 1.0)]
    pantilthat.set_all(r, g, b)
    pantilthat.show()
    return render_template('index.html')

@app.route('/white')
def white():
    pantilthat.light_mode(pantilthat.WS2812)
    pantilthat.light_type(pantilthat.GRBW)
    pantilthat.clear()
    pantilthat.set_all(0, 0, 0, 255)
    pantilthat.show()
    return render_template('index.html')

@app.route('/off')
def off():
    pantilthat.light_mode(pantilthat.WS2812)
    pantilthat.light_type(pantilthat.GRBW)
    pantilthat.clear()
    pantilthat.show()
    return render_template('index.html')

@app.route('/car_forward')
def car_forward():
    try:
        url = 'http://192.168.1.107/forward'
        x = requests.get(url) 
        return render_template('index.html')
    except:
        return render_template('index.html')

@app.route('/car_backward')
def car_backward():
    try:
        url = 'http://192.168.1.107/backward'
        x = requests.get(url) 
        return render_template('index.html')
    except:
        return render_template('index.html')

@app.route('/car_stop')
def car_stop():
    try:
        url = 'http://192.168.1.107/off'
        x = requests.get(url) 
        return render_template('index.html')
    except:
        return render_template('index.html')

@app.route('/car_left')
def car_left():
    try:
        url = 'http://192.168.1.107/left'
        x = requests.get(url) 
        return render_template('index.html')
    except:
        return render_template('index.html')

@app.route('/car_right')
def car_right():
    try:
        url = 'http://192.168.1.107/right'
        x = requests.get(url) 
        return render_template('index.html')
    except:
        return render_template('index.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
   
