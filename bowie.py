import spotipy
import spotipy.oauth2 as oauth2
import tweepy
import random

# Spotify Data

client_id = "XXXX"
client_secret = "XXXX"

credentials = oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

# Twitter Data

consumer_key = "XXXX"
consumer_secret = "XXXX"
access_token = "XXXX"
access_token_secret = "XXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Select a Bowie ID from Spotify

bowie_uri = 'spotify:artist:0oSGxfWSnnOXhD2fKuz2Gy'

# Grab all the Bowie Albums

bowie_albums = spotify.artist_albums(bowie_uri)

# Collect all the albums URIs in a variable and then choice one of them randomly

album_uris = []

for i in range(len(bowie_albums['items'])):
    album_uris.append(bowie_albums['items'][i]['uri'])

random_album = random.choice(album_uris)

# Grab all the songs of the random album, and extract the name and the link to Spotify

album_songs = []

songs = spotify.album_tracks(random_album)

for song in songs['items']:
    album_songs.append('Escuchá a David Bowie. Dale play a ' + song['name'] + ' ' + str(song['external_urls']['spotify']))

# Publish a tweet of a random song from the random album of David Bowie

api.update_status(status=random.choice(album_songs))
