import json
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=5)
future = None

playlist = []

def add_track(track):
    if track not in playlist:
        playlist.append(track)

def remove_track(track):
    if track in playlist:
        playlist.remove(track)

def save_playlist(playlist_name):
    global future
    future = pool.submit(sv_playlist, playlist_name)

def sv_playlist(playlist_name):
    with open(f'./playlists/{playlist_name}.ufy', 'w') as f:
        json.dump(playlist, f)
        f.close()

def load_playlist(path):
    with open(path.replace('\\', '/'), 'r') as f:
        data = json.load(f)
        for track in data:
            add_track(track)
        f.close()