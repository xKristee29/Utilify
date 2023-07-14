import flet as ft
from colors import radom_color

class SongInfo(ft.UserControl):
    def __init__(self, toggle):
        super().__init__()
        self.toggle = toggle

    def build(self):
        self.song_info = ft.Column([
                ft.Container(
                    ft.Column([
                            ft.Row([
                                    ft.Image(
                                        src="https://picsum.photos/200/200?1",
                                        width=150,
                                        height=150,
                                        fit=ft.ImageFit.NONE,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                        border_radius=10,
                                    ),
                                    ft.Column([
                                            ft.Text("Song Name", size=26, weight='w800'),
                                            ft.Text("Artist Name", size=20, weight='w200')
                                        ],
                                        alignment=ft.MainAxisAlignment.END,
                                        expand=True
                                    )
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.START,
                            ),
                            ft.Divider(color='#e0e0e0'),
                            ft.Column([
                                    ft.Text('Tempo: ', size=20),
                                    ft.Text('Dansabilitate: ', size=20),
                                    ft.Text('Energie: ', size=20),
                                    ft.Text('Data lansării: ', size=20),
                                ],
                                wrap=True,
                            )
                        ],
                    ),    
                    padding=20,
                    border_radius=25,
                    bgcolor=radom_color(),
                ),
                ft.TextButton(text='Închide',on_click=self.toggle,width=250)
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        return self.song_info