import json

playlist = []

def add_track(track):
    if track not in playlist:
        playlist.append(track)

def remove_track(track):
    if track in playlist:
        playlist.remove(track)

def save_playlist(playlist_name):
    with open(f'./playlists/{playlist_name}.ufy', 'w') as f:
        json.dump(playlist, f)

def load_playlist(playlist_name):
    with open(playlist_name, 'r') as f:
        data = json.load(f)
        for track in data:
            add_track(track)