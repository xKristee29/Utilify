import flet as ft


def AppBar(page: ft.Page):
    
    def open_repo(e):
        page.launch_url('https://github.com/xKristee29/Utilify/tree/main/UtilifyPWA')

    app_bar = ft.AppBar(
        leading_width=40,
        title=ft.Text("Utilify"),
        bgcolor=ft.colors.BLUE_600,
        center_title=False,
        color=ft.colors.WHITE,
        actions=[ft.IconButton(icon=ft.icons.CODE, on_click=open_repo)]
    )
    return app_bar
