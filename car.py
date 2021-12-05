from flask import Flask, render_template, Response, request
import time
import threading
import os

import requests


app = Flask(__name__)

@app.route('/')
def index():
  status_code = flask.Response(status=201)
	return status_code
