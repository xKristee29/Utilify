import flet as ft
from modules.song_info import SongInfo
from modules.song_tile import SongTile
import stores
import sys
import notifier

def Playlist(page: ft.Page):
    
    def close(e):
        song_info.visible = not song_info.visible
        song_info.update()
    
    def update_list():
        search_results.controls = []
        for track in stores.playlist:
            search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=None))
        search_results.update()
        page.update()

    def toggle_song_info(track):
        song_info.controls = [SongInfo(track=track,close=close,update_list=update_list),ft.Container(height=2e9)]
        if not song_info.visible:
            song_info.visible = not song_info.visible
        song_info.update()
        page.update()

    song_info = ft.ListView(
        col={'lg':4},
        visible=False,
        expand=True,
    )
    
    search_results = ft.Column()
    
    for track in stores.playlist:
        search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=None))

    tab = ft.ResponsiveRow([
        song_info,
        ft.Column([
            search_results
        ],col={'lg':8},scroll='hidden')
    ],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.START)
    return tab