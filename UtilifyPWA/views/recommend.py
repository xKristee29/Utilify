import flet as ft
from modules.song_info import SongInfo
from modules.song_tile import SongTile
from api import utilipy as up

saved_tracks = []

def Recommend(page: ft.Page):
    
    def search(e):
        saved_tracks.clear()
        search_results.controls = [ft.ProgressBar(color=ft.colors.BLUE_600)]
        search_results.update()
        search_results.controls = []
        for track in up.get_tracks_by_criteria(int(energy_field.value),int(danceability_field.value),int(tempo_min_field.value),int(tempo_max_field.value)):
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
    
    def surprise(e):
        saved_tracks.clear()
        search_results.controls = [ft.ProgressBar(color=ft.colors.BLUE_600)]
        search_results.update()
        search_results.controls = []
        for item in up.recommend_random():
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
        song_info.controls = [SongInfo(track=track,close=close),ft.Container(height=2e9)]
        if not song_info.visible:
            song_info.visible = not song_info.visible
        song_info.update()
        page.update()

    energy_field = ft.TextField(label='Energie',multiline=False,value='20')
    danceability_field = ft.TextField(label='Dansabilitate',multiline=False,value='40')
    tempo_min_field = ft.TextField(label='Tempo minim',multiline=False,value='30')
    tempo_max_field = ft.TextField(label='Tempo maxim',multiline=False,value='300')

    search_button = ft.FilledButton(icon='search', text='Caută', height=50, width=140, on_click=search)
    surprise_button = ft.FilledButton(icon='lightbulb', text='Surprinde-mă!', height=50, width=140, on_click=surprise)

    song_info = ft.ListView(
        col={'lg':4},
        visible=False,
        expand=True,
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
                        ft.Column([
                            ft.ResponsiveRow([
                                ft.Container(energy_field, margin=3, col={'xs':6}),
                                ft.Container(danceability_field, margin=3, col={'xs':6}),
                                ft.Container(tempo_min_field, margin=3, col={'xs':6}),
                                ft.Container(tempo_max_field, margin=3, col={'xs':6})
                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ],col={'lg':8}),
                        ft.Column([
                            ft.ResponsiveRow([
                                ft.Container(search_button, margin=3, col={'md':6,'lg':12}),
                                ft.Container(surprise_button, margin=3, col={'md':6,'lg':12})
                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        ],col={'lg':4}),
                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=10
                )
            ),
            ft.Column([search_results])
        ],col={'lg':8},scroll='hidden')
    ],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.START)
    return tab