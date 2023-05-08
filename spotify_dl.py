import os

def spotify_download(track_id):
    os.system(f'cd downloads && spotdl https://open.spotify.com/track/{track_id} --overwrite skip')
