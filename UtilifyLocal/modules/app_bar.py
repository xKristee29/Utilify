import flet as ft


def AppBar(page: ft.Page):
    app_bar = ft.AppBar(
        leading_width=40,
        title=ft.Text("Utilify"),
        bgcolor=ft.colors.BLUE_600,
        center_title=False,
        color=ft.colors.WHITE,
    )
    return app_bar
