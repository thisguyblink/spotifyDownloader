from pytube import YouTube
import requests 
import os

# Youtube Data API 3 key AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs
# Youtube Api being used to get video id from search
def getID(song, artist):
    song_name = "Earthquake" 
    artist_name = "Tyler the Creator"
    api_url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs&part=snippet&q={}{}r&type=video'
    api_url = api_url.format(song_name, artist_name)
    data = requests.get(api_url)
    results = data.json()
    videoID = results['items'][0]['id']['videoId']
    return videoID

# pytube used to download video
# use return value of id from the getID function for the num parameter
def downloadVid(num):
    url = "https://www.youtube.com/watch?v=" + num
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    video.download(output_path="/home/patrick/Documents/Downloaded_Songs")

# changing file extensions from mp4 to mp3 
def filesToMp3():
    path = os.chdir("/home/patrick/Documents/Downloaded_Songs")
    for song in os.listdir(path):
        if (song[-3:]== "mp4"):
            old_name = song.removesuffix("mp4")
            new_name = old_name + "mp3"
            os.rename(song, new_name)
            print("Song", old_name, "has been converted to a mp3 file")
            
# function to get list of songs and artists from playlist


