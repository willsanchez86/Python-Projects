import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100'
SPOTIFY_CLIENT_ID = '5d42a7c53d7a490e8709dcc53fc8b983'
SPOTIFY_CLIENT_SECRET = '294dcdf526f949b8972081248a6ab1bf'


#---------------------------------------------BILLBOARD TOP 100--------------------------------------------------------#
# Retrieve desired date from user
date_input = input("What date would you like to travel to? Enter with YYYY-MM-DD format: ")
year = date_input[:4]

response = requests.get(f'{BILLBOARD_URL}/{date_input}')
webpage = response.text
# Retrieve top 100 songs for entered date and store into 3 lists
soup = BeautifulSoup(webpage, 'html.parser')
ranks = [rank.getText() for rank in soup.find_all(name='span', class_='chart-element__rank__number')]
songs = [song.getText() for song in soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')]
artists = [artist.getText() for artist in soup.find_all(name='span', class_='chart-element__information__artist text--truncate color--secondary')]

#-----------------------------------------------SPOTIFY--------------------------------------------------------------#
scope = 'playlist-modify-private'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

#Retrieve all available uris for each song
ssong = songs[3].replace(' ', '%20')
search = sp.search(q=f"track:{ssong} year:{year}", type="track")
uri = search["tracks"]["items"][0]["uri"]
print(uri)

song_uri_list = []
for song in songs:
    encoded = song.replace(' ', '%20')
    result = sp.search(q=f"track:{encoded} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri_list.append(uri)
    except IndexError:
        print(f'{song} is not available on Spotify')


#Create Playlist
playlist_name = f'{date_input} Billboard 100'
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f'Top 100 Billboard songs on {date_input}'
)

#Add songs to playlist
sp.user_playlist_add_tracks(
    user=user_id,
    playlist_id=playlist['id'],
    tracks=song_uri_list,
)