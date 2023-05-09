import random
from nicegui import ui
from spotify_dl import spotify_download
from scraper import recommend_tracks

genres = ['romanian-pop','romanian-rap','manele','romanian-trap']

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
    spotify_download(track)

def like(track_row):
    global result_container
    track=track_elems[track_row]
    ui.notify('Liked! Track ID: '+track)
    tracks.remove(track)
    result_container.remove(track_row)
    result_container.update()

def dislike(track_row):
    global result_container
    track=track_elems[track_row]
    ui.notify('Disliked! Track ID: '+track)
    tracks.remove(track)
    result_container.remove(track_row)
    result_container.update()

def initRecommendPage():
    global container
    with ui.element('div').classes('flex justify-around space-x-1 text-xl min-h-screen') as container:
        with ui.column().classes('items-center p-4 space-y-3 m-0'):
            with ui.row().classes('items-center justify-center'):
                ui.label('Cuvinte cheie:')
                global keywords
                keywords = ui.input(label='')

            with ui.row().classes('items-center'):
                ui.label('Gen:')
                global genre
                genre = ui.select(genres, value=genres[0])
            
            with ui.row().classes('items-center'):
                ui.label('Tempo (BPM) 0-200:')
                global tempo_min
                global tempo_max
                tempo_min = ui.number(label='Min', value=60, format='%i')
                tempo_max = ui.number(label='Max', value=140, format='%i')
            
            with ui.row().classes('items-center'):
                ui.label('Nivel energie 0-100:')
                global energy_level
                energy_level = ui.number(value=60, format='%i')
            
            with ui.row().classes('items-center'):
                ui.label('Dansabilitatea 0-100:')
                global danceability
                danceability = ui.number(value=70, format='%i')
            
            with ui.row().classes('items-center'):
                ui.label('Popularitate:')
                global popularity
                popularity = ui.number(value=40, format='%i')
        
            with ui.row().classes('justify-center p-4 space-y-2'):
                search = ui.button('Caută', on_click=on_search)
            

def on_search():
    global result_container
    global tracks
    tracks = recommend_tracks(genre.value, 
                                [float(tempo_min.value), float(tempo_max.value)], 
                                float(energy_level.value) / 100.0, 
                                float(danceability.value) / 100.0, 
                                int(popularity.value),
                                keywords.value)
    if len(tracks) > 20:
        tracks = random.sample(tracks,20)
    if result_container == None:
        with container:
            result_container = ui.column().classes('p-2 space-y-2 mt-10')
    result_container.clear()
    results()