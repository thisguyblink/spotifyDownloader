from flask import Flask, render_template, request
from test import *
from youtube_downloader import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    playlist = request.form['playlist_name']
    main(playlist)
    return "The playlist for the link " + playlist + "has been downloaded"


    

