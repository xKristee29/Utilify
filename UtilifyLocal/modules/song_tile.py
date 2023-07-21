import flet as ft
from colors import radom_color

class SongTile(ft.UserControl):
    def __init__(self, track, toggle_song_info, recommend = None):
        super().__init__()
        self.track = track
        self.toggle_song_info = toggle_song_info
        self.color = radom_color
        self.recommend = recommend
    
    def with_recommend(self):
        if self.recommend != None:
            return ft.Container(
                        ft.Column([
                                ft.ElevatedButton(icon ='lightbulb', text='Recomandă', width=130, height=70, on_click=lambda e: self.recommend(self.track['track_id'])),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    )
        return ft.Container()
    
    def build(self):
        song_tile = ft.Container(
            ft.Row([
                    ft.Container(
                        ft.Image(src=self.track['image_url'], fit='fill', width=100, height=100),
                        border_radius=25,
                        height=70,
                        width=70,
                        margin=ft.margin.only(left=10)
                    ),
                    ft.Container(
                        ft.Column([
                                ft.Text(self.track['track_name'], size=17, weight='w800'),
                                ft.Text(', '.join(self.track['track_artists']), size=13, weight='w200')
                            ],
                        ),
                        padding=10,
                        expand=True,
                    ),
                    self.with_recommend()
                ],
            ),
            bgcolor=self.color(),
            border_radius=25,
            padding=10,
            margin=5,
            on_click=lambda e: self.toggle_song_info(self.track),
        )
        return song_tile