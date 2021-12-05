from flask import Flask, render_template, Response, request
import time
import threading
import os

import requests


app = Flask(__name__)

@app.route('/')
def index():
    return "Yeah", 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
