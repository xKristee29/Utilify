import flet as ft
from colors import radom_color
import stores
import downloader as dl

def SongInfo(close, track):
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
                ft.FilledButton(text='Adaugă în playlist', height=50, icon='queue_music', col=6, on_click=lambda e: stores.add_track(track)),
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

def SongInfo2(close, track, remove_track):
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
                ft.FilledButton(text='Șterge din playlist', height=50, icon='delete_forever', col=6, on_click=lambda e: remove_track(track)),
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