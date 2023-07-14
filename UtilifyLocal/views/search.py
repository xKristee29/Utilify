import flet as ft
from modules.song_info import SongInfo

def Search(page: ft.Page):

    def toggle_song_info(e):
        song_info.visible = not song_info.visible
        song_info.update()

    song_info = ft.Column(
            [SongInfo(toggle=toggle_song_info).build()],
            col={'lg':4},
            expand=True,
        )

    tab = ft.ResponsiveRow([
        song_info,
        ft.Column([
            ft.Container(
                ft.Row([
                        ft.Container(
                            ft.Image(src='https://picsum.photos/200/200?1', fit='fill', width=150, height=150),
                            border_radius=25,
                            height=100,
                            width=100,
                            margin=ft.margin.only(left=10)
                        ),
                        ft.Container(
                            ft.Column([
                                    ft.Text('Song Name', size=20, weight='w800'),
                                    ft.Text('Artist Name', size=18, weight='w200')
                                ],
                                wrap=True,
                            ),
                            padding=10,
                            expand=True,
                        ),
                        ft.Container(
                            ft.Column([
                                    ft.ElevatedButton(text='Caută după melodie', width=150, height=100),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        )
                    ],
                ),
                bgcolor=ft.colors.BLUE_600,
                border_radius=25,
                padding=10,
                margin=10,
                on_click=toggle_song_info,
            )
        ],col={'lg':8})
    ],alignment=ft.MainAxisAlignment.CENTER)
    return tab
