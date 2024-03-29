import flet as ft
from modules.song_info import SongInfo
from modules.song_tile import SongTile
from api import utilipy as up

saved_tracks = []

def Search(page: ft.Page):

    def search(e):
        saved_tracks.clear()
        search_results.controls = [ft.ProgressBar(color=ft.colors.BLUE_600)]
        search_results.update()
        search_results.controls = []
        for track in up.find_track(search_field.value):
            saved_tracks.append(track)
            search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=recommend))
        search_results.update()
        page.update()
    
    def recommend(track_id):
        saved_tracks.clear()
        search_results.controls = [ft.ProgressBar(color=ft.colors.BLUE_600)]
        search_results.update()
        search_results.controls = []
        for item in up.recommend_by_track(track_id):
            track = up.get_track(item['id'])
            saved_tracks.append(track)
            search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=recommend))
            search_results.update()
        search_results.update()
        page.update()
    
    def close(e):
        song_info.visible = not song_info.visible
        song_info.update()

    def toggle_song_info(track):
        song_info.controls = [SongInfo(track=track,close=close,page=page),ft.Container(height=2e9)]
        if not song_info.visible:
            song_info.visible = not song_info.visible
        song_info.update()
        page.update()

    song_info = ft.ListView(
        col={'lg':4},
        visible=False,
        expand=True,
    )

    search_field = ft.TextField(
        label="Caută o melodie",
        multiline=False,
        on_submit=search
    )

    search_button = ft.IconButton(
        icon='search',
        on_click=search
    )

    search_results = ft.Column()

    for track in saved_tracks:
        search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=recommend))

    tab = ft.ResponsiveRow([
        song_info,
        ft.Column([
            ft.Card(
                ft.Container(
                    ft.ResponsiveRow([
                        ft.Container(search_field, col=11),
                        ft.Container(search_button, col=1)
                    ],vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=10
                )
            ),
            ft.Column([search_results])
        ],col={'lg':8},scroll='hidden')
    ],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.START)
    return tab
