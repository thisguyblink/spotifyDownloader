from pytube import YouTube
import requests
from requests import post
import base64
import json
import os

# IMPORTANT Global Variables 
# Working is Testing API Calls
clientID = "3b1a8a6de53546518ff043f646ad21b9"
    # Refreshed on 1/16/24
clientSecret = "561e8751d1f6479eb7f5f276c82be96f"
# Test link to be used later
playlist_link = "https://open.spotify.com/playlist/2lBQEVNJIvSMT7q3T0GtZ8?si=e54c6c63d7a146ee"

# Making variables to be global bc they are used in different functions
playlist_id = " "
token = " "
track_id_list = []
videoID = " "


# Youtube Data API 3 key AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs
# Youtube Api being used to get video id from search
def getYT(search):
    api_url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs&part=snippet&q={}r&type=video'
    api_url = api_url.format(search)
    data = requests.get(api_url)
    results = data.json()
    videoID = results['items'][0]['id']['videoId']

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
    encoded = base64.b64encode((clientID + ":" + clientSecret).encode("ascii")).decode("ascii")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded
    }
 
    payload = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)
    json_response = json.loads(response.content)
    token = json_response["access_token"]
    return(token)
    

# function to get list of songs and artists from playlist
def getAuthHeader(token):
    return {"Authorization": "Bearer " + token}

def getTrackIDS(token, link): 
    # Spotify api setup and authentication
    playlist_url = "https://api.spotify.com/v1/playlists/"
    headers = getAuthHeader(token)
    
    playlist_id = link.split("playlist/")[1]
    head, sep, tail = playlist_id.partition("?")
    playlist_id = head
    query_url = playlist_url + playlist_id + "/tracks"
    offset = 0
    total = 0
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)
    total_songs = 0
    num_tracks = json_result['total']
    loop = int(num_tracks / 50)
    if num_tracks % 50 > 1:
        loop += 1
    for i in range(loop): # loop through requests 50 at a time while adding to offset
        query_url + "?limit=50&offset={}"
        query_url.format(offset)
        result = requests.get(query_url, headers=headers)
        json_result = json.loads(result.content)
        for j in range(50):
            if num_tracks > 0:
                track_id_list.append(json_result['items'][j]['track']['id'])
                num_tracks -= 1
                total_songs += 1
        head, sep, tail = query_url.partition("?")
        query_url = head
        offset += 50
        
def trackSearch():
    

        
        
getTrackIDS(token, playlist_link)
        
trackSearch()    

def main():
    token = getSpotifyToken()
    getTrackIDS(token, playlist_link)
    for 
    return 0