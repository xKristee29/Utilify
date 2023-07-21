import flet as ft
from colors import radom_color
import stores
import downloader as dl

def SongInfo(close, track, update_list = lambda: None):

    def update(e):
        modify_playlist()
        update_list()

    def modify_playlist():
        if track not in stores.playlist:
            stores.add_track(track)
            edit_playlist_button.content = ft.FilledButton(
                text='Șterge din playlist',
                height=50,
                icon='delete_forever',
                on_click=update
            )
        else:
            stores.remove_track(track)
            edit_playlist_button.content = ft.FilledButton(
                text='Adaugă în playlist', 
                height=50, 
                icon='queue_music',  
                on_click=update
            )
        edit_playlist_button.update()

    edit_playlist_button = ft.Container(col=6)

    if track in stores.playlist:
        edit_playlist_button.content = ft.FilledButton(
            text='Șterge din playlist',
            height=50,
            icon='delete_forever',
            on_click=update
        )
    else:
        edit_playlist_button.content = ft.FilledButton(
            text='Adaugă în playlist', 
            height=50, 
            icon='queue_music',
            on_click=update
        )

    song_info = ft.Column([
            ft.Container(
                ft.Column([
                        ft.Row([
                                ft.Image(src=track['image_url'], fit='fill', width=150, height=150),
                                ft.Column([
                                        ft.Text(track['track_name'], size=26, weight='w800'),
                                        ft.Text(', '.join(track['track_artists']), size=20, weight='w200')
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                    expand=True
                                )
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.START,
                        ),
                        ft.Divider(color='#e0e0e0'),
                        ft.Column([
                                ft.Text('Tempo: ' + str(int(track['tempo'])), size=20),
                                ft.Text('Dansabilitate: ' + str(int(track['danceability']*100)), size=20),
                                ft.Text('Energie: ' + str(int(track['energy']*100)), size=20),
                                ft.Text('Data lansării: ' + track['release_date'], size=20),
                            ],
                            wrap=True,
                        )
                    ],
                ),    
                padding=20,
                border_radius=25,
                bgcolor=radom_color(),
            ),
            ft.ResponsiveRow([
                ft.FilledButton(text='Descarcă', height=50, icon='download', col=6, on_click=lambda e: dl.spotify_download(track['track_id'])),
                edit_playlist_button
            ]),
            ft.TextButton(
                text='Închide',
                on_click=close,
                width=250,
                height=50,
            )
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    return song_info