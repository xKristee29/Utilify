from fastapi import FastAPI
from music_data import MusicData
import spotify_api as spotify
import database as db
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=100)

app = FastAPI()
music_data = MusicData()

def insert_result(result):
    for track in result:
        db.insert_track(track)
    music_data.update_data()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/find_track/{track_name}')
async def find_track(track_name: str, limit: int = 10):
    result = spotify.find_track(track_name)[:limit]
    insert_result(result)
    return result

@app.get('/find_file/{file_name}')
async def find_file(file_name: str, limit: int = 10):
    result = spotify.find_track(file_name)[:limit]
    return result

@app.get('/recommend_by_track/{track_id}')
async def recommend_by_track(track_id: str, limit: int = 10):
    try:
        track = db.get_track(track_id)
    except Exception as e:
        track = await add_track(track_id)
    print(track)
    if track != {"message": "Track not found"}:
        result = music_data.recommend_by_track(track['hash'], limit)
    else:
        return {"message": "Track not found"}
    return result

@app.get('/recommend_random/')
async def recommend_random(limit: int = 10):
    result = music_data.recommend_random(limit)
    return result

@app.get('/add_playlist/{playlist_id}')
async def add_playlist(playlist_id: str):
    try:
        tracks = spotify.get_playlist_tracks(playlist_id)
    except Exception as e:
        print(e)
        return {"message": "Playlist not found"}
    insert_result(tracks)
    return tracks

@app.get('/add_track/{track_id}')
async def add_track(track_id: str):
    try:
        track = spotify.get_track(track_id)
    except Exception as e:
        print(e)
        return {"message": "Track not found"}
    db.insert_track(track)
    track = db.get_track_by_hash(track['hash'])
    music_data.update_data()
    return track

@app.get('/get_track/{track_id}')
async def get_track(track_id: str):
    try:
        track = db.get_track(track_id)
    except Exception as e:
        track = await add_track(track_id)
    return track

@app.get('/get_tracks_by_criteria/')
async def get_tracks_by_criteria(danceability: int = 20, energy: int = 40, tempo_min: int = 30, tempo_max: int = 300, limit: int = 10):
    tracks = db.get_tracks_by_criteria(danceability, energy, tempo_min, tempo_max)[:limit]
    return tracks