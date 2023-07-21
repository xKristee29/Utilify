
playlist = []

def add_track(track):
    if track not in playlist:
        playlist.append(track)

def remove_track(track):
    if track in playlist:
        playlist.remove(track)