import json
import sys
import os
import notifier

playlist = []
search_result_delta = 520

try:
    os.mkdir('./downloads')
except FileExistsError:
    pass

try:
    os.mkdir('./playlists')
except FileExistsError:
    pass

try:
    f = open('settings.ufy','r')
except FileNotFoundError:
    f = open('settings.ufy','w')
    f.write('{"playlist_path":"./playlists","download_path":"./downloads"}')
    f.close()
    f = open('settings.ufy','r')

settings = json.load(f)

def save_settings(download_path, playlist_path):
    change_download_path(download_path)
    change_playlist_path(playlist_path)

def change_playlist_path(path):
    f = open('settings.ufy','w')
    settings['playlist_path'] = path.replace("\\","/")
    if settings['playlist_path'][-1] == '/':
        settings['playlist_path'] = settings['playlist_path'][:-1]
    json.dump(settings, f)
    f.close()

def change_download_path(path):
    f = open('settings.ufy','w')
    settings['download_path'] = path.replace("\\","/")
    if settings['download_path'][-1] == '/':
        settings['download_path'] = settings['download_path'][:-1]
    json.dump(settings, f)
    f.close()

def add_track(track):
    if track not in playlist:
        playlist.append(track)

def remove_track(track):
    if track in playlist:
        playlist.remove(track)

def save_playlist(playlist_name):
    try:
        with open(f'{settings["playlist_path"]}/{playlist_name}.ufy', 'w') as f:
            json.dump(playlist, f)
            f.close()
    except Exception as e:
        notifier.notify(f'Playlist-ul nu a putut fi salvat: {str(e)}')
        raise e

def load_playlist(path):
    try:
        with open(path.replace('\\', '/'), 'r') as f:
            data = json.load(f)
            for track in data:
                add_track(track)
            f.close()
    except Exception as e:
        notifier.notify(f'Playlist-ul nu a putut fi încărcat: {str(e)}')