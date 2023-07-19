import flet as ft
import stores
import notifier

def Settings(page: ft.Page):

    def save(e):
        stores.save_settings(
            download_field.value,
            playlist_field.value
        )
        notifier.notify('Setările au fost salvate cu succes!')

    download_field = ft.TextField(label="Calea de descărcare",multiline=False,value=stores.settings['download_path'])
    playlist_field = ft.TextField(label="Calea de salvare a playlist-urilor",multiline=False,value=stores.settings['playlist_path'])
    save_button = ft.FilledButton(
        icon='save',
        text='Salvează setările',
        height=50, width=140,
        on_click=save
    )

    tab = ft.ResponsiveRow([
        ft.Column([
            ft.Card(
                ft.Container(
                    ft.Column([
                            download_field,
                            playlist_field,
                            save_button
                        ],
                        spacing=20
                    ),
                    margin=20
                )
            )
        ],col={'md':7})
    ],alignment=ft.MainAxisAlignment.CENTER)
    return tab