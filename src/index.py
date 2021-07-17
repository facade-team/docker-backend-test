#!/usr/bin/env bash
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!!!!!!!! this is test!!!!!!!!!!'

@app.route('/help')
def help():
    return 'Help is working!'