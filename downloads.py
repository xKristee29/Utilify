from nicegui import ui, app
import spotify_dl as sd
import os
import sys
import glob
from threading import Thread
import time

thread = None

download_path = sys.path[0] + "\\downloads\\"

app.add_static_files('/downloads', 'downloads')

result_container = None


def results():
    global track_elems
    track_elems = {}
    for track in tracks:
        add_track(track)


def add_track(track):
    global result_container
    global track_elems
    with result_container:
        with ui.card().classes('flex-row justify-center items-center w-full') as track_row:
            track_elems[track_row] = track
            with ui.row().classes('flex justify-center items-center w-full'):
                with ui.column().classes('flex justify-center items-center w-9/12'):
                    ui.label(track).classes('text-base')
                    if track.endswith('.mp3'):
                        ui.audio(src='/downloads/' + track,
                                 controls=True).style('width: 100%;')
                with ui.column().classes('flex justify-center items-center w-1/6'):
                    if track.endswith('.mp3'):
                        ui.button('', on_click=lambda: open_explorer(track_row)).props(
                            'flat color=primary icon=file_open').classes('text-base')
                    else:
                        ui.spinner(size='lg')


def open_explorer(track_row):
    global track_elems
    track = track_elems[track_row]
    os.system(f'explorer /select,"{download_path + track}"')


def initDownladPage():
    global container
    with ui.element('div').classes('flex justify-around space-x-1 text-xl min-h-screen min-w-full'):
        with ui.column().classes('items-center p-4 space-y-3 m-0 w-full') as container:
            on_search()

def refresh_search():
    time.sleep(5)
    on_search()

def on_search():
    global result_container
    global tracks
    global thread
    if result_container == None:
        with container:
            result_container = ui.column().classes('p-2 space-y-2 mt-10')
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(download_path, x)),
                           os.listdir(download_path))
    list_of_files = sorted(list_of_files,
                           key=lambda x: os.path.getmtime(
                               os.path.join(download_path, x)),
                           reverse=True)
    downed = []
    for i, track in enumerate(list_of_files):
        if track.endswith('.mp3'):
            downed.append(track)
        if i > 50:
            break
    pending = sd.get_pending()
    tracks = pending + downed
    result_container.clear()
    results()
    if len(pending)>0:
        thread = Thread(target=refresh_search)
        thread.start()
