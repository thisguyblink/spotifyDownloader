from pytube import YouTube
import requests
import os

# Youtube Data API 3 key AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs
# Youtube Api being used to get video id from search
result = " "
videoId = "XSbZidsgMfw"
title = "Yonkers"
url = "https://www.youtube.com/watch?v=" + videoId

# pytube used to download video
video = YouTube(url)
video = video.streams.get_highest_resolution()
video.download(output_path="/home/patrick/Documents/Downloaded_Songs")

# changing file extensions from mp4 to mp3 
path = "/home/patrick/Documents/Downloaded_Songs"
