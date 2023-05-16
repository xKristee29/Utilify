import random
from nicegui import ui
import spotify_dl as sd
import scraper as sc
import querydb as db

genres = ['romanian-pop', 'romanian-rap', 'romanian-trap', 'manele', 'house', 'pop', 'rap', 'trap', 'edm', 'dance', 'latin']

tracks = []

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
    global result_container
    track=track_elems[track_row]
    db.insert_track(track,1.0)
    ui.notify('Liked! Track ID: '+track)
    tracks.remove(track)
    result_container.remove(track_row)
    result_container.update()

def dislike(track_row):
    global result_container
    track=track_elems[track_row]
    db.insert_track(track,0.0)
    ui.notify('Disliked! Track ID: '+track)
    tracks.remove(track)
    result_container.remove(track_row)
    result_container.update()

def initRecommendPage():
    global container
    with ui.element('div').classes('flex justify-around space-x-1 text-xl min-h-screen') as container:
        with ui.column().classes('items-center p-4 space-y-3 m-0'):
            with ui.row().classes('flex-around items-center justify-center'):
                ui.label('Cuvinte cheie:')
                global keywords
                keywords = ui.input(label='').classes("text-xl")

            with ui.row().classes('items-center'):
                ui.label('Gen:')
                global genre
                genre = ui.select(genres, value=genres[0]).classes("text-xl")
            
            with ui.row().classes('items-center justify-center'):
                ui.label('Tempo (BPM) 0-200:')
                global tempo_min
                global tempo_max
                tempo_min = ui.number(label='Min', value=60, format='%i').classes("text-xl w-1/6")
                tempo_max = ui.number(label='Max', value=140, format='%i').classes("text-xl w-1/6")
            
            with ui.row().classes('items-center justify-center'):
                ui.label('Nivel energie 0-100:')
                global energy_level
                energy_level = ui.number(value=60, format='%i').classes("text-xl w-1/6")
            
            with ui.row().classes('items-center justify-center'):
                ui.label('Dansabilitatea 0-100:')
                global danceability
                danceability = ui.number(value=70, format='%i').classes("text-xl w-1/6")
            
            with ui.row().classes('items-center justify-center'):
                ui.label('Popularitate:')
                global popularity
                popularity = ui.number(value=40, format='%i').classes("text-xl w-1/6")
        
            with ui.row().classes('flex-row justify-center items-center p-4 space-y-2'):
                search = ui.button('Caută', on_click=on_search).classes("text-xl")
                search_ai = ui.button('Caută cu AI', on_click=on_search_ai).classes("text-xl")
            

def on_search():
    global result_container
    global tracks
    tracks = sc.recommend_tracks(genre.value, 
                                [float(tempo_min.value), float(tempo_max.value)], 
                                float(energy_level.value) / 100.0, 
                                float(danceability.value) / 100.0, 
                                int(popularity.value),
                                keywords.value)
    if tracks is not None and len(tracks) > 20:
        tracks = random.sample(tracks,20)
    if result_container == None:
        with container:
            result_container = ui.column().classes('p-2 space-y-2 mt-10')
    result_container.clear()
    results()

def on_search_ai():
    global result_container
    global tracks
    tracks = sc.recommend_tracks_ai(genre.value, keywords.value)
    if tracks is not None and len(tracks) > 20:
        tracks = random.sample(tracks,20)
    if result_container == None:
        with container:
            result_container = ui.column().classes('p-2 space-y-2 mt-10')
    result_container.clear()
    results()