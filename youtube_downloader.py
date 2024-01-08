from pytube import YouTube
import requests 
import os

# Youtube Data API 3 key AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs
# Youtube Api being used to get video id from search
data = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs&part=snippet&q=Yonkers Tyler the Creator&type=video')
results = data.json()
videoID = results['items'][0]['id']['videoId']
print(videoID)
title = "Yonkers"
url = "https://www.youtube.com/watch?v=" + videoID

# pytube used to download video
video = YouTube(url)
video = video.streams.get_highest_resolution()
video.download(output_path="/home/patrick/Documents/Downloaded_Songs")

# changing file extensions from mp4 to mp3 
def filesToMp3():
    path = os.chdir("/home/patrick/Documents/Downloaded_Songs")
    for song in os.listdir(path):
        old_name = song.removesuffix("mp4")
        new_name = song + "mp3"
        os.rename(song, new_name)
        print("Song", old_name, "has been converted to a mp3 file")

