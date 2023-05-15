import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your own Spotify API credentials
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Create a Spotify client with credentials
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_tracks(query):
    # Search for tracks based on the query
    results = spotify.search(q=query, type='track', limit=20)['tracks']['items']
    return [track['id'] for track in results]

def recommend_tracks(genre, tempo_range, energy_level, danceability, popularity, keywords):
    # Search for tracks that match the specified genre
    query = f"{keywords} genre:{genre}"
    tracks = spotify.search(q=query, type='track', limit=50)['tracks']['items']

    # Retrieve audio features for each track
    track_ids = [track['id'] for track in tracks]
    audio_features = spotify.audio_features(track_ids)

    # Filter tracks based on audio features
    filtered_tracks = []
    for i in range(len(tracks)):
        if tempo_range[0] <= audio_features[i]['tempo'] <= tempo_range[1] \
            and audio_features[i]['energy'] >= energy_level \
            and audio_features[i]['danceability'] >= danceability \
                and tracks[i]['popularity'] >= popularity:
            filtered_tracks.append(tracks[i])
    
    if not filtered_tracks:
        print("No tracks found.")
        return None
    
    # Return the track name, artist name, and Spotify URI
    return [track['id'] for track in filtered_tracks]

def get_track_info(track_id):
    # Retrieve track information
    track = spotify.track(track_id)
    artist = track['artists'][0]['name']
    name = track['name']

    # Retrieve audio features
    audio_features = spotify.audio_features(track_id)[0]
    tempo = audio_features['tempo']
    energy = audio_features['energy']
    danceability = audio_features['danceability']
    popularity = track['popularity']

    return artist, name, tempo, energy, danceability, popularity