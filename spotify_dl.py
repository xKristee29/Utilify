import os
from concurrent.futures import ThreadPoolExecutor
from nicegui import ui

pool = ThreadPoolExecutor(max_workers=5)

downids = []
downmap = {}

def spotify_download(track_id):
    global downids
    global downmap
    if track_id in downids:
        return
    downids.append(track_id)
    future = pool.submit(download_track, track_id)
    downmap[track_id] = future
    ui.notify('Downloading track '+track_id)


def download_track(track_id):
    os.system(f'cd downloads && spotdl https://open.spotify.com/track/{track_id} --overwrite skip')

def get_pending():
    global downmap
    global downids
    pending = []
    for track_id in downids:
        if not downmap[track_id].done():
            pending.append(track_id)
    return pending