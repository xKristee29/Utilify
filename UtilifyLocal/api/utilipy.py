import requests as req
import json
import urllib

url = 'https://utilifyapi.fly.dev/'


def find_track(track_name: str):
    return req.get(url + 'find_track/' + track_name).json()


def recommend_by_track(track_id: str, limit: int = 6):
    return req.get(url + 'recommend_by_track/' + track_id + '?limit=' + str(limit)).json()


def recommend_random(limit: int = 6):
    return req.get(url + 'recommend_random/?limit=' + str(limit)).json()


def add_playlist(playlist: str):
    if len(playlist) > 25:
        playlist_id = playlist.split('/')[-1].split('?')[0]
    else:
        playlist_id = playlist
    return req.get(url + 'add_playlist/' + playlist_id).json()


def add_track(track_id: str):
    return req.get(url + 'add_track/' + track_id).json()


def get_track(track_id: str):
    return req.get(url + 'get_track/' + track_id).json()


def get_tracks_by_criteria(danceability: int = 20, energy: int = 40, tempo_min: int = 30, tempo_max: int = 300, limit: int = 6):
    return req.get(url + 'get_tracks_by_criteria/?' +
                   'danceability=' + str(danceability) +
                   '&energy=' + str(energy) +
                   '&tempo_min=' + str(tempo_min) +
                   '&tempo_max=' + str(tempo_max) +
                   '&limit=' + str(limit)).json()
