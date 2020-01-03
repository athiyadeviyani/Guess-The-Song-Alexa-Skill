import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


import random

client_credentials_manager = SpotifyClientCredentials(client_id='864a99997b1f464ca1c9d7b85683d26f', client_secret='083eab0e748841e8a989eca507f71f56')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_tracks = sp.user_playlist_tracks('athiyadee', playlist_id='10c4HJIeBPkC2vO7wZlin7', fields=None, limit=100, offset=0, market=None)

results = sp.user_playlist('1221028518', '2YRe7HRKNRvXdJBp9nXFza', fields="tracks,next")
tracks = results['tracks']

songs = []

def get_songs(tracks):
    
    for i, item in enumerate(tracks['items']):
        track = item['track']
        url = track['preview_url']
        artist = track['artists'][0]['name']
        name = track['name']
        if url != None:
           # print(str(i) + " - " + artist + " - " + name)
            #print(url)
            song = []
            song.append(name)
            song.append(artist)
            song.append(url)
            #print(song)
        
            songs.append(song)

    return songs


allsongs = get_songs(tracks)

def get_random_song():
    i = random.randint(1,len(allsongs))
    return allsongs[i]
        







