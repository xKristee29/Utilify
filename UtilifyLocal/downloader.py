import os
from concurrent.futures import ThreadPoolExecutor
import notifier
import stores

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
    try:
        os.system(f"cd {stores.settings['download_path']} && spotdl https://open.spotify.com/track/{track_id} --overwrite skip --audio youtube-music soundcloud slider-kz piped --format mp3 --restrict ascii")
        finished()
    except Exception as e:
        notifier.notify('Nu s-a putut descărca: ' + str(e))

def download_url(url, started, finished):
    started()
    try:
        os.system(f"cd {stores.settings['download_path']} && spotdl {url} --overwrite skip --audio youtube-music soundcloud slider-kz piped --threads 20 --format mp3 --restrict ascii")
        finished()
    except Exception as e:
        notifier.notify('Nu s-a putut descărca: ' + str(e))