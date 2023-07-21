import flet as ft
from modules.song_info import SongInfo2
from modules.song_tile import SongTile
import stores
import sys
import notifier


def Playlist(page: ft.Page):
    
    def close(e):
        song_info.visible = not song_info.visible
        song_info.update()
    
    def remove_track(track):
        stores.remove_track(track)
        search_results.controls = []
        for track in stores.playlist:
            search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=None))
        search_results.update()
        page.update()

    def toggle_song_info(track):
        song_info.controls = [SongInfo2(track=track,close=close,remove_track=remove_track),ft.Container(height=2e9)]
        if not song_info.visible:
            song_info.visible = not song_info.visible
        song_info.update()
        page.update()

    song_info = ft.ListView(
        col={'lg':4},
        visible=False,
        expand=True,
    )
    
    search_results = ft.ListView(expand=True, padding=3)
    for track in stores.playlist:
        search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=None))

    tab = ft.ResponsiveRow([
        song_info,
        ft.Column([
            search_results
        ],col={'lg':8})
    ],alignment=ft.MainAxisAlignment.CENTER)
    return tab