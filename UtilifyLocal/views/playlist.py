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
    
    def import_playlist(e: ft.FilePickerResultEvent):
        for f in e.files:
            stores.load_playlist(f.path)
        search_results.controls = []
        for track in stores.playlist:
            search_results.controls.append(SongTile(track=track,toggle_song_info=toggle_song_info,recommend=None))
        page.update()
    
    def save_playlist(e):
        if name_field.value != '':
            stores.save_playlist(name_field.value)
        notifier.notify('Playlist salvat cu succes!')

    
    page.file_picker.on_result = import_playlist

    name_field = ft.TextField(label='Nume playlist',multiline=False)

    save_button = ft.FilledButton(icon='save', text='Salvează playlist', height=50, width=140, on_click=save_playlist)
    import_button = ft.FilledButton(
        icon='upload',
        text='Încarcă playlist',
        height=50,
        width=140,
        on_click=lambda e: page.file_picker.pick_files(
            allow_multiple=True,
            allowed_extensions=['ufy'],
            initial_directory=stores.settings['playlist_path']
        )
    )

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
            ft.Card(
                ft.Container(
                    ft.ResponsiveRow([
                            ft.Container(name_field, margin=3, col={'lg':6}),
                            ft.Container(save_button, margin=3, col={'md':6,'lg':3}),
                            ft.Container(import_button, margin=3, col={'md':6,'lg':3})
                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=10
                )
            ),
            ft.Column([search_results])
        ],col={'lg':8},scroll='hidden')
    ],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.START)
    return tab