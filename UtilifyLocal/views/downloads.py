import flet as ft
from modules.song_info import SongInfo
from modules.song_tile import SongTile
from api import utilipy as up
import downloader as dl
import os
import sys
from concurrent.futures import ThreadPoolExecutor
import stores
import notifier

pool = ThreadPoolExecutor(max_workers=5)

def Downloads(page: ft.Page):
    global pool

    def search():
        download_path = stores.settings['download_path']

        try:
            list_of_files = filter(lambda x: os.path.isfile(os.path.join(download_path, x)),
                                os.listdir(download_path))
            list_of_files = sorted(list_of_files,
                                key=lambda x: os.path.getmtime(
                                    os.path.join(download_path, x)),
                                reverse=True)
            
            list_of_files = [track.replace(".mp3","") for track in list_of_files if track.endswith(".mp3")]

            for track in list_of_files:
                search_results.controls.append(SongTile(track=up.find_track(track)[0],toggle_song_info=toggle_song_info))
                search_results.update()
        except Exception as e:
            notifier.notify('Nu s-a putut încărca lista de melodii descărcate: ' + str(e))

    def download(e):
        playlist_id = url_field.value.split('playlist/')[-1].split('?')[0]
        track_id = url_field.value.split('track/')[-1].split('?')[0]
        dl.spotify_download(url_field.value)
        if len(playlist_id) < 25:
            pool.submit(up.add_playlist, playlist_id)
        else:
            pool.submit(up.add_track, track_id)
    
    def close(e):
        song_info.visible = not song_info.visible
        song_info.update()

    def toggle_song_info(track):
        song_info.controls = [SongInfo(track=track,close=close),ft.Container(height=2e9)]
        if not song_info.visible:
            song_info.visible = not song_info.visible
        song_info.update()
        page.update()

    song_info = ft.ListView(
        col={'lg':4},
        visible=False,
        expand=True,
    )

    url_field = ft.TextField(
        label="Descarcă de pe Spotify (URL)",
        multiline=False,
        on_submit=download
    )

    down_button = ft.IconButton(
        icon='download',
        on_click=download
    )

    search_results = ft.ListView(expand=True, padding=3)

    tab = ft.ResponsiveRow([
        song_info,
        ft.Column([
            ft.Card(
                ft.Container(
                    ft.ResponsiveRow([
                        ft.Container(url_field, col=11),
                        ft.Container(down_button, col=1)
                    ],vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=10
                )
            ),
            search_results
        ],col={'lg':8})
    ],alignment=ft.MainAxisAlignment.CENTER)

    pool.submit(search)
    return tab