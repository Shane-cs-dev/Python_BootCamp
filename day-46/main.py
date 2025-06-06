import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json
from datetime import datetime
#####################
#Spotify information
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
#####################
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
HEADER = json.loads(os.getenv("HEADER"))#convert a JSON-formatted string into a Python dictionary
#####################
#request auth from spotify website
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="./token.txt",
        username="Shane"
    )
)
user_id = sp.current_user()["id"]

#####################
#Define date
today = datetime.now()
formatted_date = today.strftime("%Y-%m-%d")
year = today.year

#Scraping the list from the website
new_url = f"https://www.billboard.com/charts/hot-100/{formatted_date}"
web = requests.get(url=new_url, headers=HEADER)
web_context = web.text
soup = BeautifulSoup(web_context, features="html.parser")
title_tag = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
playlist = [title.getText().strip() for title in title_tag] #Generate Playlist

#Request/Get spotifiy uri
spotify_html = []
spotify_uri_list = []
for song in playlist:
    result = sp.search(q=song, type="track")
    spotify_id = result["tracks"]["items"][0]["uri"]
    spotify_uri = spotify_id.split(":")[2]#Get spotify uri
    try:
        # print(f"{song}/{spotify_uri}")
        spotify_html.append(f"https://open.spotify.com/track/{spotify_uri}")
        spotify_uri_list.append(spotify_id)
    except IndexError:
        print(f"{song} is not found on Spotify")
        pass
# print(spotify_uri_list)

#Create Playlist (Need user_id to create playlist and playlist_id to add songs)
playlist_name = f"Billboard Top 100 {formatted_date}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=spotify_uri_list)




