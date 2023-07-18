import os
from concurrent.futures import ThreadPoolExecutor
import notifier

pool = ThreadPoolExecutor(max_workers=5)
future = None

def spotify_download(data, started = lambda: notifier.notify('Download started'), finished = lambda: notifier.notify('Download finished')):
    global future
    if len(data) > 25:
        future = pool.submit(download_url, data, started, finished)
    else:
        future = pool.submit(download_track, data, started, finished)

def download_track(track_id, started, finished):
    started()
    os.system(f"cd downloads && spotdl https://open.spotify.com/track/{track_id} --overwrite skip --audio slider-kz piped youtube-music soundcloud --format mp3 --restrict ascii --simple-tui --log-level NOTSET")
    finished()

def download_url(url, started, finished):
    started()
    os.system(f"cd downloads && spotdl {url} --overwrite skip --audio slider-kz piped youtube-music soundcloud --threads 10 --format mp3 --restrict ascii --simple-tui --log-level NOTSET")
    finished()