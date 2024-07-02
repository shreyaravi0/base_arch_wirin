import json
from dotenv import load_dotenv
import os
import base64
import requests

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        json_result = response.json()
        token = json_result.get("access_token")
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error fetching token: {e}")
        return None
    except KeyError as e:
        print(f"KeyError: {e}")
        return None

def get_headers(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_headers(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query

    try:
        response = requests.get(query_url, headers=headers)
        response.raise_for_status()
        json_result = response.json()
        artists = json_result["artists"]["items"]
        if artists:
            return artists[0] # Return the first artist found
        else:
            print("Artist not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error searching for artist: {e}")
        return None

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_headers(token)

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        json_result = response.json()
        tracks = json_result["tracks"]
        song_details = [{"name": track["name"], "url": track["external_urls"]["spotify"]} for track in tracks]
        return song_details
    except requests.exceptions.RequestException as e:
        print(f"Error fetching top tracks: {e}")
        return None

token = get_token()
if token:
    print(f"Token: {token}")
    artist_name = input("Enter artist name to be searched: ")
    artist = search_for_artist(token, artist_name)

    if artist:
        artist_id = artist["id"]
        songs = get_songs_by_artist(token, artist_id)

        if songs:
            for idx, song in enumerate(songs):
                print(f"{idx+1}. {song['name']} - {song['url']}")
        else:
            print("No songs found.")
else:
    print("Failed to retrieve token.")