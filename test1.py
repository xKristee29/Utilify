import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import random

load_dotenv()

# Replace the following with your own Spotify API credentials
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Authenticate with the Spotify API using the client credentials flow
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def recommend_track(genre, tempo_range, energy_level, danceability, popularity):
    # Search for tracks that match the specified genre
    query = f"genre:{genre}"
    tracks = sp.search(q=query, type='track', limit=50)['tracks']['items']

    # Retrieve audio features for each track
    track_ids = [track['id'] for track in tracks]
    audio_features = sp.audio_features(track_ids)

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
    
    # Select a random track from the filtered results
    track = filtered_tracks
    
    # Return the track name, artist name, and Spotify URI
    return track


# Define a function to search for tracks by artist, title, or keyword
def search_tracks(query):
    # Search for tracks that match the specified query
    tracks = sp.search(q=query, type='track', limit=50)['tracks']['items']
    
    # Return a list of track names and Spotify URIs
    return [(track['name'], track['uri']) for track in tracks]

# Test the functions by recommending a track with a tempo between 120-130 BPM, an energy level of 0.8, and a danceability of 0.6, and searching for tracks by keyword "house"
tracks = recommend_track('romanian-pop',[60,140], 0.6, 0.8,20)

print(tracks[0])