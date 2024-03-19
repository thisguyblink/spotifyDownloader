from flask import Flask, render_template, request
from test import *
from static.youtube_downloader import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    playlist = request.form['playlist_name']
    # Execute your Python script here
    # This function will be called when the button is clicked
    # You can put your Python script logic here
    main(playlist)
    return "The playlist for the link " + playlist + "has been downloaded"


    

