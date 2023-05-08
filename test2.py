import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import tkinter as tk

from dotenv import load_dotenv
import os

load_dotenv()

# Replace the following with your own Spotify API credentials
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# Authenticate the application with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define a function to recommend a random track based on specific criteria
def recommend_track(genre, tempo_range, energy_level, danceability):
    # Search for tracks that match the specified genre
    query = f"genre:{genre}"
    tracks = sp.search(q=query, type='track', limit=50)['tracks']['items']

    # Retrieve audio features for each track
    track_ids = [track['id'] for track in tracks]
    audio_features = sp.audio_features(track_ids)
    print(track_ids)

    # Filter tracks based on audio features
    filtered_tracks = []
    for i in range(len(tracks)):
        if tempo_range[0] <= audio_features[i]['tempo'] <= tempo_range[1] \
            and audio_features[i]['energy'] >= energy_level \
            and audio_features[i]['danceability'] >= danceability:
            filtered_tracks.append(tracks[i])
    
    if not filtered_tracks:
        print("No tracks found.")
        return None
    
    # Select a random track from the filtered results
    track = random.choice(filtered_tracks)
    
    # Return the track name, artist name, and Spotify URI
    return track

# Define a function to search for tracks by keyword
def search_tracks(query):
    # Search for tracks based on the query
    results = sp.search(q=query, type='track', limit=50)
    
    # Return a list of track names and Spotify URIs
    return [(track['name'], track['uri']) for track in results['tracks']['items']]

def recommend_button_click():
    # Get the user input values
    genre = genre_entry.get()
    tempo_min = int(tempo_entry.get())
    tempo_max = int(tempo_entry2.get())
    energy_level = int(energy_entry.get())
    danceability = float(dance_entry.get())
    # Call the recommend_tracks function to get a recommendation
    recommendation = recommend_track(genre, [tempo_min, tempo_max], energy_level, danceability)
    if recommendation:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Recommended track:\n" + recommendation)
    else:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "No matching tracks found.")


def search_button_click():
    # Get the user input value
    query = search_entry.get()
    # Call the search_tracks function to get a list of matching tracks
    results = search_tracks(query)
    # Display the results in the text widget
    result_text.delete('1.0', tk.END)
    if len(results) > 0:
        result_text.insert(tk.END, "Matching tracks:\n")
        for track in results:
            result_text.insert(tk.END, track + "\n")
    else:
        result_text.insert(tk.END, "No matching tracks found.")


# Create the main window
root = tk.Tk()
root.title("Music Recommendation Bot")
root.geometry("500x400")

# Set up the layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(6, weight=1)

# Create the input fields
genre_label = tk.Label(root, text="Genre:")
genre_label.grid(row=0, column=0, sticky='w')
genre_entry = tk.Entry(root)
genre_entry.grid(row=0, column=1, columnspan=2)

tempo_label = tk.Label(root, text="Tempo range (BPM):")
tempo_label.grid(row=1, column=0, sticky='w')
tempo_entry = tk.Entry(root, width=5)
tempo_entry.grid(row=1, column=1, sticky='w')
tempo_dash = tk.Label(root, text="-")
tempo_dash.grid(row=1, column=1)
tempo_entry2 = tk.Entry(root, width=5)
tempo_entry2.grid(row=1, column=2, sticky='w')

energy_label = tk.Label(root, text="Energy level:")
energy_label.grid(row=2, column=0, sticky='w')
energy_entry = tk.Entry(root, width=5)
energy_entry.grid(row=2, column=1, columnspan=2, sticky='w')

dance_label = tk.Label(root, text="Danceability:")
dance_label.grid(row=3, column=0, sticky='w')
dance_entry = tk.Entry(root, width=5)
dance_entry.grid(row=3, column=1, columnspan=2, sticky='w')

search_button = tk.Button(root, text="Search", command=search_button_click)
search_button.grid(row=4, column=0, sticky='w')

recommend_button = tk.Button(root, text="Recommend", command=recommend_button_click)
recommend_button.grid(row=4, column=1, columnspan=2, sticky='e')

result_text = tk.Text(root, height=10, width=60)
result_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

genre_label.config(font=("Arial", 12))
genre_entry.config(font=("Arial", 12))
tempo_label.config(font=("Arial", 12))
tempo_entry.config(font=("Arial", 12))
tempo_dash.config(font=("Arial", 12))
tempo_entry2.config(font=("Arial", 12))
energy_label.config(font=("Arial", 12))
energy_entry.config(font=("Arial", 12))
dance_label.config(font=("Arial", 12))
dance_entry.config(font=("Arial", 12))
search_button.config(font=("Arial", 12))
recommend_button.config(font=("Arial", 12))
result_text.config(font=("Arial", 12))

root.mainloop()