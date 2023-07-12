from nicegui import ui
import spotify_dl as sd
from scraper import search_tracks
import querydb as db

tracks = ['2PMxsrSS8vEy9AXeluXxNs','3SB1JqZVZ8vpDxSZzddiEO','7cih8FnEEwMlz9usWRaqwt','2NkCMAUYhqN8recETFVU2m','6VNjk0H51mnGgluivFZhQ2','5dBvUkplYBBBb3sJ2VORQy','4MnRwi9CzuRf947lKlxsVc']

track_elems = {}

result_container = None

def results():
    global track_elems
    track_elems={}
    for track in tracks:
        add_track(track)

def add_track(track):
    global result_container
    global track_elems
    with result_container:
        with ui.row().classes('flex justify-center items-center') as track_row:
            ui.html(f'<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/{track}?utm_source=generator" height="80" width="500" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>')
            track_elems[track_row]=track
            with ui.row().classes('flex justify-center items-center'):
                ui.button('',on_click=lambda:download_row(track_row)).props('flat color=primary icon=file_download')
                ui.button('',on_click=lambda:like(track_row)).props('flat color=primary icon=thumb_up')
                ui.button('',on_click=lambda:dislike(track_row)).props('flat color=primary icon=thumb_down')

def download_row(track_row):
    track=track_elems[track_row]
    sd.spotify_download(track)

def like(track_row):
    track_id=track_elems[track_row]
    db.insert_track(track_id,1.0)
    ui.notify('Liked! Track ID: '+track_elems[track_row])

def dislike(track_row):
    track_id=track_elems[track_row]
    db.insert_track(track_id,0.0)
    ui.notify('Disliked! Track ID: '+track_elems[track_row])

def initSearchPage():
    global container
    with ui.element('div').classes('flex justify-around space-x-1 text-xl min-h-screen min-w-full'):
        with ui.column().classes('items-center p-4 space-y-3 m-0 min-w-full') as container:
            with ui.card().classes('flex flex-row items-center justify-center w-full from-gray-800 to-gray-600 bg-gradient-to-r'):
                global query
                query = ui.input(label='Caută').on('keydown.enter', on_search).style('width: 80%;')
                ui.button('', on_click=on_search).props('flat color=primary icon=search')

def on_search():
    global result_container
    global tracks
    tracks = search_tracks(query.value)
    if result_container == None:
        with container:
            result_container = ui.column().classes('p-2 space-y-2 mt-10')
    result_container.clear()
    results()