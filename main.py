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

import curses
import pantilthat

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

#setting start up serrvo positions
a = .5
b = .5

pantilthat.pan(a)
pantilthat.tilt(b)


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

# @app.route("/<servo>/<angle>")
# def move(servo, angle):
# 	global panServoAngle
# 	global tiltServoAngle
# 	if servo == 'pan':
# 		panServoAngle = int(angle)
# 		os.system("python3 angleServoCtrl.py " + str(panPin) + " " + str(panServoAngle))
# 	if servo == 'tilt':
# 		tiltServoAngle = int(angle)
# 		os.system("python3 angleServoCtrl.py " + str(tiltPin) + " " + str(tiltServoAngle))
	
# 	templateData = {
#       'panServoAngle'	: panServoAngle,
#       'tiltServoAngle'	: tiltServoAngle
# 	}

# 	return render_template('index.html', **templateData)

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    
    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                #if q is pressed quit
                break
            if char == ord('p'):
                #if p is pressed take a photo!
                camera.capture('image%s.jpg' % pic)
                pic = pic + 1
                screen.addstr(0, 0, 'picture taken! ')
            elif char == curses.KEY_RIGHT:
                screen.addstr(0, 0, 'right ')
                if b > -90:
                    b = b - 5
                pantilthat.tilt(b)
                time.sleep(0.005)
            elif char == curses.KEY_LEFT:
                screen.addstr(0, 0, 'left ')
                if b < 90:
                    b = b + 5
                pantilthat.tilt(b)
                time.sleep(0.005)
            elif char == curses.KEY_DOWN:
                screen.addstr(0, 0, 'down ')
                if a < 90:
                    a = a + 5
                pantilthat.pan(a) 
                time.sleep(0.005)
            elif char == curses.KEY_UP:
                screen.addstr(0, 0, 'up ')
                if a > -90:    
                    a = a - 5
                pantilthat.pan(a)
                time.sleep(0.005)
            
            
    finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
    


