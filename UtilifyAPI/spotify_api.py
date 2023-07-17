import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import hashlib

load_dotenv()

# Replace with your own Spotify API credentials
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Create a Spotify client with credentials
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def find_track(track_name):
    try:
        tracks = []
        for item in spotify.search(track_name)['tracks']['items']:
            track_id = item['id']
            audio_features = get_track_info(track_id)
            if audio_features is not None:
                track_item = track_data_beautify(item, audio_features)
                tracks.append(track_item)
    except Exception as e:
        print(e)
        raise Exception('Track not found')
    return tracks

def get_playlist_tracks(playlist_id):
    try:
        tracks = []
        for item in spotify.playlist_tracks(playlist_id)['items']:
            track = item['track']
            track_id = track['id']
            audio_features = get_track_info(track_id)
            track_item = track_data_beautify(track, audio_features)
            tracks.append(track_item)
    except Exception as e:
        print(e)
        raise Exception('Playlist not found')
    return tracks

def get_track(track_id):
    try:
        track = spotify.track(track_id)
        audio_features = get_track_info(track_id)
        track_item = track_data_beautify(track, audio_features)
    except Exception as e:
        raise Exception('Track not found')
    return track_item

def track_data_beautify(track, audio_features):
    track_artists = [artist['name'] for artist in track['artists']]
    track_hash = hashlib.md5(str(track['name'] + ' - ' + ", ".join(track_artists)).lower().encode()).hexdigest()
    return {
            'track_id':track['id'],
            'track_name':track['name'],
            'track_artists':track_artists,
            'release_date':track['album']['release_date'],
            'danceability': audio_features['danceability'],
            'energy': audio_features['energy'],
            'tempo': audio_features['tempo'],
            'key': audio_features['key'],
            'loudness': audio_features['loudness'],
            'mode': audio_features['mode'],
            'speechiness': audio_features['speechiness'],
            'acousticness': audio_features['acousticness'],
            'instrumentalness': audio_features['instrumentalness'],
            'liveness': audio_features['liveness'],
            'valence': audio_features['valence'],
            'tags': [audio_features['danceability'], audio_features['energy'], audio_features['tempo'], audio_features['key'], audio_features['loudness'], audio_features['mode'], audio_features['speechiness'], audio_features['acousticness'], audio_features['instrumentalness'], audio_features['liveness'], audio_features['valence']],
            'hash': track_hash,
            'image_url':track['album']['images'][0]['url']
        }

def get_track_info(track_id):
    try:
        # Retrieve audio features for each track
        audio_features = spotify.audio_features(track_id)[0]
        if audio_features is None:
            return None
    except Exception as e:
        raise Exception('Track not found')
    return {
        'danceability': audio_features['danceability'],
        'energy': audio_features['energy'],
        'tempo': audio_features['tempo'],
        'key': audio_features['key'],
        'loudness': audio_features['loudness'],
        'mode': audio_features['mode'],
        'speechiness': audio_features['speechiness'],
        'acousticness': audio_features['acousticness'],
        'instrumentalness': audio_features['instrumentalness'],
        'liveness': audio_features['liveness'],
        'valence': audio_features['valence'],
    }