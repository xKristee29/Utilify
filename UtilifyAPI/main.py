from fastapi import FastAPI
from music_data import MusicData
import spotify_api as spotify
import database as db

app = FastAPI()
music_data = MusicData()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/recommend_by_track/{track_id}')
async def recommend_by_track(track_id: str, limit: int = 10):
    try:
        track = db.get_track(track_id)
    except Exception as e:
        track = await add_track(track_id)
    if track != {"message": "Track not found"}:
        result = music_data.recommend_by_track(track_id, limit)
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
    for track in tracks:
        db.insert_track(track)
    music_data.update_data()
    return tracks

@app.get('/add_track/{track_id}')
async def add_track(track_id: str):
    try:
        track = spotify.get_track(track_id)
    except Exception as e:
        print(e)
        return {"message": "Track not found"}
    db.insert_track(track)
    music_data.update_data()
    return track

@app.get('/get_track/{track_id}')
async def get_track(track_id: str):
    try:
        track = db.get_track(track_id)
    except Exception as e:
        track = await add_track(track_id)
    return track