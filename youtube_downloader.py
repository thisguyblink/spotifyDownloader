from pytube import YouTube
import requests
from requests import post
import base64
import json
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
            
def getSpotifyToken():
    clientID = "3b1a8a6de53546518ff043f646ad21b9"
    clientSecret = "d4021685a5304d259ba0be5de83cb874"
    auth_string = clientID + ":" + clientSecret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic" + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token
spo_token = getSpotifyToken()

# function to get list of songs and artists from playlist
def getAuthHeader(token):
    return {"Authorization" : "Bearer " + token}

#playlist link, red part is playlist id(not inlcuding question mark), used to get song id from playlist,
https://open.spotify.com/playlist/3HtiKiKxFosjLOGbKlX08n?si=cdd07dc532fc4138 

#song link, red part is song id(not inlcuding question mark), used to get song info
https://open.spotify.com/track/4NczzeHBQPPDO0B9AAmB8d?si=e2b96fe20db74e50