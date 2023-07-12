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

# Define the search query
query = "genre:'romanian-pop'"

# Get the search results
results = spotify.search(q=query, type='track', limit=50)

# Create a CSV file to store the data
with open('music_dataset.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "artist", "tempo", "energy", "danceability", "popularity", "key", "loudness", "instrumentation"])

    # Loop through the search results and extract the relevant data
    for track in results['tracks']['items']:
        track_id = track['id']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        audio_features = spotify.audio_features([track_id])[0]

        tempo = audio_features['tempo']
        energy = audio_features['energy']
        danceability = audio_features['danceability']
        popularity = track['popularity']
        key = audio_features['key']
        loudness = audio_features['loudness']
        instrumentation = audio_features['instrumentalness']

        # Write the data to the CSV file
        writer.writerow([track_id, track_name, artist_name, tempo, energy, danceability, popularity, key, loudness, instrumentation])

print("Dataset collected successfully!")
